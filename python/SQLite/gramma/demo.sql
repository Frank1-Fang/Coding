-- 初始化设置
.mode column
.header on

-- 删除旧表（防止重复执行出错）
.print ✅ 初始化数据库结构并清空旧表
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;

-- 创建学生表
.print ✅ 创建表：students（学生表）
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  gender TEXT CHECK (gender IN ('M', 'F')),
  birth_year INTEGER
);

-- 创建课程表
.print ✅ 创建表：courses（课程表）
CREATE TABLE courses (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  credit INTEGER DEFAULT 3
);

-- 创建成绩表（关联两张表）
.print ✅ 创建表：grades（成绩表，含外键）
CREATE TABLE grades (
  id INTEGER PRIMARY KEY,
  student_id INTEGER,
  course_id INTEGER,
  score INTEGER CHECK(score BETWEEN 0 AND 100),
  FOREIGN KEY(student_id) REFERENCES students(id),
  FOREIGN KEY(course_id) REFERENCES courses(id)
);

-- 插入数据
.print ✅ 插入数据：学生表
INSERT INTO students (name, gender, birth_year) VALUES
('Alice', 'F', 2005),
('Bob', 'M', 2004),
('Charlie', 'M', 2005),
('Daisy', 'F', 2003);

.print ✅ 插入数据：课程表
INSERT INTO courses (title, credit) VALUES
('Math', 4),
('English', 3),
('Physics', 2);

.print ✅ 插入数据：成绩表
INSERT INTO grades (student_id, course_id, score) VALUES
(1, 1, 90),
(1, 2, 88),
(2, 1, 75),
(3, 3, 80),
(4, 2, 92);

-- 基本查询
.print 🔍 查询：students 表中所有学生
SELECT * FROM students;

.print 🔍 查询：所有女生的姓名与出生年份
SELECT name, birth_year FROM students WHERE gender = 'F';

-- AND / OR 子句
.print 🔍 查询：出生在 2003~2004 年的女生
SELECT name FROM students WHERE gender = 'F' AND birth_year BETWEEN 2003 AND 2004;

-- LIKE / IN / BETWEEN / GLOB
.print 🔍 查询：以 A 开头的学生（LIKE）
SELECT name FROM students WHERE name LIKE 'A%';

.print 🔍 查询：出生于 2003 或 2005 年的学生（IN 子句）
SELECT name FROM students WHERE birth_year IN (2003, 2005);

.print 🔍 查询：以 A~C 开头的学生（GLOB）
SELECT name FROM students WHERE name GLOB '[A-C]*';

-- ORDER BY / DISTINCT
.print 🔍 查询：所有不重复出生年份（DISTINCT）并按年份降序
SELECT DISTINCT birth_year FROM students ORDER BY birth_year DESC;

-- JOIN 查询
.print 🔍 查询：三表 JOIN，显示学生-课程-成绩
SELECT s.name, c.title, g.score
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN courses c ON g.course_id = c.id
ORDER BY s.name;

-- GROUP BY / HAVING
.print 🔍 查询：统计平均分 > 80 的学生 ID 和平均分
SELECT student_id, AVG(score) AS avg_score
FROM grades
GROUP BY student_id
HAVING avg_score > 80;

-- 更新数据
.print 🔧 更新成绩：将 Bob 的数学成绩更新为 85
UPDATE grades SET score = 85 WHERE student_id = 2 AND course_id = 1;

.print 📊 验证更新后成绩（查 Bob 的所有成绩）
SELECT s.name, c.title, g.score
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN courses c ON g.course_id = c.id
WHERE s.name = 'Bob';

-- 删除数据
.print ❌ 删除：删除所有分数小于 60 的记录
DELETE FROM grades WHERE score < 60;

.print 📊 验证删除后 grades 表内容
SELECT * FROM grades;

-- ALTER 添加列
.print 🔧 添加列：向 students 表中添加 phone 字段
ALTER TABLE students ADD COLUMN phone TEXT;

.print 📊 展示 students 表结构（确认有 phone 字段）
PRAGMA table_info(students);

-- 索引
.print ⚙️ 创建索引：按成绩字段加速查询
CREATE INDEX idx_score ON grades(score);

.print 📊 查看已有索引
PRAGMA index_list(grades);

.print ⚙️ 创建唯一索引：保证课程标题不重复
CREATE UNIQUE INDEX idx_course_title ON courses(title);

.print 📊 查看 courses 表中的唯一索引
PRAGMA index_list(courses);

DROP VIEW IF EXISTS high_scores;

-- 视图
.print 👁 创建视图：high_scores（显示高分记录）
CREATE VIEW high_scores AS
SELECT s.name, c.title, g.score
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN courses c ON g.course_id = c.id
WHERE g.score >= 90;

.print 📊 查看视图 high_scores 中的记录
SELECT * FROM high_scores;

-- 触发器：自动删除该学生的成绩
.print ⛓ 创建触发器：当删除学生时，自动删除其成绩
CREATE TRIGGER delete_grades_after_student
AFTER DELETE ON students
FOR EACH ROW
BEGIN
  DELETE FROM grades WHERE student_id = OLD.id;
END;

.print 🧪 测试触发器：删除 Charlie 学生
DELETE FROM students WHERE name = 'Charlie';

.print 📊 确认 Charlie 是否从 students 表被删除
SELECT * FROM students;

.print 📊 确认 Charlie 的成绩是否也被删除
SELECT * FROM grades WHERE student_id = 3;


-- 事务示例
.print 🧪 事务测试：插入学生 Eva，但回滚（不保留）
BEGIN;
INSERT INTO students (name, gender, birth_year) VALUES ('Eva', 'F', 2006);
ROLLBACK;  -- 不提交
-- Eva 不会被插入

.print 📊 验证是否成功插入 Eva（应无记录）
SELECT * FROM students WHERE name = 'Eva';

.print ✅ 事务提交：插入学生 Frank，并提交
BEGIN;
INSERT INTO students (name, gender, birth_year) VALUES ('Frank', 'M', 2005);
COMMIT;  -- 提交成功

.print 📊 验证是否成功插入 Frank
SELECT * FROM students WHERE name = 'Frank';

-- PRAGMA 查看表结构
.print 🧾 查看 students 表结构（PRAGMA）
PRAGMA table_info(students);

-- ANALYZE 优化
.print 📊 执行 ANALYZE（生成优化统计信息）
ANALYZE;

-- VACUUM 压缩数据库
.print 🧹 执行 VACUUM（压缩数据库文件）
VACUUM;
