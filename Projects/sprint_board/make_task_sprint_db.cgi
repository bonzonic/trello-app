#!C:\Strawberry\perl\bin\perl.exe

use strict;
use warnings;
 
use DBI;
 
my $dbfile = "backlog.db";
 
my $dsn      = "dbi:SQLite:dbname=$dbfile";
my $user     = "";
my $password = "";
my $dbh = DBI->connect($dsn, $user, $password, {
   PrintError       => 0,
   RaiseError       => 1,
   AutoCommit       => 1,
   FetchHashKeyName => 'NAME_lc',
});
 
# ...
 
 
my $sql = <<'END_SQL';
CREATE TABLE sprints (
  
  
  sprint_id        INTEGER,
  sprint_name	   VARCHAR(100),
  start_date       VARCHAR(100),
  end_date         VARCHAR(100),
  task_id_list     VARCHAR(100),
  get_started_bool INTEGER
)

END_SQL

$dbh->do($sql);



my $sql = <<'END_SQL';
CREATE TABLE tasks (
  
  task_id          INTEGER,
  task_name        VARCHAR(100),
  story_points     INTEGER,
  descrip          VARCHAR(150),
  deadline_date    VARCHAR(100),
  task_type        ENUM(100),
  task_tags        ENUM(100),
  task_priority    ENUM(100),
  members          ENUM(100),
  priority_id      INTEGER,
  priority_hex     VARCHAR(100)
)

END_SQL

$dbh->do($sql);
 
 
$dbh->disconnect;

print "Content-type: text/html \n\n";

print "<html>";
print "<body>";

print "</body></html>";
