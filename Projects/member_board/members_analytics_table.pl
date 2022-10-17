#!c:/Strawberry/perl/bin/perl.exe

use strict;
use warnings;
 
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use DBI;
use HTML::Template;


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
my $start_date = param ('start_date');
my $end_date = param('end_date');

print "Content-type: text/html \n\n";

print qq~
<!DOCTYPE html>
<html lang="en" >
    <head>
        <title>Member Analytics</title>
        <link rel="stylesheet"  HREF="css/bootstrap.css" HREF="css/bootstrap-grid.css" HREF="css/bootstrap.min.css" HREF="css/bootstrap-grid.min.css" HREF="css/bootstrap-reboot.css" HREF="css/bootstrap-reboot.min.css" MEDIA="screen">
    <style>
    table {
        counter-reset: tableCount;     
    }
    .counterCell:before {              
        content: counter(tableCount); 
        counter-increment: tableCount; 
    }
    </style>
    </head>
    <body style="background-color:#DCEBFF; margin-top: 5%; ">
        <div class="container" style= text-align:center;">
            <div class="row">
                <div class="col">
                    <div class="card" style="width: auto;height: auto; border-radius: 20px;">
                        <div class="card-body">
                            <table class="table table-striped">
                                <div style="margin-bottom: 5%;"><h2>Team Member's work analytics from $start_date to $end_date</h2></div>
                                <thead>
                                  <tr>
                                    <th scope="col">#</th>
                                    <th scope="col">Team Member</th>
                                    <th scope="col">Total Hours worked</th>
                                    <th scope="col">Average Hours Worked</th>
                                  </tr>
                                </thead>
                                <tbody>
                                ~;
my $sql_checking_date = "SELECT (JulianDay(?) - JulianDay(?))";
my $sth_check_date = $dbh->prepare($sql_checking_date);
$sth_check_date->execute($end_date, $start_date);
my $no_of_dates = $sth_check_date->fetchrow();
my $sql = 'SELECT name, id FROM member';
my $sth = $dbh->prepare($sql);
$sth->execute();
#  grabbing each member 
while (my $row = $sth->fetchrow_hashref) {
  my $sql2 = 'SELECT task_id FROM tasks where member_id=?';
  my $sth2 = $dbh->prepare($sql2);
  $sth2->execute($row->{id});
  my $count = 0;

#  grabbing the tasks of the member
  while (my $rows = $sth2->fetchrow_hashref) {
    my $task_id = $rows->{task_id};
    my $sth3 = $dbh->prepare("SELECT SUM(hour) as hours FROM task_member where task_id=? and date between ? and ?");
    $sth3->execute($task_id, $start_date, $end_date);
    $count += $sth3->fetchrow_array(); # calculating each tasks number of hours
    $sth3->finish;
  }
my $result = $count/$no_of_dates;
my $rounded = sprintf("%.2f", $result); 

print qq~	
                                  <tr>
                                    <th scope="row" class="counterCell"></th>
                                    <td>$row->{name}</td>
                                    <td>$count</td>
                                    <td>$rounded</td>
                                  </tr>
~;
}
print qq~;
                                </tbody>
                              </table>
                        </div>
                      </div>
                </div>
            </div>
        </div>
        <div style="text-align:right; margin-right: 2%; margin-top:auto;">
            <a href="team_board.pl" class="btn btn-primary" >Back</a>
        </div>
    </body>
</html>
~;

$dbh->disconnect();
