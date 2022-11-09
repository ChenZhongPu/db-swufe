# 本周作业（第6次作业）

## 题目一（4分+2分）
1. 使用join得到每个学院的名字（dept_name）及每个学院的老师总数。注意，即使一个学院即使暂时没有老师，也应该输出总数为0。

2. 创建一个视图`physics_fall_2018`，表示在2018年秋季学期由物理学院（physics）开设的课程号、课程段号以及每个课程段对应的教学楼（building）和教室号（room_number）。

## 题目二（4分）
下面的SQL用于列出2018年春季学期的所有课程段，以及讲授这些课程段的教师的名字和ID。如果某一课程段尚无教师，将对应教师的名字设为"-"。

```sql
SELECT course_id, sec_id, ID,
    coalesce(name, '-') as name
FROM [1]
    NATURAL LEFT OUTER JOIN instructor
WHERE [2]
```
请分别补全[1]和[2]。

（提示：`coalesce(name, '-')`的作用是，当name为空时返回'-'，否则返回name本身。）