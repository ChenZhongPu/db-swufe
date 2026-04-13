---
title: Quiz（第七周）

author: CHEN Zhongpu

date: 2026-04

CJKmainfont: LXGW WenKai
---

## 1. 测试并解释下面的查询结果

### 第一组

```sql
WITH vals (v) as (VALUES (1), (NULL), (3), (4), (3), (2))
SELECT SUM(v) FROM vals;
```

### 第二组

```sql
WITH vals (v) as (VALUES (1), (NULL), (3), (4), (3), (2))
SELECT COUNT(v) FROM vals;

WITH vals (v) as (VALUES (1), (NULL), (3), (4), (3), (2))
SELECT COUNT(DISTINCT v) FROM vals;
```

### 第三组

```sql
WITH vals (v) as (VALUES (1), (NULL), (3), (4), (3), (2))
SELECT COUNT(*) FROM vals;
```

### 第四组

```
WITH vals (v) as (VALUES (1), (NULL), (3), (4), (3), (2))
SELECT COUNT(1) FROM vals;
```

## 2. 在 `instructor` 分别统计 `Comp. Sci.` 和 `Finance` 的平均工资

```sql
SELECT dept_name, ROUND(AVG(salary), 2)
FROM instructor
WHERE dept_name = 'Comp. Sci.' OR dept_name = 'Finance'
GROUP BY dept_name;

SELECT AVG(salary) FILTER ( WHERE dept_name = 'Comp. Sci.'),
       AVG(salary) FILTER ( WHERE dept_name = 'Finance' )
FROM instructor;
```

---

聚集表达式（Aggregate Expression）的详细使用参考：<https://www.postgresql.org/docs/current/sql-expressions.html#SYNTAX-AGGREGATES>
