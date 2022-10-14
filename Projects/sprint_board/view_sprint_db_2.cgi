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


my $sprint_id = param ('row');
my $get_started_bool = param('row2');

my $check = qq{
  UPDATE sprints
  set get_started_bool = ?
  WHERE sprint_id = ?
};

my $sth2 = $dbh->prepare($check);
$sth2->execute($get_started_bool, $sprint_id);




my $sql = 'SELECT * FROM sprints WHERE sprint_id=?';
my $sth = $dbh->prepare($sql);
$sth->execute($sprint_id);


print "Content-type: text/html \n\n";

print "<html>";


print "<body>";


while (my @row = $sth->fetchrow_array()) {
  my ($sprint_id, $sprint_name, $start_date, $end_date, $task_id_list) = @row;	

  
print qq~



	
<head>
	<title>View Sprint</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<LINK REL="STYLESHEET" TYPE="text/css" HREF="css/bootstrap.css" HREF="css/bootstrap-grid.css HREF="css/bootstrap.min.css HREF="css/bootstrap-grid.min.css HREF="css/bootstrap-reboot.css HREF="css/bootstrap-reboot.min.css" MEDIA="screen">\n
	
</head>



    <body>
		<form action = "delete_sprint_db.cgi">
            <div id="main">
                <div class="form-row">
                    <!-- A placeholder to display the name of the sprint-->
                    <div class="form-group col-md-11">
                      <input type="text" class="form-control" id="inputTaskName" value = "$sprint_name" placeholder="SPRINT 1" style="text-align: center;font-weight: bold;"readonly>
                    </div>
                </div>
                <div class="form-row">
                    <!-- A column  to display the word "Start Date :"-->
                    <div class="form-group col-md-2">
                        <label for="startDate" style="font-weight:bold">Start Date :</label>
                    </div>

                    <!--A placeholder to display the start date input of the sprint-->
                    <div class="form-group col-md-3">
                        <input type="date" class="form-control" id="startDate" name="start_date" value = "$start_date"  style="text-align: center;" readonly>
                    </div>
                </div>

                <div class="form-row">
                    <!-- A column to display the word "End date :"-->
                    <div class="form-group col-md-2">
                        <label for="endDate" style="font-weight:bold">End Date :</label>
                    </div>
                    <!-- A placeholder to display the input of the end date of the sprint-->
                    <div class="form-group col-md-3">
                        <input type="date" class="form-control" id="endDate" name="end_date" value = "$end_date"  style="text-align: center;" readonly>
                    </div>
                </div>

                <div class="form-row" style="margin-top:50px;">
                    <!-- To Do Board -->
                    <div class="form-group col-md-3">
                        <div id='list1' class="board-list" ondrop="dropIt(event)" ondragover="allowDrop(event)">
                            <!--Title of the board "Not Started"-->
                            <div class="list-title" >
                              Not Started
                            </div>
                            <!-- Task in the To Do board-->
                              <div  id='card1' class="card" draggable="true" ondragstart="dragStart(event)">
                              Task 1
                              </div>
                              <div  id='card2' class="card" draggable="true" ondragstart="dragStart(event)">
                              Back up database
                              </div>
                              <div id='card3' class="card" draggable="true" ondragstart="dragStart(event)">
                              Build Lambda function
                              </div>
                              <div id='card4' class="card" draggable="true" ondragstart="dragStart(event)">
                                Testing
                                </div>
                            <div id='card4' class="card" draggable="true" ondragstart="dragStart(event)">
                                Design UI
                                </div>
                          </div>
                    </div>

                    <div class="form-group col-md-1">
                        <!-- space -->
                    </div>

                    <!-- Second Board "In Progress"-->
                    <div class="form-group col-md-3">
                        <div  id='list2' class="board-list" ondrop="dropIt(event)" ondragover="allowDrop(event)">
                            <div  class="list-title">
                            In Progress
                            </div>
                          </div>
                    </div>

                    <div class="form-group col-md-1">
                        <!-- space -->
                    </div>

                    <!--Thrird Board "Completed"-->
                    <div class="form-group col-md-3">
                        <div  id='list3' class="board-list"  ondrop="dropIt(event)" ondragover="allowDrop(event)">
                            <div  class="list-title">
                              Completed
                              </div>
                              </div>
                        </div>
                </div>

                <!-- Button in the View sprint which carries out a specific instruction-->
                <div style="margin-top:30px ;">
                    <!-- A button to end sprint-->
					<input type="hidden" name="row" class="btn btn-primary" value = "$sprint_id">
                    <input class="btn btn-primary" type = "submit" role="button" value = "End Sprint" style="float:right;">
                    <!--A button to edit the sprint-->
                    <a class="btn btn-primary" href="#" role="button" style="float:right;margin-right: 15px;">Edit</a>
                    <!--A button to exit the sprint-->
                    <a href = "sprint_board_db.cgi" class="btn btn-primary" style="float:;"role="button">Exit</a>
                </div>


                </div>
                
                
            </div>
        
		</form>
    
    </body>


~;
}



$sth -> finish();
$dbh->disconnect;
print "</body></html>";

