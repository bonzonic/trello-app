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
 
my $task_id = param ('value');
my $sprint_name = param('sprintName');
my $sprintStartDate = param('sprintStartDate');
my $sprintEndDate = param('sprintEndDate');
my $get_started_bool = 0;
my $assigned_to_sprint = 0;

my $count = 0;
my ($count) = $dbh->selectrow_array('SELECT COUNT (*) FROM sprints');
$count = $count + 1;

my @spl = split(',', $task_id);
my $length = @spl;

for my $a (0..$length-1){

   $dbh->do('update tasks set assigned_to_sprint = 1 where task_id = ?', undef, $spl[$a]);
}


$dbh->do('INSERT INTO sprints(sprint_id , sprint_name, start_date, end_date, task_id_list, get_started_bool) VALUES (?, ?, ?, ?, ?, ?)', undef, $count, $sprint_name, $sprintStartDate, $sprintEndDate,@spl, $get_started_bool);

my $url = "sprint_board_db.cgi";
my $q = CGI->new;
print $q->redirect($url);

print "Content-type: text/html \n\n";

print "<html>";
print "<body>";

print "</body></html>";


$dbh->disconnect;