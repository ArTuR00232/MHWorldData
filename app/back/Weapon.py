from flask import request, jsonify
from conn import db_connection


def get_weapon(lg = 'en', nm = '', wty = ''):
    lang = request.args.get('lang', lg)
    name = request.args.get('name', nm)
    weapon_type = request.args.get('weapon_type', wty)

    conn = db_connection()
    cursor = conn.cursor()

    query = "SELECT weapon.id, weapon_text.name, weapon_type  ,attack, attack_true, element1, element1_attack, element2, element2_attack FROM weapon\
                               JOIN weapon_text ON weapon.id = weapon_text.id\
                               WHERE weapon_text.lang_id = ?\
                               AND weapon_text.name LIKE ?\
                               AND weapon.weapon_type  LIKE ?\
                               "
    cursor.execute(query,(lang,f'%{name}%', f'%{weapon_type}%'))

    weapon_data = cursor.fetchall()

    weapon_list = [
            {
                "ID":row[0],
                "Name":row[1],
                "waepon_type": row[2],
                "attack":row[3],
                "true_attack":row[4],
                "Element":row[5],
                "Element_attack":row[6],
                "Element 2":row[7],
                "Element_attack 2":row[8]
            }
            for row in weapon_data
        ]
    return jsonify(weapon_list) 