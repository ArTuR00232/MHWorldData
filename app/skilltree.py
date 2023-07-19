import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")

#search by name
def skilltree(lang, name = ''):
    skilltree = pd.read_sql_query("SELECT stx.id,name, max_level, description FROM skilltree AS st\
                                  JOIN skilltree_text AS stx ON st.id = stx.id\
                                  WHERE stx.lang_id = '{}' \
                                  AND stx.name LIKE '%{}%'".format(lang,name), conn)
    # for index,row in skilltree.iterrows():
    #     print("ID:", row['id'])
    #     print("Name:", row['name'])
    #     print("Max_level:", row['max_level'])
    #     print("Description:", row['description'])
    #     print("-------------------")

conn.close()