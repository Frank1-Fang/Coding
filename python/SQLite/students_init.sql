.mode column
.header on

DROP TABLE IF EXISTS students;

CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT,
  grade INTEGER
);

INSERT INTO students (name, grade) VALUES ('Alice', 85);
INSERT INTO students (name, grade) VALUES ('Bob', 90);
INSERT INTO students (name, grade) VALUES ('Charlie', 78);

.print '第一次查询结果：';
SELECT * FROM students;

UPDATE students SET grade = 82 WHERE name = 'Charlie';

.print '第二次查询结果：';
SELECT * FROM students;

DELETE FROM students WHERE name = 'Bob';

.print '第三次查询结果：';
SELECT * FROM students;
