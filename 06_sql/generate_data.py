import csv
import random
from datetime import datetime

# 配置参数
num_records = 100000
output_file = "product_data.csv"


def generate_product_data():
    """生成产品测试数据并保存为CSV文件"""
    print(f"开始生成{num_records}条产品数据...")
    start_time = datetime.now()

    with open(output_file, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        for i in range(1, num_records + 1):
            name = f"p{i}"
            price = round(random.uniform(0, 1000), 2)
            csv_writer.writerow([name, price])
            # 每生成10000条数据显示一次进度
            if i % 10000 == 0:
                print(f"已生成 {i} 条数据...")

    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds()

    print("数据生成完成！")
    print(f"总共生成了 {num_records} 条记录")
    print(f"耗时: {elapsed:.2f}秒")
    print(f"数据已保存到文件: {output_file}")


if __name__ == "__main__":
    generate_product_data()
