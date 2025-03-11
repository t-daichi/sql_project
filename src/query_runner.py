import pandas as pd
import sqlite3

# SQLiteデータベースの作成
db_path = "data/imdb_movies.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# CSVを読み込んでSQLiteに保存
csv_path = "data/imdb_movies.csv"
df = pd.read_csv(csv_path)
df.to_sql("movies", conn, if_exists="replace", index=False)

print("データの保存完了")

conn.close()
