import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")



#search by name and/or type
def tool(lang,name = '', type = ''):
    tool = pd.read_sql_query("SELECT t.id, tool_type, name, slot_1, slot_2, slot_3 FROM tool AS t \
                              JOIN tool_text AS ttx ON t.id = ttx.id \
                              WHERE ttx.lang_id == '{}'\
                              AND ttx.name LIKE '%{}%'\
                              AND t.tool_type LIKE '%{}%'".format(lang,name, type), conn)
    # for index,row in tool.iterrows():
    #     print("ID:", row['id'])
    #     print("Name:", row['name'])
    #     print("Tool Type:", row['tool_type'])
    #     print("Slot1:", row['slot_1'])
    #     print("Slot2:", row['slot_2'])
    #     print("Slot3:", row['slot_3'])
    #     print("-------------------")


conn.close()