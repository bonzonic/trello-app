#!c:/Strawberry/perl/bin/perl.exe

use strict;
use warnings;
 
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
 
 
use DBI;



my $dbfile = "../backlog.db";
 
my $dsn  = "dbi:SQLite:dbname=$dbfile";
my $user = "";
my $password = "";
my $dbh = DBI->connect($dsn, $user, $password, {
   PrintError   => 0,
   RaiseError   => 1,
   AutoCommit   => 1,
   FetchHashKeyName => 'NAME_lc',
});
 


my $task_name = param ('task_name');
my $story_points = param ('story_point');
my $descrip = param('description');
my $deadline_date =  param('dead_date');
my $task_type =  param ('task_type');
my $task_tags = param ('task_tags');
my $task_priority =  param ('task_priority');
my $members = param ('members');
my $priority_id;
my $priority_hex;
my $member_id;

if($task_priority eq "Critical"){
	$priority_id = 1;
	$priority_hex = "#EC0000";
}elsif($task_priority eq "High"){
	$priority_id = 2;
	$priority_hex = "#FF7515";
}elsif($task_priority eq "Medium"){
	$priority_id = 3;
	$priority_hex = "#F1C40F";
}else{
	$priority_id = 4;
	$priority_hex = "#39C000";
}

my $sql = 'SELECT id, name FROM member';
my $sth = $dbh->prepare($sql);
$sth->execute();

while (my @row = $sth->fetchrow_array()) {
  my ($id, $name) = @row;
  if ($members eq $ name) {
	$member_id = $id;
  }
}
  
$dbh->do('INSERT INTO tasks(task_name, story_points, descrip, deadline_date, task_type, task_tags, task_priority, members, priority_id, priority_hex, member_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
		undef, 
		$task_name, $story_points, $descrip, $deadline_date, $task_type, $task_tags, $task_priority, $members, $priority_id, $priority_hex, $member_id);


my $url = "task_board_db.cgi";
my $q = CGI->new;
print $q->redirect($url);

print "Content-type: text/html \n\n";

print "<html>";
print "<body>";

print "</body></html>";




	    

$dbh->disconnect;