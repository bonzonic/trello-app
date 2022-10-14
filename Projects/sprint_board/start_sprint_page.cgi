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

my $sprint_name = param ('sprintName');
my $sprintStartDate = param('sprintStartDate');
my $sprintEndDate = param('sprintEndDate');

print "Content-type: text/html \n\n";

print "<html>";


print "<body>";

print qq~

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="styles.css">
  <script src="script.js" defer></script>
  <title>Start Sprint</title>
</head>
<body>

    <div id="just-line-break"></div>

    <br/>

    <div id="line-break-and-tab"></div>

    <div style="text-align:center; font-size:40px; font-family: Helvetica, Arial, sans-serif">
        <svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor" class="bi bi-ui-checks" viewBox="0 0 16 16">
            <path d="M7 2.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-7a.5.5 0 0 1-.5-.5v-1zM2 1a2 2 0 0 0-2 2v2a2 2 0 0 0 2 2h2a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H2zm0 8a2 2 0 0 0-2 2v2a2 2 0 0 0 2 2h2a2 2 0 0 0 2-2v-2a2 2 0 0 0-2-2H2zm.854-3.646a.5.5 0 0 1-.708 0l-1-1a.5.5 0 1 1 .708-.708l.646.647 1.646-1.647a.5.5 0 1 1 .708.708l-2 2zm0 8a.5.5 0 0 1-.708 0l-1-1a.5.5 0 0 1 .708-.708l.646.647 1.646-1.647a.5.5 0 0 1 .708.708l-2 2zM7 10.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-7a.5.5 0 0 1-.5-.5v-1zm0-5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5zm0 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z"/>
          </svg>
        START SPRINTING 
    </div>
    <br/>
    <div style="text-align:center; font-size:20px; font-family: Helvetica, Arial, sans-serif">
        Drag and drop tasks between Product Backlog and Sprint Backlog with ease !
    </div>

    <div id="just-line-break"></div>

      <br/>

      <div id="line-break-and-tab"></div>
      <div id="just-line-break"></div>

      <br/>

      <div id="line-break-and-tab"></div>
      <div id="just-line-break"></div>

      <br/>

      <div id="line-break-and-tab"></div>
      <div id="just-line-break"></div>

      <br/>

      <div id="line-break-and-tab"></div>

      <div style="font-size:20px; font-family: Helvetica, Arial, sans-serif">
        Product Backlog:
    </div>
  <div id="container-1" class="container">
~;

my $sql = 'SELECT task_id, task_name,  assigned_to_sprint FROM tasks';
   
my $sth = $dbh->prepare($sql);

 
$sth->execute();

while (my $row = $sth->fetchrow_hashref) {

  if ($row->{assigned_to_sprint} == 0) {
    print qq~
    <p class="draggable" draggable="true" id="$row->{task_id}">$row->{task_name}</p>
    ~;
  }
}
print qq~
    </div>
      <div id="just-line-break"></div>

      <br/>
    
      <div id="line-break-and-tab"></div>
      <div id="just-line-break"></div>
    
      <br/>
    
      <div id="line-break-and-tab"></div>
      <div id="just-line-break"></div>
    
      <br/>
    
      <div id="line-break-and-tab"></div>
      <div id="just-line-break"></div>
    
      <br/>
    
      <div id="line-break-and-tab"></div>

      <div style="font-size:20px; font-family: Helvetica, Arial, sans-serif">
        Sprint Backlog:
    </div>

    <div id="container-2" class="container">
      </div>

      <div style="margin-top:100px">
      <form action="start_sprint_save.cgi", method="get">
        <input type="hidden" name="sprintName" value="$sprint_name">
        <input type="hidden" name="sprintStartDate" value="$sprintStartDate">
        <input type="hidden" name="sprintEndDate" value="$sprintEndDate">
        <input id="save_sprint" type="hidden" name="value" value="">
        <input onClick="getElements()" style="text-align:center; font-size:17px; font-family: Helvetica, Arial, sans-serif; float: right; margin-right: 25px;" role="button" class="button" value="Save" type="submit">
      </form>
        <a href="add_sprint.html" style="text-align:center; font-size:17px; font-family: Helvetica, Arial, sans-serif; float: right; margin-right: 25px;" role="button" class="button">Back</a>
    </div>
    
</body>

~;


$dbh->disconnect();


print "</html>";
