---
title: Structured Query Language
prev1_title: Database
prev2_title: Computer Engineering
date: 2020-05-30
description: Structured Query Language
_previous: https://ailever.github.io/education/2020/05/30/Computer-Engineering/
categories:
  - education
HL1: education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Computer_Engineering.png
author_staff_member: anonym
---

<!-- Top Block -->
<div align="center" class="top_btn_box">
  <button class="top_btn" type="button" onclick="location.href='https://www.w3schools.com/sql/sql_exercises.asp'">W3S Tutorial</button>
  <button class="top_btn" type="button" onclick="location.href='https://www.sololearn.com/learning/1060'">Solo-Learn Tutorial</button>
  <button class="top_btn" type="button" onclick="location.href='https://www.postgresql.org/download/'">Postgres Download</button>
  <button class="top_btn" type="button" onclick="location.href='https://sqldbm.com/Home/'">SQLDBM</button>
</div><br>
<!-- Top Block -->

## Common Syntax
### Table - SELECT
<!-- Content Block -->
<pre class="sql-code">
SELECT * FROM [table_name]
WHERE [condition]
GROUP BY [column]
HAVING [condition]
ORDER BY [column] ASC|DESC;
</pre>
<pre class="sql-code">
SELECT * FROM [table_name];
SELECT * FROM [table_name] ORDER BY [column];
SELECT [column1], [column2], ... FROM [table_name];
SELECT [column] FROM [table_name];
SELECT DISTINCT [column] FROM [table_name];
SELECT COUNT(DISTINCT [column]) FROM [table_name];
SELECT * FROM [column] WHERE [condition];
                              condition : [column][operator][value]
                              column = 'value'   /* equal */
                              column > 'value'   /* greater than */
                              column < 'value'   /* less than */
                              column >= 'value'  /* greater than or equal */
                              column <= 'value'  /* less than or equal */
                              column <> 'value'  /* not equal */
                              column != 'value'  /* not equal */
                              column BETWEEN 'value1' AND 'value2'        
                              column LIKE 'pattern'	
                              column IN ('value1', 'value2', ...)
                              column1 = 'value1' AND column2 = 'value2' AND ...
                              column1 = 'value1' OR column2 = 'value2' OR ...
                              NOT column = 'value'
                              IS NULL;
                              IS NOT NULL;
</pre>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
  
<br><br></div>
<!-- Content Block -->

### Table - CREATE
<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<pre class="sql-code">
CREATE TABLE [table_name] (
    [column1] [datatype],
    [column2] [datatype],
   ....
);
</pre>
<pre class="sql-code">
CREATE TABLE [new_table_name] AS
    SELECT [column1], [column2], ...
    FROM [existing_table_name]
    WHERE [condition];
</pre>
<br><br></div>
<!-- Content Block -->

### Table - DROP
<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<pre class="sql-code">
DROP TABLE [table_name];
</pre>
<br><br></div>
<!-- Content Block -->

### Table - ALTER
<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<pre class="sql-code">
ALTER TABLE [table_name]
ADD [column_name] [datatype];
</pre>
<br><br></div>
<!-- Content Block -->



### Table - INSERT
<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<pre class="sql-code">
INSERT INTO [table_name] ([column1], [column2], ...)
VALUES ( 'value1',  'value2', ...);
</pre>
<br><br></div>
<!-- Content Block -->


### Table - UPDATE
<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<pre class="sql-code">
UPDATE [table_name]
SET [column1] = 'value1', [column2]= 'value2', ...
WHERE [condition];
</pre>
<br><br></div>
<!-- Content Block -->

### Table - DELETE
<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;"> 
<pre class="sql-code">
DELETE FROM [table_name]
WHERE [condition];
</pre>
<br><br></div>
<!-- Content Block -->

### Database - CREATE
<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<pre class="sql-code">
CREATE DATABASE [databasename];
</pre>  
<br><br></div>
<!-- Content Block -->

### Database - BACKUP
<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<pre class="sql-code">
BACKUP DATABASE [databasename]
TO DISK = 'filepath';
</pre>  
<br><br></div>
<!-- Content Block -->

### Database - DROP
<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<pre class="sql-code">
DROP DATABASE [databasename];
</pre>    
<br><br></div>
<!-- Content Block -->

### --
<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<pre class="sql-code">

</pre>    
<br><br></div>
<!-- Content Block -->



<br><br><br>
## Database Management System
### Data Quality
Data Integrity
- Entity Integrity
- Referential Integrity : Bijection
- Domain Integrity

### Navigational DBMS
### Relational DBMS
#### Postgre
<!-- Content Block -->
<div align="left" style="font-size:large;font-weight:bold;color:black;background-color:unset;">Server On/Off</div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<code class="code-title">Windows</code>
<pre class="shell-code">
pg_ctl -D "C:\Program Files\PostgreSQL\[version]\data" [start|stop|restart]  
</pre>
<code class="code-title">Linux</code> : <code class="code-path">/etc/postgresql/[version]/main/postgresql.conf</code>
<pre class="shell-code">
$ sudo service [start|stop|restart] postgresql  
</pre>
<code class="code-title">macOS</code>
<pre class="shell-code">
$ brew service [start|stop|restart] postgresql  
</pre>
<br><br></div>
<!-- Content Block -->

##### Access
<!-- Content Block -->
<div align="left" style="font-size:large;font-weight:bold;color:black;background-color:unset;">DB Access</div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<pre class="shell-code">
$ sudo -iu postgresql
$ psql
</pre>
<br><br></div>
<!-- Content Block -->

### Object-Oriented DBMS
### NoSQL and NewSQL DBMS





## Development Environment
### DBeaver
<code class="code-title">Shortcuts</code>
<pre class="code-path">
ctrl + enter
ctrl + shift + enter
</pre><br>


### pgAdmin4
<!-- Content Block -->
<div align="left" style="font-size:large;font-weight:bold;color:black;background-color:unset;">pgAdmin4 configuration</div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">  
<code class="code-title">Windows</code> : <code class="code-path">%CommonProgramFiles%\pgadmin\config_system.py</code><br>
<code class="code-title">Linux</code> : <code class="code-path">/etc/pgadmin/config_system.py</code><br>
<code class="code-title">macOS</code> : <code class="code-path">/Library/Preferences/pgadmin/config_system.py</code><br>
<br><br></div>
<!-- Content Block -->


<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<!-- Content Block -->

---

<!-- Reference Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='REF'>Reference</b>
<ol>
  <li>Postgre : https://tableplus.com/blog/2018/10/how-to-start-stop-restart-postgresql-server.html</li>
  <li>Postgre : https://www.pgadmin.org/download/pgadmin-4-python/</li>
  <li></li>
</ol>
</div>
<!-- Reference Block -->

<!-- Article Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='ART'>Related Articles</b>
<ol>
  <li></li>
  <li></li>
  <li></li>
</ol>
</div>
<!-- Article Block -->

<!-- Bottom Block -->
<div align="center" class="bottom_btn_box">
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2020-05-30-_CE-db-en-sql.md" target="_blank" style="color:white">Edit</a></span>
</div>
<!-- Bottom Block -->

<!-- Notice
# Mathematical Expression
- outline : $  $
- inline  : $$  $$

# Default Div Tag
- align : left, right, center
- font-size : xx-small, x-small, small, medium, large, x-large, xx-large
- font-weight : normal, bold
- color : red, orange, yellow, green, cyan, blue, purple, pink, white, gray, brown
- background-color : red, orange, yellow, green, cyan, blue, purple, pink, white, gray, brown

# Html Ref
- color code : https://htmlcolorcodes.com/
- tags : https://www.w3schools.com/tags/default.asp
- attributes : https://www.w3schools.com/tags/ref_attributes.asp
Notice -->


