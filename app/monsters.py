import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")



#search by name and/or size of the monsters
def monster(lang, name = '', size = ''):
    count = 1
    monster = pd.read_sql_query("SELECT mon.id, mont.name, weakness_fire, weakness_water, weakness_ice, weakness_thunder, weakness_dragon, weakness_poison, weakness_sleep, weakness_paralysis, weakness_blast, weakness_stun, description, size FROM monster AS mon\
                                JOIN monster_text AS mont ON mon.id = mont.id\
                                WHERE mont.lang_id = '{}'\
                                AND mont.name LIKE '%{}%'\
                                AND mon.size LIKE '%{}%'\
                                 ".format(lang, name, size), conn)
    # for index, row in monster.iterrows():    
    #     print(count)
    #     print("ID:", row['id'])
    #     print("Name:", row['name'])
    #     print("Size:", row['size'])        
    #     print("Fire:", row['weakness_fire'])
    #     print("Water:", row['weakness_water'])
    #     print("Ice:", row['weakness_ice'])
    #     print("Dragon:", row['weakness_dragon'])
    #     print("Poison:", row['weakness_poison'])
    #     print("Sleep:", row['weakness_sleep'])
    #     print("Paralyses:", row['weakness_paralysis'])
    #     print("Blast:", row['weakness_blast'])
    #     print("Stun:", row['weakness_stun'])
    #     print("Description:", row['description'])
    #     print("-------------------")
    #     count+=1


conn.close()
