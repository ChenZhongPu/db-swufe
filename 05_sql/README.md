本周学习了SQL中对空值的处理，聚集函数的使用。

# 本周作业（第4次作业）
本周作业**需要**使用Postgresql及DataGrip软件操作；不需要操作截图。

## 题目一（1分+2分）
1. 请问`count(DISTINCT *)`是否合法？用实验验证你的想法。

2. 请问下面的SQL语句是否合法？用实验验证你的想法。你从实验结果能得到什么结论？

```sql
SELECT dept_name, min(salary)
FROM instructor
GROUP BY dept_name
HAVING name LIKE '%at%';
```

## 题目二（2分）
请问`=some`和`in`有什么关系？请用实验验证。

## 题目三（2分+3分）
1. 找到平均工资最高的系的名字。
2. 用**两种方法**分别找到工资最高的员工的名字（可能不唯一）。