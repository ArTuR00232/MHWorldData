import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")

#serch by name, type attack, dust efect
def kinsect(lang, name = '', attack = '', dust = ''):
    kinsect = pd.read_sql_query("SELECT k.id,name,attack_type, dust_effect, power, speed, heal FROM kinsect as k\
                             JOIN kinsect_text AS kt ON k.id = kt.id\
                             WHERE kt.lang_id = '{}'\
                             AND kt.name LIKE '%{}%'\
                             AND k.attack_type LIKE '%{}%'\
                             AND k.dust_effect LIKE '%{}%'\
                             ".format(lang, name, attack, dust), conn)
    
    return kinsect

    