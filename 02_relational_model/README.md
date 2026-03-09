# Relational Model
数据模型是描述数据、数据联系、数据语义以及一致性约束的概念工具的集合。本周我们学习的是**关系模型**。此外，为了理解关系数据库查询语言的理论基础，我们还学习了**关系代数**。

----
## 教材评注

> The *relational algebra* is a functional query language.

这里的`functional`表示函数式的，而是源于数学和计算机科学中的**函数式编程（Functional Programming）**概念。具体而言，查询是由一系列嵌套的、无状态的函数调用组成的，这些函数以关系为定义域和值域。

```python
employees = [
    {'name': 'Alice', 'dept': 'Dev', 'salary': 5000},
    {'name': 'Bob', 'dept': 'HR', 'salary': 4000}
]

# 1. Filter 对应关系代数中的 选择 (Selection σ)
# 2. Map 对应关系代数中的 投影 (Projection π)
result = map(lambda e: e['salary'] * 1.1, 
             filter(lambda e: e['dept'] == 'Dev', employees))
```

关系代数是数据库查询理论的基础，最新的研究参见：https://claude.ai/share/5c0534c3-7c63-49ac-940e-362827e9378e

----

## 本周作业（第1次作业）
### 题目一
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

### 题目二
假设数据库中存储用户名和密码的关系模式是 users(name, pswd, gender)，请结合关系代数简述实现`用户登录`逻辑的思路。

### 思考

下面两个关系代数表达式是否等价？

```math
\sigma_{dept\_name='Physics'}(instructor \Join_{instructor.ID=teaches.ID} teaches)   
```

```math
(\sigma_{dept\_name='Physics'}(instructor)) \Join_{instructor.ID=teaches.ID} teaches
```