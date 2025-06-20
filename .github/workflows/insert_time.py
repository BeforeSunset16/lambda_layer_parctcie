import pandas as pd
import snowflake.connector
from datetime import datetime
import pytz

pst = pytz.timezone('US/Pacific')
est = pytz.timezone('US/Eastern')

# 模拟或加载数据（你可以改为读取 CSV 或其他来源）
df = pd.DataFrame([    
    {'CREATED_AT': datetime.now(pytz.utc)}    
])

# 计算 PST 年、月、日、小时
df['PST_YEAR'] = df['CREATED_AT'].apply(lambda x: int(x.astimezone(pst).year))
df['PST_MONTH'] = df['CREATED_AT'].apply(lambda x: int(x.astimezone(pst).month))
df['PST_DAY'] = df['CREATED_AT'].apply(lambda x: int(x.astimezone(pst).day))
df['PST_HOUR'] = df['CREATED_AT'].apply(lambda x: int(x.astimezone(pst).hour))

# 计算 EST 年、月、日、小时
df['EST_YEAR'] = df['CREATED_AT'].apply(lambda x: int(x.astimezone(est).year))
df['EST_MONTH'] = df['CREATED_AT'].apply(lambda x: int(x.astimezone(est).month))
df['EST_DAY'] = df['CREATED_AT'].apply(lambda x: int(x.astimezone(est).day))
df['EST_HOUR'] = df['CREATED_AT'].apply(lambda x: int(x.astimezone(est).hour))

df['A'] = df['CREATED_AT'].apply(lambda x: int(str(x.hour)[0]))
df['B'] = df['CREATED_AT'].apply(lambda x: int(str(x.hour)[1]))
df['C'] = df['CREATED_AT'].apply(lambda x: int(str(x.minute)[0]))
df['D'] = df['CREATED_AT'].apply(lambda x: int(str(x.minute)[1]))
df['E'] = df['CREATED_AT'].apply(lambda x: int(str(x.second)[0]))
df['F'] = df['CREATED_AT'].apply(lambda x: int(str(x.second)[1]))
df['CREATED_AT'] = df['CREATED_AT'].apply(lambda x: x.isoformat())
# 连接 Snowflake
conn = snowflake.connector.connect(
    user='SHENPRACTISE',
    password='Hanpractice123',
    account='fb69655',   # 如：xy12345.ca-central-1
    warehouse='DAG3_WH',
    database='ML_HOL_DB',
    schema='PLAYGROUND'
)

cursor = conn.cursor()

# 构建 insert 语句（忽略自增 ID 字段）
columns = [
    'CREATED_AT', 'PST_YEAR', 'PST_MONTH', 'PST_DAY', 'PST_HOUR',
    'A', 'B', 'C', 'D', 'E', 'F',
    'EST_YEAR', 'EST_MONTH', 'EST_DAY', 'EST_HOUR'
]

placeholders = ', '.join(['%s'] * len(columns))
column_names = ', '.join(columns)

insert_sql = f"""
    INSERT INTO PANDAS_INSERT_TIME ({column_names})
    VALUES ({placeholders})
"""

# 插入每一行
for _, row in df.iterrows():
    values = [row[col] for col in columns]
    cursor.execute(insert_sql, values)

cursor.close()
conn.close()