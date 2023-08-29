from flask import jsonify,request
from conn import db_connection




#search by name and/or type of the item
def get_armor(lg = 'en',nm = '',ty = ''):
    lang = request.args.get('lang', lg)  # Get the 'lang' parameter from the query string
    name = request.args.get('name', nm)   # Get the 'name' parameter from the query string
    armor_type = request.args.get('type', ty)  # Get the 'type' parameter from the query string
    
    conn = db_connection()
    cursor = conn.cursor()
    
    query = "SELECT armor.id, armor_text.name, defense_base, defense_max, fire, thunder, water, ice, dragon, armor_type FROM armor \
             JOIN armor_text ON armor.id = armor_text.id \
             WHERE armor_text.lang_id = ? AND armor_text.name LIKE ? AND armor.armor_type LIKE ?"
    
    cursor.execute(query, (lang, f'%{name}%', f'%{armor_type}%'))
    
    armor_data = cursor.fetchall()
    
    armor_list = [
        {
            "ID": row[0],
            "Name": row[1],
            "Type": row[2],
            "Defense_base": row[3],
            "Defense_max": row[4],
            "Fire": row[5],
            "Thunder": row[6],
            "Water": row[7],
            "Ice": row[8],
            "Dragon": row[9]
        }
        for row in armor_data
    ]

    return jsonify(armor_list)


