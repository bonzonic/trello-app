#!C:\Strawberry\perl\bin\perl.exe

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
  -src   => 'css/bootstrap.css',
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


print "<body>";

print qq~

<head>
	<title>Sprint board</title>
	<LINK REL="STYLESHEET" TYPE="text/css" HREF="css/bootstrap.css" HREF="css/bootstrap-grid.css HREF="css/bootstrap.min.css HREF="css/bootstrap-grid.min.css HREF="css/bootstrap-reboot.css HREF="css/bootstrap-reboot.min.css" MEDIA="screen">\n
	<!-- Styling for the layout of the page and cards-->
	<style>
		#main{
			margin: 50px;
		}
		.card{
			margin-top: 50px; 
			margin-left: 150px;
			margin-right: 200px;
			border-radius: 20px;
		}
		.card-header{
			font-weight:bold;
			text-align: center;
		}

	</style>
</head>
<!-- Setting the board colour-->
<body style="background-color:#DCEBFF;">
	<div id="main">
		<!-- Adding buttons in the same row -->
		<div class="form-row">
			<!-- Button to add sprint -->
			<div class="form-group col-md-4" >
				<a href = "add_sprint.html" class="btn btn-outline-dark" button style ="background-color:#FEFCFF"href="#" role="button">+</a>
			</div>

			<div class="form-group col-md-4">
				<!-- space -->
			</div>

			<!-- Button to view the members in the sprint-->
			<div class="form-group col-md-2">
				<a class="btn btn-primary" href="../member_board/team_board.pl" role="button" style="float: right;"> View Team</a>
			</div>

			<!-- Button to view the task in the sprint-->
			<div class="form-group col-md-2">
				<a href= "../task_board/task_board_db.cgi" class="btn btn-primary" href="#" role="button"> View Tasks</a>
			</div>

		</div>
	</div>

<div>

~;

my $sql = 'SELECT * FROM sprints';
   
my $sth = $dbh->prepare($sql);

 
$sth->execute();

while (my $row = $sth->fetchrow_hashref) {
	
	if($row->{get_started_bool} == 0){

		print qq~

		<form action = "view_sprint_db.cgi">
			<!-- Creating a card for each sprint-->
			<div class="card">
				<div class="card-header">
					<h5>$row->{sprint_name}</h5>
				</div>
				<div class="card-body">
					<div class="row" style="font-weight: bold;">
						<!-- Display the start date label -->
						<div class="col-sm-2">
							<label for="startDate" class="col-form-label" >Start Date :</label>                       
						</div>
							
						<div class="col-sm-3">
							<div type="date" class="form-control" id="startDate" style="text-align: center;" readonly>
								<h5>$row->{start_date}</h5>
							</div>
						</div>

						<!-- Display the end date label -->
						<div class="col-sm-2" >
							<label for="endDate" class="col-form-label" >End Date :</label>                       
						</div>
							
						<div class="col-sm-3" >
							<div type="date" class="form-control" id="endDate" style="text-align: center; " readonly>
								<h5>$row->{end_date}</h5>
							</div>
						</div>
						<!-- Button to start the sprint-->
						<div style="margin-left:30px"> 
							<input type="hidden" name="row" value="$row->{sprint_id}">
							<input type = "submit" class="btn btn-outline-danger" value = "Get Started" style="float:right;">
						</div>
					</div>
				</div>
			  </div>
		</form>
  

~;

}elsif($row->{get_started_bool} == 1){
	
	print qq~

		<form action = "view_sprint_db_2.cgi">
			<!-- Creating a card for each sprint-->
			<div class="card">
				<div class="card-header">
					<h5>$row->{sprint_name}</h5>
				</div>
				<div class="card-body">
					<div class="row" style="font-weight: bold;">
						<!-- Display the start date label -->
						<div class="col-sm-2">
							<label for="startDate" class="col-form-label" >Start Date :</label>                       
						</div>
							
						<div class="col-sm-3">
							<div type="date" class="form-control" id="startDate" style="text-align: center;" readonly>
								<h5>$row->{start_date}</h5>
							</div>
						</div>

						<!-- Display the end date label -->
						<div class="col-sm-2" >
							<label for="endDate" class="col-form-label" >End Date :</label>                       
						</div>
							
						<div class="col-sm-3" >
							<div type="date" class="form-control" id="endDate" style="text-align: center; " readonly>
								<h5>$row->{end_date}</h5>
							</div>
						</div>
						<!-- Button to start the sprint-->
						<div style="margin-left:30px"> 
							<input type="hidden" name="row" value="$row->{sprint_id}">
							<input type = "submit" class="btn btn-outline-danger" value = "In Progress" style="float:right;">
						</div>
					</div>
				</div>
			  </div>
		</form>
  

~;
	

}

}



$dbh->disconnect();


print "</body></html>";
