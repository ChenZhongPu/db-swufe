本周学习了SQL中对空值的处理，聚集函数的使用。

# 本周作业（第4次作业）
不需要操作截图。

## 题目一（2分）
请问下面的SQL语句是否合法？用实验验证你的想法。你从实验结果能得到什么结论？

```sql
SELECT dept_name, min(salary)
FROM instructor
GROUP BY dept_name
HAVING name LIKE '%at%';
```

## 题目二（3分+3分+5分）
1. 找到课程总学分最高的系的名字。
2. 有人认为下面的查询结果总是0，你是否认同她的看法？为什么？

```sql
SELECT AVG(salary) - (SUM(salary) / COUNT(*))
FROM instructor;
```
3. 用**两种方法**分别找到工资最高的员工的名字（可能不唯一）。
