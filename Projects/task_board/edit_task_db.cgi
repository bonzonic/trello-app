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
 
 my $task_id = param ('row');

my $sql = 'SELECT * FROM tasks where task_id=?';
my $sth = $dbh->prepare($sql);
$sth->execute($task_id);

print "Content-type: text/html \n\n";

print "<html>";


print "<body>";

while (my @row = $sth->fetchrow_array()) {
  my ($task_id, $task_name, $story_points, $description, $deadline_date, $task_type, $task_tag, $task_priority, $member) = @row;
print qq~

<head>
	<LINK REL="STYLESHEET" TYPE="text/css" HREF="css/bootstrap.css" HREF="css/bootstrap-grid.css HREF="css/bootstrap.min.css HREF="css/bootstrap-grid.min.css HREF="css/bootstrap-reboot.css HREF="css/bootstrap-reboot.min.css" MEDIA="screen">\n
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
		
    </style>
    <title>view task</title>
</head>


<body>
		<form action="saving_task_db.cgi" method="post">
			<div style="margin:50px;font-weight:bold;">
				<div class="container">

					<div class="row">
					  <div class="col-sm-7">
						<input type="text" class="form-control" id="outputTaskName" value="$task_name" name= "new_task_name" style="text-align:center; font-weight: bold;" >
					  </div>
					  <div class="col-sm-3" style="text-align:right">
						<label for="outputMember" class="col-form-label" >Member: </label>
					  </div>
					  <div class="col-sm-2">
                        <input type="text" class="form-control" id="outputMember" style="text-align: center;"name="new_member" value="$member" readonly>
					  </div>
					</div>

					<div class="row" style="margin-top: 20px;">
					  <div class="col-sm-7">
						<!--space-->
					</div>
					  <div class="col-sm-3" style="text-align:right">
						<label for="time-completed" class="col-form-label">Hours Done :</label>
					  </div>
					  <div class="col-sm-2">
						<input type="number" class="form-control" id="time-completed" name="hours_completed" style="text-align: center;"placeholder="0" >
					  </div>
					</div>

					<div class="row" style="margin-top: 20px;">
						<div class="col-sm-2">
							<label for="outputStoryPoints" class="col-form-label">Story Points :</label>
					  </div>
					  <div class="col-sm-2">
						<input type="number" class="form-control" id="outputStoryPoints" style="text-align: center;"value="$story_points" name= "new_story_points" >
					  </div>
						<div class="col-sm-6" style="text-align:right">
						  <label for="date_completed" class="col-form-label">Date :</label>
						</div>
						<div class="col-sm-2">
						  <input type="datetime-local" class="form-control" name="date_completed" id="date_completed" style="text-align: center;">
						</div>
					  </div>

					<div>
						<label style="margin-top:40px ;">Description :</label>
						<textarea style="margin-top:30px" value="description" name= "new_description" class="form-control" rows="6" placeholder="This is my description for this task" >$description</textarea>
					</div>

					<div class="row" style="margin-top:45px">
						<div class="col-sm-2">
							<label for="deadlineDate" class="col-form-label" >Deadline Date :</label>                       
						</div>
						<div class="col-sm-3">
						  <input type="date" value="$deadline_date" name="new_deadline_date" class="form-control" id="deadlineDate" style="text-align: center;" >
						</div>
					</div>

					<div class="row" style="margin-top:45px">
						<div class="col-sm-2">
							<label for="Type" class="col-form-label" >Type :</label>                       
						</div>
						<div class="col-sm-3">
							<select class="form-select form-control" id="inputGroupSelect01" name="new_task_type">
~;
if ($task_type eq "User Story") {
	print "<option selected value='User Story'>User Story</option>";
	print "<option value='Bug'>Bug</option>";
	print "<option value='Report'>Report</option>";
}
elsif ($task_type eq "Bug") {
	print "<option value='User Story'>User Story</option>";
	print "<option selected value='Bug'>Bug</option>";
	print "<option value='Report'>Report</option>";
}

else {
	print "<option value='User Story'>User Story</option>";
	print "<option value='Bug'>Bug</option>";
	print "<option selected value='Report'>Report</option>";
}
print qq~
							</select>
						</div>
					</div>

					<div class="row" style="margin-top:45px">
						<div class="col-sm-2">
							<label for="Priority" class="col-form-label" >Priority :</label>                       
						</div>
						<div class="col-sm-3">
						  <select class="form-select form-control" id="inputGroupSelect01" name="new_task_priority">
						  ~;
if ($task_priority eq "Low") {
	print "<option selected value='Low'>Low</option>";
	print "<option value='Medium'>Medium</option>";
	print "<option value='High'>High</option>";
	print "<option value='Critical'>Critical</option>"
}
elsif ($task_priority eq "Medium") {
	print "<option value='Low'>Low</option>";
	print "<option selected value='Medium'>Medium</option>";
	print "<option value='High'>High</option>";
	print "<option value='Critical'>Critical</option>"
}

elsif ($task_priority eq "High") {
	print "<option value='Low'>Low</option>";
	print "<option value='Medium'>Medium</option>";
	print "<option selected value='High'>High</option>";
	print "<option value='Critical'>Critical</option>"
}

else {
	print "<option value='Low'>Low</option>";
	print "<option value='Medium'>Medium</option>";
	print "<option value='High'>High</option>";
	print "<option selected value='Critical'>Critical</option>"
}
print qq~
						</select>
						</div>
					</div>

					<div class="row" style="margin-top:45px">
						<div class="col-sm-2">
							<label for="Tags" class="col-form-label" >Tag :</label>                       
						</div>
						<div class="col-sm-3">
						  <select class="form-select form-control" id="inputGroupSelect01" name="new_task_tags">
~;
if ($task_tag eq "Testing") {
	print "<option selected value='Testing'>Testing</option>";
	print "<option value='UI'>UI</option>";
	print "<option value='Core'>Core</option>";
}
elsif ($task_type eq "UI") {
	print "<option value='Testing'>Testing</option>";
	print "<option selected value='UI'>UI</option>";
	print "<option value='Core'>Core</option>";
}
else {
	print "<option value='Testing'>Testing</option>";
	print "<option value='UI'>UI</option>";
	print "<option selected value='Core'>Core</option>";
}
print qq~
						</select>
						</div>
					</div>
				</div>
			</div>
		
			<input type="hidden" name="row" class="btn btn-primary" value="$task_id">
			<input class="btn btn-primary" type="submit" value="Save" style="float: left;margin-right: 15px;"></a>
		</form>
		
		<div style="margin-bottom:150px; margin-top:50px;">
			<a class="btn btn-primary" href="task_board_db.cgi" role="button" style="float: right;margin-right: 15px;">Exit</a>
			  
			<form action="delete_task.cgi">
				<input type="hidden" name="row" class="btn btn-primary" value="$task_id">
				<input class="btn btn-primary" type="submit" value="Delete" style="float: left;margin-right: 15px;"></a>
			</form>
		</div>  

            

~;
}

print "</body></html>";

   

$dbh->disconnect;