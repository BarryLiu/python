-- sqlite3 tmp/03.db < schema.sql   创建数据库

drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);