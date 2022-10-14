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
my $name = param('name');
my $role = param('role');
my $email = param('email');

my $check = qq{
  UPDATE member
  set name = ?,
  role = ?,
  email = ? 
  WHERE id = ?
};

my $sth = $dbh->prepare($check);
$sth->execute($name, $role, $email, $id);


my $url = "team_board.pl";
my $q = CGI->new;
print $q->redirect($url);

$sth->finish();
$dbh->commit;
$dbh->disconnect;
 
