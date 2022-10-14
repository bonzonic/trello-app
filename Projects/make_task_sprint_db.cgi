#!c:/Strawberry/perl/bin/perl.exe

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
   on_connect_do => 'PRAGMA foreign_keys = ON'
});
 
# ...
my $stmt = qq(DROP TABLE IF EXISTS member);
my $rv = $dbh->do($stmt);
my $stmt = qq(DROP TABLE IF EXISTS sprints);
my $rv = $dbh->do($stmt);
my $stmt = qq(DROP TABLE IF EXISTS tasks);
my $rv = $dbh->do($stmt);
my $stmt = qq(DROP TABLE IF EXISTS task_member);
my $rv = $dbh->do($stmt);
# autoincrement allows the code to increment it by 1 everytime it gets called
my $sql = <<'END_SQL';
CREATE TABLE member (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
  );

END_SQL

$dbh->do($sql);

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
  
  task_id          INTEGER PRIMARY KEY AUTOINCREMENT,
  task_name        VARCHAR(100),
  story_points     INTEGER,
  descrip          VARCHAR(150),
  deadline_date    VARCHAR(100),
  task_type        VARCHAR(100),
  task_tags        VARCHAR(100),
  task_priority    VARCHAR(100),
  members          ENUM(100),
  priority_id      INTEGER,
  priority_hex     VARCHAR(100),
  assigned_to_sprint INTEGER
)

END_SQL

$dbh->do($sql);

my $sql = <<'END_SQL';
CREATE TABLE task_member (
    task_id INTEGER NOT NULL,
    date DATETIME NOT NULL,
    hour NUMBER(8) NOT NULL,
    PRIMARY KEY(task_id, date),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id) 
    ON DELETE CASCADE
  );

END_SQL

$dbh->do($sql);
 
$dbh->disconnect;

print "Content-type: text/html \n\n";

print "<html>";
print "<body>";

print "</body></html>";
