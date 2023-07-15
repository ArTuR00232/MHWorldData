
import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")

def weaponName(lang, name):
    weapon = pd.read_sql_query("SELECT weapon.id, weapon_text.name ,attack, attack_true, element1, element1_attack, element2, element2_attack FROM weapon\
                               JOIN weapon_text on weapon.id = weapon_text.id\
                               WHERE weapon_text.lang_id = '{}'\
                               and weapon_text.name LIKE '%{}%'".format(lang,name),conn)
    for index, row in weapon.iterrows():
        print("ID:", row['id'])
        print("Name:", row['name'])
        print("Attack:", row['attack'])
        print("True Attack:", row['attack_true'])
        print("Element 1:", row['element1'])
        print("Element 1 Attack:", row['element1_attack'])
        print("Element 2:", row['element2'])
        print("Element 2 Attack:", row['element2_attack'])
        print("-------------------")
    

def weaponType(lang, type):
    weapon = pd.read_sql_query("SELECT weapon.id, weapon_text.name ,attack, attack_true, element1, element1_attack, element2, element2_attack FROM weapon\
                               JOIN weapon_text on weapon.id = weapon_text.id\
                               WHERE weapon_text.lang_id = '{}'\
                               and weapon.weapon_type LIKE '%{}%'".format(lang,type),conn)
    for index, row in weapon.iterrows():
        print("ID:", row['id'])
        print("Name:", row['name'])
        print("Attack:", row['attack'])
        print("True Attack:", row['attack_true'])
        print("Element 1:", row['element1'])
        print("Element 1 Attack:", row['element1_attack'])
        print("Element 2:", row['element2'])
        print("Element 2 Attack:", row['element2_attack'])
        print("-------------------")

#weaponName('pt', 'great')
weaponType('pt', 'dual')


conn.close()