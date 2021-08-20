# Relational Model
数据模型是描述数据、数据联系、数据语义以及一致性约束的概念工具的集合。本周我们学习的是**关系模型**。此外，为了理解关系数据库查询语言的理论基础，我们还学习了**关系代数**。

# 本周作业（第1次作业）
## 题目一（2分+3分）
考虑一个`银行`数据库，其关系模式如下所示：

- branch (branch_name, branch_city, assets)
- customer (ID, customer_name, customer_street, customer_city)
- loan (loan_number, branch_name, amount)
- borrower (ID, loan_number)
- account (account_number, branch_name, balance)
- depositor (ID, account_number)

使用`关系代数`完成下面的查询：

1. 找到位于`成都`市的支行的名字。
2. 找到在`杨柳`支行有贷款（`loan`）的借款人（`borrower`）的ID。

## 题目二（3分）
考虑两个关系模式，
- student (ID, name, class)
- people (ID, name, nationality, occupation)

请问两者之间进行关系代数的`并`、`交`和`差`是否有意义？你从中能总结出什么？

## 题目三（2分）
假设数据库中存储用户名和密码的关系模式是 user(name, pswd, gender)，请结合关系代数简述实现`用户登录`逻辑的思路。