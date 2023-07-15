
import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")


# receve a term of monster data the user want to consult
# def dataArmor(lang, name):
#     armor = pd.read_sql_query("SELECT at.name as t,a.id as a, at.name as at, ask.armor_id as ask, ars.id as ars, arst.name as arst, arsb.setbonus_id as arsb, arsbt.name as arsbt, st.id as st, stx.name as stx  FROM armor AS a \
#                               JOIN armor_text AS at on at.id = a.id\
#                               JOIN armor_skill AS ask on a.id = ask.armor_id \
#                               LEFT JOIN armorset AS ars on a.armorset_id = ars.id \
#                               JOIN armorset_text AS arst on a.armorset_id = arst.id \
#                               LEFT JOIN armorset_bonus_skill AS arsb on arsb.setbonus_id = a.armorset_bonus_id \
#                               JOIN armorset_bonus_text AS arsbt on arsbt.id = a.armorset_bonus_id \
#                               LEFT JOIN skilltree AS st on arsb.skilltree_id = st.id \
#                               JOIN skilltree_text AS stx on st.id = stx.id \
#                               WHERE at.lang_id == '{}' and at.name LIKE '%{}%' \
#                               and arst.lang_id == '{}'\
#                               and arsbt.lang_id == '{}'\
#                               and stx.lang_id == '{}'\
#                               ".format(lang, name,lang,lang,lang), conn)
#    # print(armor)
#     return armor

#search by name of the item
def dataArmorName(lang,name):
    armor = pd.read_sql_query("SELECT armor.id,armor_text.name, defense_base, defense_max, fire, thunder, water, ice, dragon FROM armor\
                              JOIN armor_text on armor.id = armor_text.id \
                              WHERE armor_text.lang_id == '{}'  and armor_text.name LIKE '%{}%'".format(lang,name), conn)
    for index,row in armor.iterrows():
        print("ID:", row['id'])
        print("Name:", row['name'])
        print("Defense_base:", row['defense_base'])
        print("Defense_max:", row['defense_max'])
        print("Fire:", row['fire'])
        print("Thunder:", row['thunder'])
        print("Water:", row['water'])
        print("Ice:", row['ice'])
        print("Dragon:", row['dragon'])
        print("-------------------")
    

#search by type of the armor
def dataArmortype(lang, name):
    armor = pd.read_sql_query("SELECT armor.id, armor_text.name, defense_base, defense_max, fire, thunder, water, ice, dragon FROM armor\
                              JOIN armor_text on armor.id = armor_text.id \
                              WHERE armor_text.lang_id == '{}'  and armor.armor_type LIKE '%{}%'".format(lang,name), conn)
    for index,row in armor.iterrows():
        print("ID:", row['id'])
        print("Name:", row['name'])
        print("Defense_base:", row['defense_base'])
        print("Defense_max:", row['defense_max'])
        print("Fire:", row['fire'])
        print("Thunder:", row['thunder'])
        print("Water:", row['water'])
        print("Ice:", row['ice'])
        print("Dragon:", row['dragon'])
        print("-------------------")



dataArmorName('pt','head')
dataArmortype('pt','head')


conn.close()