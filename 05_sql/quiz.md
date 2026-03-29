# Quiz （第五周）

(1) SQL支持集合的并（`UNION`）、交（`INTERSECT`）和差（`EXCEPT`）。但是早期MySQL并不支持`INTERSECT`：

> The INTERSECT operator is a standard SQL feature and is natively supported in MySQL 8.0.31 and later versions.

在 SQL 中，`IN` 允许在 WHERE 子句中规定多个可能的值：

```sql
SELECT 1 in (1, 2, 3);
```

查阅资料，使用`IN`使用下面`INTERSECT`的功能（不考虑性能）：

```sql
(SELECT course_id
FROM section
WHERE semester = 'Fall' AND year = 2017)
INTERSECT
(SELECT course_id
FROM section
WHERE semester = 'Spring' AND year = 2018);
```

---

(2) 根据PPT中关于`CASE`的用法，考虑关系模式 `users(id, name, gender)`，其中`id`是身份证，`gender`是`M`或`F`。检索所有四川人的名字及其性别（其中性别使用汉字输出）。

```sql
CASE
  WHEN condition1 THEN result1
  WHEN condition2 THEN result2
  WHEN conditionN THEN resultN
  ELSE result
END;
```

---

（3）下面是PG/DuckDB支持的语法，查阅其含义：

```sql
SELECT '3408221992' ~ '^34(\d){8}$';
```
