
import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")


#search by name and/or type of the item
def armor(lang,name = '', type = ''):
    armor = pd.read_sql_query("SELECT armor.id,armor_text.name, defense_base, defense_max, fire, thunder, water, ice, dragon, armor_type FROM armor\
                              JOIN armor_text ON armor.id = armor_text.id \
                              WHERE armor_text.lang_id == '{}'\
                              AND armor_text.name LIKE '%{}%'\
                              AND armor.armor_type LIKE '%{}%'\
                              ".format(lang, name, type), conn)
    
    return armor
    # for index,row in armor.iterrows():
    #     print("ID:", row['id'])
    #     print("Name:", row['name'])
    #     print("Type:", row['armor_type'])
    #     print("Defense_base:", row['defense_base'])
    #     print("Defense_max:", row['defense_max'])
    #     print("Fire:", row['fire'])
    #     print("Thunder:", row['thunder'])
    #     print("Water:", row['water'])
    #     print("Ice:", row['ice'])
    #     print("Dragon:", row['dragon'])
    #     print("-------------------")
    
# a = armor('pt', 'Elmo de Couro α')
# print(str(a))
#conn.close()