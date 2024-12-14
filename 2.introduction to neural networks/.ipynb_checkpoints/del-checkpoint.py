import pandas as pd
import cx_Oracle

df = pd.read_csv("datat/data.csv")

# Connect to Oracle
connection = cx_Oracle.connect("sys", "Lap758405", "localhost:1522/XEPDB1", mode=cx_Oracle.SYSDBA)

cursor = connection.cursor()

# # Insert data into the table
# for _, row in df.iterrows():
#     cursor.execute("""
#         INSERT INTO your_table_name (column1, column2, column3)
#         VALUES (:1, :2, :3)
#     """, (row['column1'], row['column2'], row['column3']))

# connection.commit()
# cursor.close()
# connection.close()
