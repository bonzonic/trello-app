#!c:/Strawberry/perl/bin/perl.exe

use strict;
use warnings;
 
use DBI;
use HTML::Template;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);



my $q= new CGI;

CGI::Link({
  -rel   => 'stylesheet',
  -type  => 'text/css',
  -src   => '/css/bootstrap.css',
  -media => 'all'
});



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


my $id = param('row');
my $task_name = param ('new_task_name');
my $story_points = param ('new_story_points');
my $description = param('new_description');
my $deadline_date =  param('new_deadline_date');
my $task_type =  param ('new_task_type');
my $task_tag = param ('new_task_tags');
my $task_priority =  param ('new_task_priority');
my $member = param ('new_member');
my $priority_id;
my $priority_hex;
my $hours_completed = param("hours_completed");
my $date_completed = param("date_completed");


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


my $check = qq{
  UPDATE tasks
  set task_name = ?, 
  story_points = ?, 
  descrip = ?, 
  deadline_date = ?, 
  task_type = ?, 
  task_tags = ?, 
  task_priority = ?, 
  members = ?,
  priority_id = ?,
  priority_hex = ?
  WHERE task_id = ?
};

my $sth = $dbh->prepare($check);
$sth->execute($task_name, $story_points, $description, $deadline_date, $task_type, $task_tag, $task_priority, $member, $priority_id, $priority_hex, $id);

$dbh->do("INSERT INTO task_member(task_id, date, hour) VALUES ('$id', '$date_completed', '$hours_completed')");


my $url = "task_board_db.cgi";
my $q = CGI->new;
print $q->redirect($url);


print "Content-type: text/html \n\n";

print "<html>";
print "<body>";

$sth->finish();
$dbh->commit;
$dbh->disconnect;
print "</body></html>";
 

