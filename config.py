import os
from dotenv_vault import load_dotenv
import sys

try:
    load_dotenv(override=True)
except FileNotFoundError:
    print(".env file not found! Using default settings.")
    try:
        load_dotenv(f".env.default")
    except FileNotFoundError:
        print(".env.default file not found! No setting to load.")

# 获取第一个参数
if len(sys.argv) > 1:
    env_state = sys.argv[1]
    print(f"load .env.{env_state}")
    # 加载特定环境的环境变量
    load_dotenv(f".env.{env_state}", override=True)


class Config:
    sqlite_db_name = 'net_snip.db'
    default_word_length = 5
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT")
    db_database = os.getenv("POSTGRES_DATABASE")
    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    file_limit_size = os.getenv("FILE_LIMIT_SIZE") if os.getenv("FILE_LIMIT_SIZE") is not None else "5M"
    file_limit_total_size = os.getenv("FILE_LIMIT_TOTAL_SIZE") if os.getenv(
        "FILE_LIMIT_TOTAL_SIZE") is not None else "50M"
