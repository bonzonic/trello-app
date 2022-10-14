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

my $task_id = param ('row');

my $sql = 'SELECT * FROM tasks where task_id=?';
my $sth = $dbh->prepare($sql);
$sth->execute($task_id);

print "Content-type: text/html \n\n";

print "<html>";

print "<body>";

while (my @row = $sth->fetchrow_array()) {
  my ($task_id, $task_name, $story_points, $description, $deadline_date, $task_type, $task_tag, $task_priority, $member) = @row;

my $sthi = $dbh->prepare("SELECT SUM(hour) as hours FROM task_member where task_id=?");
$sthi->execute($task_id);
my $count = $sthi->fetchrow_array();
$sthi->finish;

print qq~

<head>
	<LINK REL="STYLESHEET" TYPE="text/css" HREF="css/bootstrap.css" HREF="css/bootstrap-grid.css HREF="css/bootstrap.min.css HREF="css/bootstrap-grid.min.css HREF="css/bootstrap-reboot.css HREF="css/bootstrap-reboot.min.css" MEDIA="screen">\n
    <script src="script.js"></script>
    <style>
        #div1 {
            width:33.33%;
            float: left;
        }

        #div2 {
            width:33.33%;
            margin: 0 auto;
        }

        #div3 {
            width:20%;
            float: right;
        }
		#container-fluid{
            display:flex;
            flex-wrap:wrap;
        }
        table {
        counter-reset: tableCount;     
    }
    .counterCell:before {              
        content: counter(tableCount); 
        counter-increment: tableCount; 
    }
    </style>
    <title>view task</title>
</head>


<body>
            <div style="margin:50px;font-weight:bold;">
                <div class="container">
                    <div class="row">
                      <div class="col-sm-7">
                        <input type="text" class="form-control" id="outputTaskName" value="$task_name" style="text-align:center; font-weight: bold;" readonly>
                      </div>
                      <div class="col-sm-3" style="text-align:right">
                        <label for="outputMember" class="col-form-label" >Member: </label>
                      </div>
                      <div class="col-sm-2">
                        <input type="text" class="form-control" id="outputMember" style="text-align: center;"value="$member" readonly>
                      </div>
                    </div>
                    <div class="row" style="margin-top: 20px;">
                        <div class="col-sm-2">
                            <label for="outputStoryPoints" class="col-form-label">Story Points :</label>
                      </div>
                      <div class="col-sm-2">
                        <input type="number" class="form-control" id="outputStoryPoints" style="text-align: center;" value="$story_points" readonly>
                      </div>
                        <div class="col-sm-6" style="text-align:right">
                          <label for="time-cumulative" class="col-form-label">Cumulative Time Completed :</label>
                        </div>
                        <div class="col-sm-2">
                          <input type="number" class="form-control" id="time-cumulative" style="text-align: center;"value="$count"readonly>
                        </div>
                      </div>

                    <div style="margin-top:20px ;">
                        <button type="button" class="btn btn-dark btn-sm" style="float: right;margin-left: 30px;"  data-toggle="modal" data-target="#exampleModalCenter">History</button>
                    </div>
                    <!--  the popup stuff is here -->
                    <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                      <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                          <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLongTitle">$task_name</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                              <span aria-hidden="true">&times;</span>
                            </button>
                          </div>
                          <div class="modal-body">
                            <table class="table">
                              <thead>
                                  <tr>
                                  <th scope="col">#</th>
                                  <th scope="col">Date and Time</th>
                                  <th scope="col">Hours completed</th>
                                  </tr>
                              </thead>
                              <tbody>
                              ~;
# getting all the values for the history
my $sql = 'SELECT * FROM task_member where task_id=?';
my $sthi = $dbh->prepare($sql);
$sthi->execute($task_id);

while (my @rows = $sthi->fetchrow_array()) {
  my ($task_id, $date, $hour) = @rows;
  print qq~
                                  <tr>
                                  <th scope="row" class="counterCell"></th>
                                  <td>$date</td>
                                  <td>$hour</td>
                                  </tr>
    ~
}
                              print qq~
                              </tbody>
                              </table>
                          </div>
                          <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div>
                        <label style="margin-top:40px ;">Description :</label>
                        <textarea style="margin-top:30px" name="description" class="form-control" rows="6" placeholder="This is my description for this task" readonly>$description</textarea>
                    </div>

                    <div class="row" style="margin-top:45px">
                        <div class="col-sm-2">
                            <label for="deadlineDate" class="col-form-label" >Deadline Date :</label>                       
                        </div>
                        <div class="col-sm-3">
                          <input type="date" value="$deadline_date" class="form-control" id="deadlineDate" style="text-align: center;" readonly>
                        </div>
                    </div>

                    <div class="row" style="margin-top:45px">
                        <div class="col-sm-2">
                            <label for="Type" class="col-form-label" >Type :</label>                       
                        </div>
                        <div class="col-sm-3">
                          <input type="Text" class="form-control" id="Type" style="text-align: center;" value="$task_type" readonly>
                        </div>
                    </div>

                    <div class="row" style="margin-top:45px">
                        <div class="col-sm-2">
                            <label for="Priority" class="col-form-label" >Priority :</label>                       
                        </div>
                        <div class="col-sm-3">
                          <input type="Text" class="form-control" id="Type" style="text-align: center;" value="$task_priority" readonly>
                        </div>
                    </div>

                    <div class="row" style="margin-top:45px">
                        <div class="col-sm-2">
                            <label for="Tags" class="col-form-label" >Tag :</label>                       
                        </div>
                        <div class="col-sm-3">
                          <input type="Text" class="form-control" id="Type" style="text-align: center; " value="$task_tag" readonly>
                        </div>
                    </div>
          <div style="margin-bottom:150px; margin-top:50px;">
            <a class="btn btn-primary" href="task_board_db.cgi" role="button" style="float: right;margin-right: 15px;">Exit</a>
              
			  <form action="edit_task_db.cgi">
				<input type="hidden" name="row" class="btn btn-primary" value="$task_id">
				<input class="btn btn-primary" type="submit" value="Edit" style="float: left;margin-right: 15px;">
			</form>
			  
              <form action="delete_task.cgi">
                <input type="hidden" name="row" class="btn btn-primary" value="$task_id">
                <input class="btn btn-primary" type="submit" value="Delete" style="float: left;margin-right: 15px;">
              </form>
          </div>                  


            </div>
            

~;
}
$sth -> finish();
$dbh->disconnect;
print "</body></html>";
