
import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")

def weaponName(lang, name = '', type = ''):
    weapon = pd.read_sql_query("SELECT weapon.id, weapon_text.name ,attack, attack_true, element1, element1_attack, element2, element2_attack, weapon_type FROM weapon\
                               JOIN weapon_text ON weapon.id = weapon_text.id\
                               WHERE weapon_text.lang_id = '{}'\
                               AND weapon_text.name LIKE '%{}%'\
                               AND weapon.weapon_type  LIKE '%{}%'\
                               ".format(lang,name, type),conn)
    
    types = weapon['armor_type'].values 
    return [weapon,types[0]]
    # for index, row in weapon.iterrows():
    #     print("ID:", row['id'])
    #     print("Name:", row['name'])
    #     print("Type:", row['weapon_type'])
    #     print("Attack:", row['attack'])
    #     print("True Attack:", row['attack_true'])
    #     print("Element 1:", row['element1'])
    #     print("Element 1 Attack:", row['element1_attack'])
    #     print("Element 2:", row['element2'])
    #     print("Element 2 Attack:", row['element2_attack'])
    #     print("-------------------")
    


conn.close()