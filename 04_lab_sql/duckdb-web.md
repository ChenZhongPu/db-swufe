# DuckDB Web Shell

[DuckDB Web Shell](https://shell.duckdb.org/)是`wasm`版本的DuckDB，方便学习使用。

```bash
.files add
.files list
ATTACH 'mydb.db' AS mydb;
USE mydb;
SELECT * FROM instructor;
```

参考 [ATTACH and DETACH](https://duckdb.org/docs/stable/sql/statements/attach)。
