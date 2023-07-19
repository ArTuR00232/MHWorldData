import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")


#search charm by name
def datacharm(lang, name = '', type = ''):
    charm = pd.read_sql_query("SELECT c.id, rarity, name, description FROM charm AS c \
                              JOIN charm_text AS ct ON c.id = ct.id \
                              WHERE ct.lang_id == '{}'\
                              AND ct.name LIKE '%{}%'".format(lang,name), conn)
    # for index,row in charm.iterrows():
    #     print("ID:", row['id'])
    #     print("Name:", row['name'])
    #     print("Type:", row[''])
    #     print("Rarity:", row['rarity'])
    #     print("Description:", row['description'])
    #     print("-------------------")

#search decoration by name
def dataDecorationName(lang, name = ''):
    decoration = pd.read_sql_query("SELECT dect.id, dect.name AS named, stx.name,dec.rarity, description  FROM decoration AS dec \
                                   JOIN decoration_text AS dect ON dec.id = dect.id \
                                   JOIN skilltree AS st ON st.id = dec.id \
                                   JOIN skilltree_text AS  stx ON stx.id = st.id \
                                   WHERE dect.lang_id == '{}'\
                                   AND dect.name LIKE '%{}%'\
                                   AND stx.lang_id = '{}'".format(lang, name, lang), conn)
    # for index, row in decoration.iterrows():
    #     print("ID:", row['id'])
    #     print("Name:", row['named'])
    #     print("Name Skill:", row['name'])
    #     print("Rarity:", row['rarity'])
    #     print("Description:", row['description'])
    #     print("-------------------")





conn.close()