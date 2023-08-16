
import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")

#quest by monster/rank/type
def quests(lang, monster = '', rank = '', type = '', item = ''):
    quest = pd.read_sql_query("SELECT q.id, mont.name,q.rank, q.stars, q.quest_type, q.zenny, it.name AS item_name from quest AS q\
                              JOIN quest_text AS qt ON q.id = qt.id\
                              JOIN quest_reward AS qr ON q.id = qr.quest_id\
                              JOIN item_text AS it on qr.item_id = it.id\
                              JOIN quest_monster AS qm ON q.id = qm.quest_id\
                              JOIN monster AS mon ON qm.monster_id = mon.id\
                              JOIN monster_text AS mont ON mon.id = mont.id\
                              WHERE qt.lang_id = '{}'\
                              AND mont.name LIKE '%{}%'\
                              AND mont.lang_id = '{}'\
                              AND q.rank  LIKE '%{}%'\
                              AND q.quest_type LIKE '%{}%'\
                              AND it.lang_id = '{}'\
                              AND it.name LIKE '%{}%'\
                              ".format(lang,monster, lang, rank, type, lang, item), conn)
    return quest
    #quests = quest.merge(item_name)
    #     print("ID: ", row['id'])
    #     print("Quest: ", row['name'])
    #     print("Rank: ", row['rank'])    
    #     print("Stars: ", row['stars'])        
    #     print("Type: ", row['quest_type'])
    #     print("Zenny: ", row['zenny'])
    #     print("item: ", row['item_name'])
    #     print("-------------------")

    

# p = quests('pt')
# print(p)
conn.close()
