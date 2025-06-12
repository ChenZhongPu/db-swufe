# file: generate_large_parquet_corrected.py

import pandas as pd
import numpy as np
import os
import time
import pyarrow as pa
import pyarrow.parquet as pq


def generate_and_save_large_parquet_corrected(
    file_path: str = "large_dataset.parquet",
    target_size_gb: int = 10,
    rows_per_chunk: int = 1_000_000,
):
    """
    Generates a large Parquet file by writing in chunks using pyarrow.ParquetWriter.

    Args:
        file_path (str): The output Parquet file path.
        target_size_gb (int): The target file size in gigabytes.
        rows_per_chunk (int): The number of rows to generate and write at a time.
    """
    print("开始生成大型 Parquet 文件 (修正版)...")
    print(f"目标文件: {file_path}")
    print(f"目标大小: ~{target_size_gb} GB")
    print("-" * 30)

    # Data schema definition
    num_categories = 1000
    num_groups = 5000
    categories = [f"category_{i}" for i in range(num_categories)]
    groups = [f"group_{i}" for i in range(num_groups)]

    # Define the PyArrow schema to ensure consistency across chunks
    schema = pa.schema(
        [
            pa.field("id", pa.int64()),
            pa.field("group_id", pa.string()),
            pa.field("category_id", pa.string()),
            pa.field("value1", pa.float64()),
            pa.field("value2", pa.float64()),
            pa.field("timestamp", pa.timestamp("s")),
        ]
    )

    # Remove the old file if it exists
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"已删除旧文件: {file_path}")

    start_time = time.time()

    # Use ParquetWriter to append chunks
    with pq.ParquetWriter(file_path, schema, compression="snappy") as writer:
        total_rows_written = 0
        chunk_num = 0
        while True:
            chunk_start_time = time.time()
            chunk_num += 1

            # Create a data chunk as a pandas DataFrame
            df_chunk = pd.DataFrame(
                {
                    "id": np.arange(
                        total_rows_written, total_rows_written + rows_per_chunk
                    ),
                    "group_id": np.random.choice(groups, size=rows_per_chunk),
                    "category_id": np.random.choice(categories, size=rows_per_chunk),
                    "value1": np.random.randn(rows_per_chunk) * 1000,
                    "value2": np.random.randn(rows_per_chunk) * 500,
                    "timestamp": pd.to_datetime(
                        np.random.randint(
                            1_577_836_800, 1_609_372_800, size=rows_per_chunk
                        ),
                        unit="s",
                    ),
                }
            )
            total_rows_written += rows_per_chunk

            # Convert pandas DataFrame to a PyArrow Table
            table = pa.Table.from_pandas(df_chunk, schema=schema)

            # Write the table (chunk) to the Parquet file
            writer.write_table(table)

            chunk_end_time = time.time()
            print(
                f"已写入块 {chunk_num}，耗时: {chunk_end_time - chunk_start_time:.2f} 秒"
            )

            # Check file size to stop generation
            current_size_gb = os.path.getsize(file_path) / (1024**3)
            if current_size_gb >= target_size_gb:
                print(f"\n已达到目标文件大小 {current_size_gb:.2f} GB，停止生成。")
                break

    end_time = time.time()
    final_size_gb = os.path.getsize(file_path) / (1024**3)

    print("\n" + "=" * 30)
    print("文件生成完毕！")
    print(f"最终文件大小: {final_size_gb:.2f} GB")
    print(f"总耗时: {(end_time - start_time) / 60:.2f} 分钟")
    print("=" * 30)


if __name__ == "__main__":
    generate_and_save_large_parquet_corrected(
        file_path="large_dataset.parquet", target_size_gb=10
    )
