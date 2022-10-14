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

my $filter_task = param ('row');


print "Content-type: text/html \n\n";

print "<html>";


print "<body>";


print qq~

<head>
<!-- Integrating the chosen CSS style with the HTML file -->
	<LINK REL="STYLESHEET" TYPE="text/css" HREF="css/bootstrap.css" HREF="css/bootstrap-grid.css HREF="css/bootstrap.min.css HREF="css/bootstrap-grid.min.css HREF="css/bootstrap-reboot.css HREF="css/bootstrap-reboot.min.css" MEDIA="screen">\n
    <style>
        #div1 {
            width:33.33%;
            float: left;
            margin-left:10px
        }

        #div2 {
            width:33.33%;
            margin: 0 auto;
        }

        #div3 {
            width:20%;
            float: right;
        }
        #div4{
            text-align:center;
            border-radius:10px;
            border: 1px solid;        
        }
        #div5{
            border-radius:5px;
            border: 3px solid;
        }
		#container-fluid{
            display:flex;
            flex-wrap:wrap;
        }
    </style>
</head>

<body style="background-color:#E5E4E2;">
<!-- a placeholder for the '+' button and instruction string to create sprint/member/task -->
    <div id="div1">
        <!-- href so task_board can link with task add page -->
        <a href="task_add.html"><button style ="background-color:#FEFCFF" type ="button" class="btn btn-outline-dark">+</button></a>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
        </svg>
        <i>Click this button to add new sprint/member/task</i>
    </div>
    <!-- a placeholder for the Filter, View Sprint and View Team buttons -->
    <div class="container-fluid">
        <div class="row justify-content-end my-3">
            <!-- a placeholder for the Filter button that links to the filter page -->
            <div class="col-sm-auto">
                <a href="filter_task_db.cgi"><button style ="background-color:#FEFCFF" type ="button" class="btn btn-outline-dark">Filter</button></a>
            </div>
            <!-- a placeholder for the View Sprint button that will link to the sprint page -->
            <div class="col-sm-auto">
                <a href = "../sprint_board/sprint_board_db.cgi"><button style ="background-color:#FEFCFF" type ="button" class="btn btn-outline-dark">View Sprint</button></a>
            </div>
            <!-- a placeholder for the View Team button that will link to the team page -->
            <div class="col-sm-auto">
                <a href="../member_board/team_board.pl" style ="background-color:#FEFCFF" type ="button" class="btn btn-outline-dark">View Team</a>
            </div>
        </div>
    </div>
	

</body>




~;


if ($filter_task eq "Priority"){
	
	my $sql = 'SELECT * FROM tasks ORDER BY priority_id ASC';
   
my $sth = $dbh->prepare($sql);

 
$sth->execute();


print qq~
    <div id="container-fluid">
        
~;


		
while (my $row = $sth->fetchrow_hashref) {		

print qq~		
	<form action="view_task.cgi">
        <!-- a placeholder for the task cards -->
        <div class="card" id="div5" style="width:20em;height:20em;margin: 50px 75px 75px 100px; border-radius:5px; border-color:$row->{priority_hex};">
            <div class="card-body">
                <div class="row" style="margin-bottom:15px;">
                    <div class="col"style="text-align:center;border-radius:15px;background-color:$row->{priority_hex};">
                        <h2>$row->{task_name}</h2>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6"style="font-weight:bold;">
                        <h5>Members:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{members}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Type:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{task_type}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Tag:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{task_tags}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:10px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Status:</h5>
                    </div>
                    <div id=div4 class="col" style="border-color:#39C000;background-color:#C2FFA9;">
                        <h5>Open</h5>
                    </div>
                </div>
				<input type="hidden" name="row" class="btn btn-primary" value="$row->{task_id}">
				<input type="submit" class="btn btn-primary btn-sm" style="float:right" value="View Details">	
			</div>
		</div>
    </form>

~;	

}
		  
print qq~	  
			
			
	</div>
			
~;	
}elsif($filter_task eq "UI"){
	
my $sql = 'SELECT * FROM tasks WHERE task_tags = "UI" ORDER BY priority_id ASC';
   
my $sth = $dbh->prepare($sql);

 
$sth->execute();


print qq~
    <div id="container-fluid">
        
~;


		
while (my $row = $sth->fetchrow_hashref) {		

print qq~		
	<form action="view_task.cgi">
        <!-- a placeholder for the task cards -->
        <div class="card" id="div5" style="width:20em;height:20em;margin: 50px 75px 75px 100px; border-radius:5px; border-color:$row->{priority_hex};">
            <div class="card-body">
                <div class="row" style="margin-bottom:15px;">
                    <div class="col"style="text-align:center;border-radius:15px;background-color:$row->{priority_hex};">
                        <h2>$row->{task_name}</h2>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6"style="font-weight:bold;">
                        <h5>Members:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{members}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Type:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{task_type}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Tag:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{task_tags}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:10px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Status:</h5>
                    </div>
                    <div id=div4 class="col" style="border-color:#39C000;background-color:#C2FFA9;">
                        <h5>Open</h5>
                    </div>
                </div>
				<input type="hidden" name="row" class="btn btn-primary" value="$row->{task_id}">
				<input type="submit" class="btn btn-primary btn-sm" style="float:right" value="View Details">	
			</div>
		</div>
    </form>

~;	

}
		  
print qq~	  
			
			
	</div>
			
~;	
}elsif($filter_task eq "Testing"){
	
	my $sql = 'SELECT * FROM tasks WHERE task_tags = "Testing" ORDER BY priority_id ASC';
   
my $sth = $dbh->prepare($sql);

 
$sth->execute();


print qq~
    <div id="container-fluid">
        
~;


		
while (my $row = $sth->fetchrow_hashref) {		

print qq~		
	<form action="view_task.cgi">
        <!-- a placeholder for the task cards -->
        <div class="card" id="div5" style="width:20em;height:20em;margin: 50px 75px 75px 100px; border-radius:5px; border-color:$row->{priority_hex};">
            <div class="card-body">
                <div class="row" style="margin-bottom:15px;">
                    <div class="col"style="text-align:center;border-radius:15px;background-color:$row->{priority_hex};">
                        <h2>$row->{task_name}</h2>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6"style="font-weight:bold;">
                        <h5>Members:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{members}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Type:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{task_type}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Tag:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{task_tags}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:10px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Status:</h5>
                    </div>
                    <div id=div4 class="col" style="border-color:#39C000;background-color:#C2FFA9;">
                        <h5>Open</h5>
                    </div>
                </div>
				<input type="hidden" name="row" class="btn btn-primary" value="$row->{task_id}">
				<input type="submit" class="btn btn-primary btn-sm" style="float:right" value="View Details">	
			</div>
		</div>
    </form>

~;	

}
		  
print qq~	  
			
			
	</div>
			
~;
}elsif($filter_task eq "Core"){
	
	my $sql = 'SELECT * FROM tasks WHERE task_tags = "Core" ORDER BY priority_id ASC';
   
my $sth = $dbh->prepare($sql);

 
$sth->execute();


print qq~
    <div id="container-fluid">
        
~;


		
while (my $row = $sth->fetchrow_hashref) {		

print qq~		
	<form action="view_task.cgi">
        <!-- a placeholder for the task cards -->
        <div class="card" id="div5" style="width:20em;height:20em;margin: 50px 75px 75px 100px; border-radius:5px; border-color:$row->{priority_hex};">
            <div class="card-body">
                <div class="row" style="margin-bottom:15px;">
                    <div class="col"style="text-align:center;border-radius:15px;background-color:$row->{priority_hex};">
                        <h2>$row->{task_name}</h2>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6"style="font-weight:bold;">
                        <h5>Members:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{members}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Type:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{task_type}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Tag:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{task_tags}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:10px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Status:</h5>
                    </div>
                    <div id=div4 class="col" style="border-color:#39C000;background-color:#C2FFA9;">
                        <h5>Open</h5>
                    </div>
                </div>
				<input type="hidden" name="row" class="btn btn-primary" value="$row->{task_id}">
				<input type="submit" class="btn btn-primary btn-sm" style="float:right" value="View Details">	
			</div>
		</div>
    </form>

~;	

}
		  
print qq~	  
			
			
	</div>
			
~;
}else{
	
my $sql = 'SELECT * FROM tasks ORDER BY priority_id ASC';
   
my $sth = $dbh->prepare($sql);

 
$sth->execute();


print qq~
    <div id="container-fluid">
        
~;


		
while (my $row = $sth->fetchrow_hashref) {		

print qq~		
	<form action="view_task.cgi">
        <!-- a placeholder for the task cards -->
        <div class="card" id="div5" style="width:20em;height:20em;margin: 50px 75px 75px 100px; border-radius:5px; border-color:$row->{priority_hex};">
            <div class="card-body">
                <div class="row" style="margin-bottom:15px;">
                    <div class="col"style="text-align:center;border-radius:15px;background-color:$row->{priority_hex};">
                        <h2>$row->{task_name}</h2>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6"style="font-weight:bold;">
                        <h5>Members:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{members}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Type:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{task_type}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:15px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Tag:</h5>
                    </div>
                    <div class="col" id="div4" style="border-color:#585858;background-color:#D8D8D8;">
                        <h5>$row->{task_tags}</h5>
                    </div>
                </div>
                <div class="row"style="margin-bottom:10px">
                    <div class="col-sm-6" style="font-weight:bold;">
                        <h5>Task Status:</h5>
                    </div>
                    <div id=div4 class="col" style="border-color:#39C000;background-color:#C2FFA9;">
                        <h5>Open</h5>
                    </div>
                </div>
				<input type="hidden" name="row" class="btn btn-primary" value="$row->{task_id}">
				<input type="submit" class="btn btn-primary btn-sm" style="float:right" value="View Details">	
			</div>
		</div>
    </form>

~;	

}
		  
print qq~	  
			
			
	</div>
			
~;
}
			

$dbh->disconnect();


print "</body></html>";



