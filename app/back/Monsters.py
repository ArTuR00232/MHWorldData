from flask import jsonify, request
from conn import db_connection



#search by name and/or size of the monsters
def get_monster(lg = 'en', nm = '', sz = ''):
    # Get the 'lang','name','size' parameter from the query string
    lang = request.args.get('lang', lg)
    name = request.args.get('name', nm)
    size = request.args.get('size',sz)
    
    conn = db_connection()
    cursor = conn.cursor()

    query = "SELECT mon.id, mont.name, size, weakness_fire, weakness_water, weakness_ice, weakness_thunder, weakness_dragon, weakness_poison, weakness_sleep, weakness_paralysis, weakness_blast, weakness_stun, description FROM monster AS mon\
            JOIN monster_text AS mont ON mon.id = mont.id\
            WHERE mont.lang_id = ? AND mont.name LIKE ? AND mon.size LIKE ?"
    
    cursor.execute(query,(lang, f'%{name}%', f'%{size}%'))
    
    moster_data = cursor.fetchall()
    
    moster_list=[
        {
            "ID:": row[0],
            "Name:": row[1],
            "Size:": row[2],        
            "Fire:": row[3],
            "Water:": row[4],
            "Ice:": row[5],
            "Dragon:": row[6],
            "Poison:": row[7],
            "Sleep:": row[8],
            "Paralyses:": row[9],
            "Blast:": row[10],
            "Stun:": row[11],
            "Description:": row[12]
        }
        for row in moster_data
    ]
    return jsonify(moster_list)


