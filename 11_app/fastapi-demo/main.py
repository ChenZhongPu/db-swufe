import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import psycopg

# 加载 .env 文件中的环境变量
load_dotenv()

# 创建 FastAPI 应用
app = FastAPI(title="教师信息API", description="提供教师信息查询功能")


# 从环境变量获取数据库连接信息
class DatabaseConfig:
    """数据库配置类"""

    def __init__(self):
        self.db_name = os.environ.get("DB_NAME", "mydb")
        self.db_user = os.environ.get("DB_USER", "postgres")
        self.db_port = os.environ.get("DB_PORT", "5432")
        self.db_password = os.environ.get("DB_PASSWORD", "")
        self.db_host = os.environ.get("DB_HOST", "localhost")

    def get_connection_string(self) -> str:
        """返回数据库连接字符串"""
        return f"dbname={self.db_name} user={self.db_user} password={self.db_password} host={self.db_host} port={self.db_port}"


# 数据库操作函数
def get_db_connection():
    """获取数据库连接"""
    db_config = DatabaseConfig()
    try:
        return psycopg.connect(db_config.get_connection_string())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"数据库连接失败: {str(e)}")


@app.get("/")
def read_root():
    """API根路径"""
    return {"message": "欢迎使用教师信息API"}


@app.get("/teachers/{teacher_id}")
def find_teacher_by_id(teacher_id: str) -> float:
    """
    根据ID查询教师信息

    参数:
    - teacher_id: 教师ID

    返回:
    - 教师salary
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                # 使用参数化查询防止SQL注入
                cur.execute(
                    "SELECT salary FROM instructor WHERE ID = %s", (teacher_id,)
                )
                result = cur.fetchone()

                if result is None:
                    raise HTTPException(
                        status_code=404, detail=f"ID为{teacher_id}的教师不存在"
                    )
                return float(result[0])

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    # 启动服务器，开发环境使用
    uvicorn.run(app, host="0.0.0.0", port=8000)
