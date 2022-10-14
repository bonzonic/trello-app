#!/usr/bin/perl

use strict;
use warnings;
 
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
 
 
use DBI;

my $dbfile = "backlog.db";
 
my $dsn  = "dbi:SQLite:dbname=$dbfile";
my $user = "";
my $password = "";
my $dbh = DBI->connect($dsn, $user, $password, {
   PrintError   => 0,
   RaiseError   => 1,
   AutoCommit   => 1,
   FetchHashKeyName => 'NAME_lc',
});
 
 
 
my $sprint_name = param ('sprint_name');
my $start_date = param ('start_date');
my $end_date = param('end_date');
my $task_id_list = 0;
my $get_started_bool = 0;

my $count = 0;
my ($count) = $dbh->selectrow_array('SELECT COUNT (*) FROM sprints');
$count = $count + 1;



$dbh->do('INSERT INTO sprints(sprint_id, sprint_name, start_date, end_date, task_id_list, get_started_bool) VALUES (?, ?, ?, ?, ?, ?)',
		undef, 
		$count, $sprint_name, $start_date, $end_date, $task_id_list, $get_started_bool );


my $url = "http://127.0.0.1/pb_sb_db.cgi";
my $q = CGI->new;
print $q->redirect($url);

print "Content-type: text/html \n\n";

print "<html>";
print "<body>";

print "</body></html>";

$dbh->disconnect;