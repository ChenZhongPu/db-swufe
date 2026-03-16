---
title: SQL练习（1）

author: CHEN Zhongpu

date: 2026-3

CJKmainfont: LXGW WenKai
---

> SQL是混乱的！使用具体的DBMS之前一定要查文档。

1. DuckDB中如果`DECIMAL`不提供任何宽度、精度信息，默认是如何？

2. 在DuckDB中，为什么下面的代码是不报错？

```sql
CREATE TABLE test_info(
    info VARCHAR(3)
);

INSERT INTO test_info VALUES ('abcd');
```
