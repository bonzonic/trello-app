#!C:\Strawberry\perl\bin\perl.exe

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
  -src   => 'css/bootstrap.css',
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

my $sprint_id = param ('row');

my $sql = 'Delete FROM sprints where sprint_id=?';
my $sth = $dbh->prepare($sql);
$sth->execute($sprint_id);

my $url = "sprint_board_db.cgi";
my $q = CGI->new;
print $q->redirect($url);

print "Content-type: text/html \n\n";

print "<html>";
print "<body>";

print "</body></html>";


	    
$sth -> finish();
$dbh -> commit;
$dbh->disconnect;