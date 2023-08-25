from flask import request, jsonify
from conn import db_connection


#quest by monster/rank/type
def get_quests(lg = 'en', mtr = '', rk = '', ty = '', it = ''):
    lang = request.args.get('lang',lg) 
    monster = request.args.get('moster',mtr)
    rank = request.args.get('rank',rk)
    quest_type = request.args.get('type',ty)
    item = request.args.get('item',it)

    conn = db_connection()
    cursor = conn.cursor()

    query = "SELECT q.id, mont.name,q.rank, q.stars, q.quest_type, q.zenny, it.name AS item_name from quest AS q\
                              JOIN quest_text AS qt ON q.id = qt.id\
                              JOIN quest_reward AS qr ON q.id = qr.quest_id\
                              JOIN item_text AS it on qr.item_id = it.id\
                              JOIN quest_monster AS qm ON q.id = qm.quest_id\
                              JOIN monster AS mon ON qm.monster_id = mon.id\
                              JOIN monster_text AS mont ON mon.id = mont.id\
                              WHERE qt.lang_id = ?\
                              AND mont.name LIKE ?\
                              AND mont.lang_id = ?\
                              AND q.rank  LIKE ?\
                              AND q.quest_type LIKE ?\
                              AND it.lang_id = ?\
                              AND it.name LIKE ?\
                              "
    cursor.execute(query,(lang,f'%{monster}%', lang, f'%{rank}%', f'%{quest_type}%', lang, f'%{item}%'))
    
    quest_data = cursor.fetchall()
    
    quest_list =[
        {
            "ID: ": row[0],
            "Quest: ": row[1],
            "Rank: ": row[2],    
            "Stars: ": row[3],        
            "Type: ": row[4],
            "Zenny: ": row[5],
            "item: ": row[6],
        }
        for row in quest_data
    ]    
    return jsonify(quest_list)

    


