import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")


#search charm by name
def datacharm(lang, name):
    charm = pd.read_sql_query("SELECT c.id, rarity, name, description FROM charm AS c \
                              JOIN charm_text AS ct on c.id = ct.id \
                              WHERE ct.lang_id == '{}' and ct.name LIKE '%{}%'".format(lang,name), conn)
    for index,row in charm.iterrows():
        print("ID:", row['id'])
        print("Name:", row['name'])
        print("Rarity:", row['rarity'])
        print("Description:", row['description'])
        print("-------------------")

#search charm by  type
def datacharmType(lang, type):
    charm = pd.read_sql_query("SELECT c.id, rarity, name, description FROM charm AS c \
                              JOIN charm_text AS ct on c.id = ct.id \
                              WHERE ct.lang_id == '{}' and ct.name LIKE '%{}%'".format(lang,type), conn)
    for index, row in charm.iterrows():
        print("ID:", row['id'])
        print("Name:", row['name'])
        print("Rarity:", row['rarity'])
        print("Description:", row['description'])
        print("-------------------")


#have two columns with the same name "name" in decoration_text and skilltree_text
def dataDecorationName(lang, name):
    decoration = pd.read_sql_query("SELECT dect.id, dect.name AS named, stx.name,dec.rarity, description  FROM decoration AS dec \
                                   JOIN decoration_text AS dect on dec.id = dect.id \
                                   JOIN skilltree AS st on st.id = dec.id \
                                   JOIN skilltree_text AS  stx on stx.id = st.id \
                                   WHERE dect.lang_id == '{}' and dect.name LIKE '%{}%' and stx.lang_id = '{}'".format(lang, name, lang), conn)
    for index, row in decoration.iterrows():
        print("ID:", row['id'])
        print("Name:", row['named'])
        print("Name Skill:", row['name'])
        print("Rarity:", row['rarity'])
        print("Description:", row['description'])
        print("-------------------")


dataDecorationName('pt', ' ')
#datacharm('pt','')
#datacharmType('pt', ' ')


conn.close()