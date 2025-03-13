# SQL中的常量

参考[Constants](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-CONSTANTS).

> A numeric constant that contains neither a decimal point nor an exponent is initially presumed to be type integer if its value fits in type integer (32 bits); otherwise it is presumed to be type bigint if its value fits in type bigint (64 bits); otherwise it is taken to be type numeric. Constants that contain decimal points and/or exponents are always initially presumed to be type numeric.

| Name             | Storage Size | Description                     | Range                                                                                    |
| ---------------- | ------------ | ------------------------------- | ---------------------------------------------------------------------------------------- |
| smallint         | 2 bytes      | small-range integer             | -32768 to +32767                                                                         |
| integer          | 4 bytes      | typical choice for integer      | -2147483648 to +2147483647                                                               |
| bigint           | 8 bytes      | large-range integer             | -9223372036854775808 to +9223372036854775807                                             |
| decimal          | variable     | user-specified precision, exact | up to 131072 digits before the decimal point; up to 16383 digits after the decimal point |
| numeric          | variable     | user-specified precision, exact | up to 131072 digits before the decimal point; up to 16383 digits after the decimal point |
| real             | 4 bytes      | variable-precision, inexact     | 6 decimal digits precision                                                               |
| double precision | 8 bytes      | variable-precision, inexact     | 15 decimal digits precision                                                              |
| smallserial      | 2 bytes      | small autoincrementing integer  | 1 to 32767                                                                               |
| serial           | 4 bytes      | autoincrementing integer        | 1 to 2147483647                                                                          |
| bigserial        | 8 bytes      | large autoincrementing integer  | 1 to 9223372036854775807                                                                 |

In PostgreSQL, we can use `pg_typeof` to chek the type of a constant.

```sql
SELECT pg_typeof(1);
```

## MySQL

In standard SQL, the syntax `DECIMAL(M)` is equivalent to `DECIMAL(M,0)`. Similarly, the syntax `DECIMAL` is equivalent to `DECIMAL(M,0)`, where the implementation is permitted to decide the value of `M`. MySQL supports both of these variant forms of `DECIMAL` syntax. The default value of `M` is 10.
