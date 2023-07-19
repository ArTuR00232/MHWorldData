
import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")

#quest by monster/rank/type
import pandas as pd
import sqlite3

#connection with the data base
conn = sqlite3.connect("mhw.db")

#serch by name, category
def item(lang, name = '', category = ''):
    item = pd.read_sql_query("SELECT it.name AS result, it2.name AS item1,it3.name AS item2, it.description FROM item_combination AS ic\
                                 JOIN item AS i ON i.id = ic.result_id\
                                 JOIN item AS i1 ON i1.id = ic.first_id \
                                 JOIN item AS i2 ON i2.id = ic.second_id\
                                 JOIN item_text AS it ON it.id = ic.result_id\
                                 JOIN item_text AS it2 ON i1.id = it2.id\
                                 JOIN item_text AS it3 ON i2.id = it3.id\
                                 WHERE it.lang_id = '{}'\
                                 AND it2.lang_id = '{}'\
                                 AND it3.lang_id = '{}'\
                                 AND i.category LIKE '%{}%'\
                                 ".format(lang, lang, lang, category),conn)
    # item = pd.read_sql_query("SELECT * FROM item AS i\
    #                          JOIN item_text AS it ON i.id = it.id\
    #                          WHERE it.lang_id = '{}'\
    #                          AND it.name LIKE '%{}%'\
    #                          AND i.category LIKE '%{}%'\
    #                          ".format(lang, name, category), conn)
    

    print(item)
    x=0
    for index, row in item.iterrows():
        while x < 1:
            with open ('./app/text.txt', 'w') as file:
                file.write(str(row))
            x=x+1

    return item

    #quests = quest.merge(item_name)
    #     print("ID: ", row['id'])
    #     print("Quest: ", row['name'])
    #     print("Rank: ", row['rank'])    
    #     print("Stars: ", row['stars'])        
    #     print("Type: ", row['quest_type'])
    #     print("Zenny: ", row['zenny'])        
    #     print("-------------------")

    
    # print(quest)
    # x=0
    # for index, row in quest.iterrows():
    #     while x < 1:
    #         with open ('./text.txt', 'w') as file:
    #             file.write(str(row))
    #         x+=1


item('pt', 'megapoção')
conn.close()
