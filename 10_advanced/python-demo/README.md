---
title: 使用Python访问数据库

author: CHEN Zhongpu

date: date

CJKmainfont: LXGW WenKai
---

## 1. 环境搭建

使用Python开发应用程序的第一步是搭建虚拟环境（`virtual environment`），主流的方式有三种：

- 直接使用[venv](https://docs.python.org/3/library/venv.html)（Python自带）
- 使用[conda](https://docs.conda.io/docs/user-guide/tasks/manage-environments.html)（Anaconda或Miniconda提供)
- 使用[uv](https://docs.astral.sh/uv/)（目前最佳实践）

### 创建虚拟环境并激活

> 如果使用PyCharm等集成开发环境，在创建项目时可以选择创建虚拟环境，并且IDE会自动激活它。

为了方便起见，下面的示例使用`venv`，其中`env`是虚拟环境的路径。

```bash
python3 -m venv env
```

接下来，激活虚拟环境：

```bash
# bash/zsh (Linux/macOS)
source env/bin/activate
# cmd.exe (Windows)
env\Scripts\activate.bat
# PowerShell (Windows)
env\Scripts\Activate.ps1
```

### 安装依赖

为了加速下载，建议使用国内的镜像，可选的包括[清华](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)和[南大](https://mirror.nju.edu.cn/mirrorz-help/pypi/?mirror=NJU)等。

```bash
# PostgreSQL
pip install -i https://mirror.nju.edu.cn/pypi/web/simple 'psycopg[binary]'

# MySQL
pip install -i https://mirror.nju.edu.cn/pypi/web/simple mysql-connector-python
```

> 对于PostgreSQL,实际上还有较老但使用也很广泛的`psycopg2-binary`。

## 2. 测试（PostgreSQL）

```python
import psycopg

# Update the conn as you need
with psycopg.connect("dbname=mydb user=postgres port=5432 password=") as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM department")
        records = cur.fetchall()
        print(records)
```

## 2. 测试（MySQL）

```python
import mysql.connector

# Update the conn as you need
cnx = mysql.connector.connect(
    host="127.0.0.1", port=3306, user="root", database="mydb", password=""
)

cur = cnx.cursor()

cur.execute("SELECT * FROM department")

records = cur.fetchall()
print(records)

cur.close()
cnx.close()
```

## 3. 练习

- [psycopg](https://www.psycopg.org/psycopg3/docs/)
- [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/)

实现数据库的增删改操作。
