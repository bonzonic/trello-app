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

my $id = param ('row');
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

print "Content-type: text/html \n\n";

print qq~;
<!DOCTYPE html>
<html lang ='en'>
    <head>
    <title>Member Analytics</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap\@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>

    <body style="background-color:#DCEBFF; margin-top: 5%; ">
        <div class="container" style= text-align:center;">
            <div class="row">
                <div class="col">
                    <div class="card" style="width: auto; border-radius: 20px;">
                        <div class="card-body">
                            <div>
                                <canvas id="myChart"></canvas>
                              </div>
                        </div>
                      </div>
                </div>
            </div>
        </div>
        <div style="text-align:right; margin-right: 2%; margin-top:auto;">
            <a href="team_board.pl" class="btn btn-primary" >Back</a>
        </div>
        ~;

my $sql = "SELECT name from member where id=?";
my $sth = $dbh->prepare($sql);
$sth->execute($id);
my $name = $sth->fetchrow();

# today
my $sql = "SELECT DATE('now')";
my $sth = $dbh->prepare($sql);
$sth->execute();
my $date = $sth->fetchrow();

# yesterday
my $sql = "SELECT DATE('now', '-1 day')";
my $sth = $dbh->prepare($sql);
$sth->execute();
my $date_1day = $sth->fetchrow();

# the day before yesterday
my $sql = "SELECT DATE('now', '-2 day')";
my $sth = $dbh->prepare($sql);
$sth->execute();
my $date_2day = $sth->fetchrow();

# 3rd 
my $sql = "SELECT DATE('now', '-3 day')";
my $sth = $dbh->prepare($sql);
$sth->execute();
my $date_3day = $sth->fetchrow();

# 4th
my $sql = "SELECT DATE('now', '-4 day')";
my $sth = $dbh->prepare($sql);
$sth->execute();
my $date_4day = $sth->fetchrow();

# 5th
my $sql = "SELECT DATE('now', '-5 day')";
my $sth = $dbh->prepare($sql);
$sth->execute();
my $date_5day = $sth->fetchrow();

# 6th
my $sql = "SELECT DATE('now', '-6 day')";
my $sth = $dbh->prepare($sql);
$sth->execute();
my $date_6day = $sth->fetchrow();

#  ------------------------------------------------- values

my $sql = 'SELECT task_id FROM tasks where member_id =?';
my $sth = $dbh->prepare($sql);
$sth->execute($id);
my $count = 0;
my $count2 = 0;
my $count3 = 0;
my $count4 = 0;
my $count5 = 0;
my $count6 = 0;
my $count7 = 0;
# for each task id, i calculate the time where the date is the same 
while (my $row = $sth->fetchrow_hashref) {
    my $sth3 = $dbh->prepare("SELECT SUM(hour) as hours FROM task_member where task_id=? and date(date)=?");
    $sth3->execute($row->{task_id}, $date);
    $count += $sth3->fetchrow_array(); # calculating each tasks number of hours
    $sth3->execute($row->{task_id}, $date_1day);
    $count2 += $sth3->fetchrow_array(); # calculating each tasks number of hours
    $sth3->execute($row->{task_id}, $date_2day);
    $count3 += $sth3->fetchrow_array(); # calculating each tasks number of hours
    $sth3->execute($row->{task_id}, $date_3day);
    $count4 += $sth3->fetchrow_array(); # calculating each tasks number of hours
    $sth3->execute($row->{task_id}, $date_4day);
    $count5 += $sth3->fetchrow_array(); # calculating each tasks number of hours
    $sth3->execute($row->{task_id}, $date_5day);
    $count6 += $sth3->fetchrow_array(); # calculating each tasks number of hours
    $sth3->execute($row->{task_id}, $date_6day);
    $count7 += $sth3->fetchrow_array(); # calculating each tasks number of hours
    $sth3->finish;
}

print qq~
        <script>
            const labels = [
              '$date_6day',
              '$date_5day',
              '$date_4day',
              '$date_3day',
              '$date_2day',
              '$date_1day',
              'Today',
            ];
          
            const data = {
              labels: labels,
              datasets: [{
                label: '$name',
                backgroundColor: 'rgb(0, 90, 211)',
                borderColor: 'rgb(0, 90, 211)',
                data: [$count7, $count6, $count5, $count4, $count3, $count2, $count],
              }]
            };
          
          </script>
          <script>
            const myChart = new Chart(
              document.getElementById('myChart'),
              {
                type: 'bar',
                data: data,
                options: {
                    plugins: {
                        title: {
                            display: true,
                            text: 'Work Analytics of $name Over the 7 Days',
                            font:{
                                size: 35
                            }
                                }
                            },
                    scales: {
                        y:{
                         title:{
                            display: true,
                            text: 'Hours Worked'
                         }   
                        },
                        x:{
                            title:{
                                display:true,
                                text:'Days of the Week'
                            }
                        }
                    }
                        }
            });
          </script>
    </body>
~;