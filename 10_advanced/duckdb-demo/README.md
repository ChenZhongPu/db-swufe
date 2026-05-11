# duckdb-demo

这个项目用 `uv` 管理 Python 环境，用于测试 DuckDB 的几种常见用法：

- 访问已有 DuckDB 数据库：`mydb.db`
- 读取 CSV：`customers.csv`
- 读取 JSON：`orders.json`
- 读取 Excel：`file_example_XLSX_50.xlsx`

## 运行

每个示例文件都可以独立运行：

```bash
uv run python database_access.py
uv run python read_csv_file.py
uv run python read_json_file.py
uv run python read_excel_file.py
```

## 文件说明

- `database_access.py`：用只读连接访问 `mydb.db`，查看表并执行聚合查询。
- `read_csv_file.py`：用 `read_csv_auto(...)` 直接读取 CSV。
- `read_json_file.py`：用 `read_json_auto(...)` 读取 JSON，并展开嵌套数组。
- `read_excel_file.py`：执行 `INSTALL excel` 和 `LOAD excel` 后读取 `.xlsx`。
- `customers.csv`、`orders.json`：为示例创建的测试数据。

## Excel 说明

DuckDB 可以直接读取 `.xlsx` 文件：

```sql
INSTALL excel;
LOAD excel;
SELECT * FROM 'file_example_XLSX_50.xlsx';
SELECT * FROM read_xlsx('file_example_XLSX_50.xlsx', header = true);
```
