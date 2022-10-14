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

my $sql = 'SELECT name FROM member';
my $sth = $dbh->prepare($sql);
$sth->execute();

print "Content-type: text/html \n\n";

print qq~

<!DOCTYPE html>
<html>

<head>
    <title>create task</title>
    <script src="script.js"></script>
    <link rel="stylesheet" HREF="css/bootstrap.css" HREF="css/bootstrap-grid.css" HREF="css/bootstrap.min.css" HREF="css/bootstrap-grid.min.css" HREF="css/bootstrap-reboot.css" HREF="css/bootstrap-reboot.min.css" MEDIA="screen">
    <link rel="stylesheet" href="create_task.css">
</head>

<body>
    <form action = "test2.cgi" method = "get">
        <div id="main">
            <h4 id="newTask">NEW TASK</h4>
            <div class="form-row">
                <div class="form-group col-md-9">
                    <label for="inputTaskName">Task Name :</label>
                    <input type="text" class="form-control" id="inputTaskName" placeholder="Enter task name" name="task_name" size = "size">
                </div>
                <div class="form-group col-md-3">
                    <label for="inputStoryPoints">Story Points :</label>
                    <input type="number" class="form-control" id="inputStoryPoints" name="story_point">
                </div>
            </div>
            <div class="form-group">
                <label>Description :</label>
                <textarea name="description" class="form-control" rows="5" placeholder="Add description"></textarea>
            </div>
            <div class="form-row">
                <div class="form-group col-md-3">
                    <label for="date">Deadline Date:</label>
                    <input type="date" class="form-control" id="deadlineDate" name="dead_date">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-3">
                    <label for="inputGroupSelect01">Task Type: </label>
                    <select class="form-select form-control" id="inputGroupSelect01" name="task_type">
                        <option disabled selected>Choose your option</option>
                        <option value="User Story">User Story</option>
                        <option value="Bug">Bug</option>
                        <option value="Report">Report</option>
                    </select>
                </div>
                <div class="form-group col-md-3">
                    <label for="inputGroupSelect01">Task Tags: </label>
                    <select class="form-select form-control" id="inputGroupSelect01" name="task_tags">
                        <option disabled selected>Choose your option</option>
                        <option value="Testing">Testing</option>
                        <option value="UI">UI</option>
                        <option value="Core">Core</option>
                    </select>
                </div>
                <div class="form-group col-md-3">
                    <label for="inputGroupSelect01">Task Priority: </label>
                    <select class="form-select form-control" id="inputGroupSelect01" name="task_priority">
                        <option disabled selected>Choose your option</option>
                        <option value="Low">Low</option>
                        <option value="Medium">Medium</option>
                        <option value="High">High</option>
                        <option value="Critical">Critical</option>
                    </select>
                </div>
                <div class="form-group col-md-3">
                    <label for="inputGroupSelect01">Task Members: </label>
                    <select class="form-select form-control" id="inputGroupSelect01" name="members">
                        <!-- needs to get the members from the database -->
                        <option disabled selected>Choose your option</option>
                        ~;
while (my @row = $sth->fetchrow_array()) {
  my ($name) = @row;
  print qq~
  <option value="$name">$name</option>
~;
}
  print qq~
                    </select>
                </div>
            </div>
            <div style="margin-top:80px">
				 
                <input class="btn btn-primary" type="submit" value="Done" style="float: right;">
				
                <a class="btn btn-primary" href="task_board_db.cgi" role="button" style="float: right;margin-right: 15px;">Cancel</a>
            </div>
        </div>
    </form>
</body>

</html>
~;
   

$dbh->disconnect;