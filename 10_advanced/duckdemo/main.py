import pandas as pd
import duckdb
import time
import os
import psutil  # 用于监控内存

# --- 配置 ---
PARQUET_FILE = "large_dataset.parquet"


def get_memory_usage():
    """获取当前 Python 进程的内存使用情况 (MB)"""
    process = psutil.Process()
    return process.memory_info().rss / (1024 * 1024)


def test_pandas_performance():
    """使用 Pandas 执行分析任务并测试性能"""
    print("\n" + "=" * 30)
    print("🚀 开始测试 Pandas 性能...")
    print("=" * 30)

    start_mem = get_memory_usage()
    print(f"初始内存使用: {start_mem:.2f} MB")

    start_time = time.perf_counter()

    try:
        # 1. 读取整个 Parquet 文件到内存
        print("步骤 1: 正在读取 Parquet 文件到内存... (这可能会非常慢或失败)")
        df = pd.read_parquet(PARQUET_FILE)
        read_time = time.perf_counter()
        read_mem = get_memory_usage()
        print(f"文件读取完毕。耗时: {read_time - start_time:.2f} 秒")
        print(
            f"读取后内存使用: {read_mem:.2f} MB (增长了 {read_mem - start_mem:.2f} MB)"
        )

        # 2. 执行分组、聚合和排序
        print("\n步骤 2: 正在执行 groupby, agg, sort...")
        result = (
            df.groupby("group_id")
            .agg(sum_value1=("value1", "sum"), mean_value2=("value2", "mean"))
            .sort_values(by="sum_value1", ascending=False)
            .head(10)
        )

        end_time = time.perf_counter()
        end_mem = get_memory_usage()

        print("\n--- Pandas 结果 ---")
        print(result)
        print("---------------------")
        print(f"最终内存使用: {end_mem:.2f} MB")
        print(f"Pandas 总执行时间: {end_time - start_time:.2f} 秒")

    except MemoryError:
        end_time = time.perf_counter()
        print("\n" + "!" * 30)
        print("内存错误 (MemoryError)！Pandas 无法将整个文件加载到内存中。")
        print(f"测试失败于 {end_time - start_time:.2f} 秒。")
        print("!" * 30)
    except Exception as e:
        end_time = time.perf_counter()
        print(f"\n发生未知错误: {e}")
        print(f"测试失败于 {end_time - start_time:.2f} 秒。")


def test_duckdb_performance():
    """使用 DuckDB 执行分析任务并测试性能"""
    print("\n" + "=" * 30)
    print("🦆 开始测试 DuckDB 性能...")
    print("=" * 30)

    start_mem = get_memory_usage()
    print(f"初始内存使用: {start_mem:.2f} MB")

    start_time = time.perf_counter()

    # DuckDB 直接在文件上执行 SQL 查询，无需将整个文件读入内存
    # DuckDB 的查询优化器会处理所有事情
    query = f"""
    SELECT
        group_id,
        SUM(value1) AS sum_value1,
        AVG(value2) AS mean_value2
    FROM '{PARQUET_FILE}'
    GROUP BY group_id
    ORDER BY sum_value1 DESC
    LIMIT 10;
    """

    print("正在执行 DuckDB SQL 查询...")

    # 连接到 DuckDB (可以是在内存中)
    con = duckdb.connect()
    result = con.execute(query).fetchdf()  # fetchdf() 直接将结果转换为 Pandas DataFrame

    end_time = time.perf_counter()
    end_mem = get_memory_usage()

    print("\n--- DuckDB 结果 ---")
    print(result)
    print("-------------------")
    print(f"最终内存使用: {end_mem:.2f} MB (峰值内存增长非常小)")
    print(f"DuckDB 总执行时间: {end_time - start_time:.2f} 秒")

    con.close()


if __name__ == "__main__":
    # 确保文件存在
    if not os.path.exists(PARQUET_FILE):
        print(f"错误: Parquet 文件 '{PARQUET_FILE}' 不存在。")
        print("请先运行 'generate_large_parquet.py' 来生成文件。")
    else:
        # 运行 Pandas 测试
        # test_pandas_performance()

        # 运行 DuckDB 测试
        test_duckdb_performance()
