---
title: 关系代数练习

author: CHEN Zhongpu

date: 2026-03

CJKmainfont: LXGW WenKai
---

（True/False）在主流关系代数中，关系实际上是bag。

---

关系 R(A, B) 和 S(B, C) 的内容分别如下：

| A   | B   |
| --- | --- |
| 1   | 2   |
| 1   | 2   |

| B   | C   |
| --- | --- |
| 2   | 3   |
| 4   | 5   |
| 4   | 5   |

那么，$R \Join_{R.B < S.B} S$ 的结果是？

---

(True/False) $\Pi_{L}(R \cup S) = \Pi_{L}(R) \cup \Pi_{L}(S)$，其中L是任意属性列表。

---

(填空) $\sigma_{C \land D}(R) = \sigma_{C}(R) \underline{\quad \text{请输入答案} \quad} \sigma_{D}(R)$

---

考虑教师（instructor）关系，下面的关系代数是什么意思？

$$
\Pi_{i.ID, i.name}(\sigma_{i.salary > w.salary}(\rho_i(instructor) \times \sigma_{w.id=12345}(\rho_w(instructor))))
$$

（提示：$\rho_r(R)$表示将R改名成r）
