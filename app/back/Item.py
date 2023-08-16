#connection with the data base
conn = sqlite3.connect("mhw.db")

#quest by monster/rank/type
import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")

#serch by name, category
def item(lang, name = '', category = ''):
    item = pd.read_sql_query("SELECT it.name AS result, it2.name AS item1,it3.name AS item2, it.description FROM item_combination AS ic\
                                 JOIN item AS i ON i.id = ic.result_id\
                                 JOIN item AS i1 ON i1.id = ic.first_id \
                                 JOIN item AS i2 ON i2.id = ic.second_id\
                                 JOIN item_text AS it ON it.id = ic.result_id\
                                 JOIN item_text AS it2 ON i1.id = it2.id\
                                 JOIN item_text AS it3 ON i2.id = it3.id\
                                 WHERE it.lang_id = '{}'\
                                 AND it2.lang_id = '{}'\
                                 AND it3.lang_id = '{}'\
                                 AND i.category LIKE '%{}%'\
                                 ".format(lang, lang, lang, category),conn)
    

conn.close()