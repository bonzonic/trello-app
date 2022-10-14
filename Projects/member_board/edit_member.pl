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

my $id = param ('row');
my $sql = 'SELECT * FROM member where id=?';
my $sth = $dbh->prepare($sql);
$sth->execute($id);

while (my @row = $sth->fetchrow_array()) {
  my ($id, $name, $role, $email) = @row;

print qq~
<!DOCTYPE html>
<html>
    <head>
        <!--To view a member-->
        <title>View Member</title>
        <link rel="stylesheet" HREF="css/bootstrap.css" HREF="css/bootstrap-grid.css" HREF="css/bootstrap.min.css" HREF="css/bootstrap-grid.min.css" HREF="css/bootstrap-reboot.css" HREF="css/bootstrap-reboot.min.css" MEDIA="screen">
        <!--Style needed for the web browser-->
        <style>
            h4{
                color:#326EDB;
                font-weight: bold;
            }
            #main{
                margin: 100px;
                margin-left: 300px;
            }
        </style>
    </head>
    <body>
        <form action="save_member.pl" method="post">
            <div id="main">
                <div class="form-row">
                    <div class="form-group col-md-9">
                        <!--Title of the web page which is Member-->
                        <h4 id="newTask">Member</h4>
                    </div>
                    <div class="form-group col-md-9">
                        <!--A place holder to display the member's name-->
                      <label for="inputTaskName" style="font-weight:bold">Name :</label>
                      <input type="text" class="form-control" id="outputName" style="text-align: center; font-weight: bold;" name="name" value="$name">
                    </div>
                    <div class="form-group col-md-9">
                        <!--A place holder to display the member's role-->
                      <label for="inputTaskName" style="font-weight:bold">Role :</label>
                      <input type="text" class="form-control" id="outputRole" style="text-align: center; font-weight: bold;" name="role" value="$role">
                    </div>
                    <div class="form-group col-md-9">
                        <!--A place holder to display the member's email-->
                      <label for="inputTaskName" style="font-weight:bold">Email address:</label>
                      <input type="text" class="form-control" id="outputEmail" style="text-align: center; font-weight: bold;"name="email" value="$email">
                    </div>
                    
                    <div class="form-group col-md-9" style="margin-top:30px">
                        <!-- A button to delete member -->
                        <input type="hidden" name="row" class="btn btn-primary" value="$id">
				        <input type="submit" class="btn btn-primary" style="margin-right:10px; float:right;" value="Save">
                        </form>
                        <!-- A button to save and link to team board -->
                    </div>
                </div>
            </div>
    </body>
</html>
~;
}
$sth -> finish();
$dbh->disconnect;
