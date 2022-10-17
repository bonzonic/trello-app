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

print "Content-type: text/html \n\n";

print "<html>";

print qq~
    <head>
        <title>Team board</title>
        <link rel="stylesheet"  HREF="css/bootstrap.css" HREF="css/bootstrap-grid.css" HREF="css/bootstrap.min.css" HREF="css/bootstrap-grid.min.css" HREF="css/bootstrap-reboot.css" HREF="css/bootstrap-reboot.min.css" MEDIA="screen">
        <!-- Styling for the layout of the page and cards-->
        <style>
            #main{
                margin: 50px;
            }
            .card-header{

                text-align: center;
            }
            .card{
                border-radius: 20px;
               
            }
            .row{
                margin-top: 20px;
            }
        </style>
    </head>
    <!-- Setting the board colour-->
    <body style="background-color:#DCEBFF;">
        <div id="main">
            <!-- Adding buttons in the same row -->
            <div class="form-row">
                <div class="form-group col-md-4" >
                     <!--space-->
                </div>

                <div class="form-group col-md-8">
                    <!-- Button to view sprint-->
                    <a class="btn btn-primary" href="../sprint_board/sprint_board_db.cgi" role="button" style="float: right; margin-left:10px;">View Sprint</a>
                    <!-- Button to view the task -->
                    <a class="btn btn-primary" href="../task_board/task_board_db.cgi" role="button" style="float: right; margin-left:10px">View Task</a>
                    <!-- Button to view the team dashboard-->
                    <a class="btn btn-dark" href="team_dashboard.html" role="button" style="float: right;">Team Dashboard</a>
                </div>
            </div>	
            
            <div style="margin-top:30px;margin-left:150px;margin-right:150px;">
                <div class="card-deck">
                       <!-- Creating a card for each team -->
                       
                        <div class="card">
                            <div class="card-header">
                                <!--Displaying team's name-->
                                <div class="row" >
                                    <div class="col-sm-4">
                                        <!--space--> 
                                    </div>
                                    <!--Creating team headings-->
                                    <div class="col-sm-3">
                                        <label for="teamName" style="font-weight:bold; font-size: 25px;">Team</label> 
                                    </div>

                                    <!--Button to add members into the team-->
                                    <div class="col-sm-5">
                                        <a class="btn btn-outline-dark" href="add_member.html" role="button" style="float: right;">+</a>
                                    </div>
                                </div>
                            </div>
                                                        ~;
my $sql = 'SELECT * FROM member';
my $sth = $dbh->prepare($sql);
$sth->execute();
while (my $row = $sth->fetchrow_hashref) {		
print qq~	
                            <!--Creating team body-->
                            <div class="card-body">
                                <div class="row">
                                    <!--Creating team member-->
                                    <div class="col-sm-9">
                                        <label for="teamName" style="font-weight:bold; font-size: 21px;">$row->{name}</label>
                                    </div>
                                   <!-- Button to view member-->
                                   <div class="col-sm-2">
                                    <form action="view_member.pl">
                                      <input type="hidden" name="row" class="btn btn-primary" value="$row->{id}">
                                      <input type="submit" class="btn btn-secondary" style="margin-right:30px;float: right;" value="View">	
                                    </form>
                                  </div>
                                    <!--Button to see the analytics for a member-->
                                    <div class="col-sm-1">
                                        <form action="member_analytics.pl">
                                            <input type="hidden" name="row" class="btn btn-primary" value="$row->{id}"> 
                                            <input type="submit" class="btn btn-dark" role="button" style="float: right;" value="Analytics">
                                        </form>
                                    </div>
                                </div>
                            </div>
            ~;
}
print qq~
                        </div>
                </div>
            </div>
        </div>

    </body>
</html>

~;

$dbh->disconnect();
