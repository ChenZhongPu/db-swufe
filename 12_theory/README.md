# 测试

> 翻译自[CMU DB 2025](https://15445.courses.cs.cmu.edu/spring2025/files/hw2-clean.pdf).

考虑一个数据库有单个关系`E(play_id, games_played, room_id, total_points)`，其中`play_id`是主码，所有属性均是固定宽度。假设`E`有20,000个元组，并存储在100个pages中。忽略关系的其他额外存储空间，如*page header*和*tuple header*，并有如下假设：

- DMBS没有任何meta-data。
- `E`没有任何索引。
- `E`没有任何页面在内存，并且DBMS能够在内存中存储无限数量的pages。
- `E`中元组的顺序是随机的（即堆存储）。

## Q1

```sql
SELECT MAX(total_points) FROM E
    WHERE games_played < 445 AND room_id == 15645 ;
```

假设DBMS采用的是行式存储（row-oriented）。为了回答上述查询，DBMS需要从磁盘读取pages的数量是？（选择最合适的答案）

- A. 1-40
- B. 41-60
- C. 61-80
- D. 81-100
- E. $\geq$ 101
- F. 无法确定

## Q2

```sql
SELECT total_points, games_played, room_id FROM E
  WHERE player_id = 445 OR player_id = 645 OR player_id = 799
```

假设DBMS采用的行式存储，为了回答上述查询，DBMS最少需要从磁盘读取pages的数量是？

- A. 1
- B. 2-3
- C. 4-6
- D. 7-9
- E. 10-100

## Q3

基于Q2的背景，DBMS最多需要从磁盘读取pages的数量是？

- A. 1
- B. 2-3
- C. 4-6
- D. 7-9
- E. 10-100
