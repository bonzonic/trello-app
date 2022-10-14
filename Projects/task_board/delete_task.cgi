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
 
my $task_id = param ('row');

my $sql = 'Delete FROM tasks where task_id=?';
my $sth = $dbh->prepare($sql);
$sth->execute($task_id);
my $sql = 'Delete FROM task_member where task_id=?';
my $sth = $dbh->prepare($sql);
$sth->execute($task_id);

my $url = "task_board_db.cgi";
my $q = CGI->new;
print $q->redirect($url);

print "Content-type: text/html \n\n";

print "<html>";
print "<body>";

print "</body></html>";




	    
$sth -> finish();
$dbh -> commit;
$dbh->disconnect;