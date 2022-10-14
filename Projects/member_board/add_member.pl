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
 

my $name = param("inputName");
my $role = param("inputRole");
my $email = param("inputEmail");

$dbh->do('INSERT INTO member(name, role, email) VALUES (?, ?, ?)',
		undef, 
		$name, $role, $email);

my $url = "team_board.pl";
my $q = CGI->new;
print $q->redirect($url);

print "Content-type: text/html \n\n";

print "<html>";
print "<body>";

print "</body></html>";




	    

$dbh->disconnect;