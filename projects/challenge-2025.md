# 挑战题

## 要求

1. 3月10日之前提交，并通知助教查看
2. 使用Markdown编写你的作业，并提交到自己的Github仓库中
3. 使用标准的参考文献格式（包括网页、论文、书籍等，参考文献不计入字数）；鼓励使用大模型辅助，但要确认其知识的正确性，并明确说明哪些工作是大模型辅助的。
4. 题目一必做，题目二和题目三任选一题。

> Markdown参考：[Markdown中文文档](https://markdown-zh.readthedocs.io/en/latest/)

## 题目一

思考并解释关系数据库中“关系”一词的含义。（不超过100字）

## 题目二

调研2023年之后最先进的Text2SQL技术（类似小的文献综述，不超过500字），并总结其异同之处。

## 题目三

考虑下面的题目，

```
考虑create table classroom
 (building  varchar(15),
  room_number  varchar(7),
  capacity  numeric(4,0),
  primary key (building, room_number)
 );找出容量最大的教室房间号
```

其答案是

```sql
SELECT room_number
FROM classroom
WHERE capacity = (SELECT MAX(capacity) FROM classroom);
```

请使用任意编程语言通过API分别调用DeepSeek V3和R1让大模型回答上面的题目。
