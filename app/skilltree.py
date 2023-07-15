import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")


def skilltree(lang, name):
    skilltree = pd.read_sql_query("SELECT stx.id,name, max_level, description FROM skilltree AS st\
                                  JOIN skilltree_text AS stx on st.id = stx.id\
                                  WHERE stx.lang_id = '{}' \
                                  and stx.name LIKE '%{}%'".format(lang,name), conn)
    print(skilltree)

skilltree('pt',' ')