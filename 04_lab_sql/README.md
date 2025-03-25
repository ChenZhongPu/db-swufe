本周通过Postgresql软件实践基本的SQL，并学习了集合操作等知识。

# 本周作业（第3次作业）

## 题目一（3分+1分）

> **需要**使用PostgreSQL/MySQL及DataGrip软件操作，并对操作页面及结果进行截图。

1. 新建一个`university`数据库，并执行`largeRelationsInsertFile.sql`，导入数据。
2. 运行第2次作业的题目三代码。注意：把原题目中的`会计`改成`History`。

## 题目二（3分）

（二选一）

### PostgreSQL

参考[Pattern Matching](https://www.postgresql.org/docs/17/functions-matching.html)，在PG中使用至少三种方法实现找到所有以`S`开头教师的名字。

### MySQL

参考[Pattern Matching](https://dev.mysql.com/doc/refman/8.4/en/pattern-matching.html)和[String Functions and Operators](https://dev.mysql.com/doc/refman/8.4/en/string-functions.html) ，在MySQL中使用至少三种方法实现找到所有以`S`开头教师的名字。

## 题目三（3分）

`psql`是PostgreSQL的命令行工具，请使用`psql`命令行工具 (`mysql`是MySQL的命令行工具，请使用`mysql`命令行工具)：

- 实现题目二
- 列出所有的数据库
- 列出当前数据库的所有表
- 显示某张表的关系模式

Hint: [psql](https://www.postgresql.org/docs/current/app-psql.html), [mysql shell](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-commands.html)
