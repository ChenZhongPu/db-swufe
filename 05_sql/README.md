本周学习了SQL中对空值的处理，聚集函数的使用。

# 本周作业（第4次作业）

## 题目一（2分）

请问下面的SQL语句是否合法？用实验验证你的想法。你从实验结果能得到什么结论？

```sql
SELECT dept_name, min(salary)
FROM instructor;

SELECT dept_name, min(salary)
FROM instructor
GROUP BY dept_name
HAVING name LIKE '%at%';

SELECT dept_name
FROM instructor
WHERE AVG(salary) > 20000;
```

## 题目二（3分+3分+2分）

1. 找到工资最高员工的名字，假设工资最高的员工只有一位（至少两种写法）。

2. 找到工资最高员工的名字，假设工资最高的员工有多位（试试多种写法）。

3. 解释下面四句。

```sql
SELECT 1 IN (1);

SELECT 1 = (1);

SELECT (1, 2) = (1, 2);

SELECT (1) IN (1, 2);
```

---

## Some Links

- [Why doesn't COUNT(DISTINCT (\*)) work?](https://stackoverflow.com/questions/5010470/why-doesnt-countdistinct-work)
- [Python: any()](https://realpython.com/any-python/)
- [Python: all()](https://realpython.com/python-all/)

---

## 聚合函数扩展

```sql
SELECT dept_name, min(salary)
FROM instructor;
```

> SELECT 中未被聚合函数包裹的列，必须出现在 GROUP BY 子句中。

| 数据库     | 默认行为                                |
| ---------- | --------------------------------------- |
| PostgreSQL | 严格遵守标准，支持函数依赖              |
| MySQL 5.7+ | 默认开启 `ONLY_FULL_GROUP_BY`，严格模式 |
| SQLite     | 宽松，允许未分组列（取任意值）          |
| SQL Server | 严格遵守标准                            |
| Oracle     | 严格遵守标准                            |

```
❯ sqlite3 mydb.db < DDL.sql
❯ sqlite3 mydb.db < smallRelationsInsertFile.sql
❯ sqlite3 mydb.db
SQLite version 3.51.0 2025-06-12 13:14:41
Enter ".help" for usage hints.
sqlite> SELECT MIN(salary) FROM instructor;
40000
sqlite> SELECT name, MIN(salary) FROM instructor;
Mozart|40000
```
