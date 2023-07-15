import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")




def toolName(lang,name):
    tool = pd.read_sql_query("SELECT t.id, tool_type, name, slot_1, slot_2, slot_3 FROM tool AS t \
                              JOIN tool_text AS ttx on t.id = ttx.id \
                              WHERE ttx.lang_id == '{}' and ttx.name LIKE '%{}%'".format(lang,name), conn)
    for index,row in tool.iterrows():
        print("ID:", row['id'])
        print("Name:", row['name'])
        print("Tool Type:", row['tool_type'])
        print("Slot1:", row['slot_1'])
        print("Slot2:", row['slot_2'])
        print("Slot3:", row['slot_3'])
        print("-------------------")

def toolType(lang,type):
    tool = pd.read_sql_query("SELECT t.id, tool_type, name, slot_1, slot_2, slot_3 FROM tool AS t \
                              JOIN tool_text AS ttx on t.id = ttx.id \
                              WHERE ttx.lang_id == '{}' and t.tool_type LIKE '%{}%'".format(lang,type), conn)
    for index,row in tool.iterrows():
        print("ID:", row['id'])
        print("Name:", row['name'])
        print("Tool Type:", row['tool_type'])
        print("Slot1:", row['slot_1'])
        print("Slot2:", row['slot_2'])
        print("Slot3:", row['slot_3'])
        print("-------------------")

toolName('pt','booster')
toolType('pt','booster')


conn.close()