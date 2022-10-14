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

print "<body>";

print qq~

<head>
  <LINK REL="STYLESHEET" TYPE="text/css" HREF="css/bootstrap.css" HREF="css/bootstrap-grid.css HREF="css/bootstrap.min.css HREF="css/bootstrap-grid.min.css HREF="css/bootstrap-reboot.css HREF="css/bootstrap-reboot.min.css" MEDIA="screen">\n
<style>
form{
    font-family: Helvetica, Arial, sans-serif;

}
#main{
    margin:80px;font-weight:bold;

}
#newTask{
    font-weight:bold ;margin-bottom: 30px;
}

#just-line-break {
    white-space: pre-line;
}
  
  #line-break-and-tab {
    white-space: pre-wrap;
}
</style>
</head>
<body>

    </div>

    <div id="just-line-break"></div>

    <br/>

    </div>

    <div id="just-line-break"></div>

    <br/>

    <div class="container text-center">
        <div class="row">
          <div class="col">
          </div>
          <div class="col">
          </div>
        </div>
        <div class="row">
          <div class="col">
          </div>
          <div class="col">
            <p style="font-size:50px">FILTER</p>

            <div id="just-line-break"></div>

            <br/>
    
            <div id="line-break-and-tab"></div>

            <p style="font-size:30px">TASKS</p>
          </div>
          <div class="col">
          </div>
        </div>

        <div id="just-line-break"></div>

        <br/>

        <div id="line-break-and-tab"></div>

        <div id="just-line-break"></div>

        <br/>

        <div id="line-break-and-tab"></div>

        <div class="row">
                <div id="just-line-break"></div>

                <br/>
        
                <div id="line-break-and-tab"></div>
                <form action="task_board_db.cgi">
                    <div class="d-grid gap-2">
                      <input type="hidden" name="row" class="btn btn-primary" value="Priority">
                      <input class="btn btn-outline-dark" type="submit" value="Priority" style ="background-color:#E5E4E2"></a>
                    </div>
                </form>
                <div id="just-line-break"></div>

                <br/>
        
                <div id="line-break-and-tab"></div>

                <form action="task_board_db.cgi">
                  <div class="d-grid gap-2">
                    <input type="hidden" name="row" class="btn btn-primary" value="UI">
                    <input class="btn btn-outline-dark" type="submit" value="UI" style ="background-color:#E5E4E2"></a>
                  </div>
               </form>

                <div id="just-line-break"></div>

                <br/>
        
                <div id="line-break-and-tab"></div>

                <form action="task_board_db.cgi">
                  <div class="d-grid gap-2">
                    <input type="hidden" name="row" class="btn btn-primary" value="Testing">
                    <input class="btn btn-outline-dark" type="submit" value="Testing" style ="background-color:#E5E4E2"></a>
                  </div>
               </form>

                <div id="just-line-break"></div>

                <br/>
        
                <div id="line-break-and-tab"></div>

                <form action="task_board_db.cgi">
                  <div class="d-grid gap-2">
                    <input type="hidden" name="row" class="btn btn-primary" value="Core">
                    <input class="btn btn-outline-dark" type="submit" value="Core" style ="background-color:#E5E4E2"></a>
                  </div>
              </form>
          </div>
      </div>

      <div id="just-line-break"></div>

      <br/>

      <div id="line-break-and-tab"></div>

      <div id="just-line-break"></div>

      <br/>

      <div id="line-break-and-tab"></div>

      <div style="margin-top:100px">
        <form action="task_board_db.cgi">
			<input type="hidden" name="row" class="btn btn-primary" value="">
			<input class="btn btn-primary" type="submit" value="Cancel" style ="float: right; margin-right: 15px;"></a>
        </form>
    </div>

</body>
        

~;


print "</body></html>";




