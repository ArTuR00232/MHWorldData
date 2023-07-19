import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")

#serch by name, category
def item(lang, name = '', category = ''):
    item = pd.read_sql_query("SELECT i.id,name,category, subcategory, description FROM item as i\
                             JOIN item_text AS it ON i.id = it.id\
                             JOIN item_combination AS ic ON ic.result_id = i.id AND ic.result_id = it.id\
                             WHERE it.lang_id = '{}'\
                             AND it.name LIKE '%{}%'\
                             AND i.category LIKE '%{}%'\
                             ".format(lang, name, category), conn)
    
    return item


p = item('pt')
print(p)
