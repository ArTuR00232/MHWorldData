from flask import request, jsonify
from conn import db_connection


#serch by name, type attack, dust efect
def get_kinsect(lg = 'en', nm = '', atty = '', dt = ''):
    lang = request.args.get('lang',lg)
    name = request.args.get('name',nm)
    attack_type = request.args.get('attack',atty)
    dust = request.args.get('dust',dt)

    conn = db_connection()
    cursor = conn.cursor()

    query = "SELECT k.id,name,attack_type, dust_effect, power, speed, heal FROM kinsect as k\
                             JOIN kinsect_text AS kt ON k.id = kt.id\
                             WHERE kt.lang_id = ?\
                             AND kt.name LIKE ?\
                             AND k.attack_type LIKE ?\
                             AND k.dust_effect LIKE ?\
                             "
    cursor.execute(query,(lang, f'%{name}%', f'%{attack_type}%', f'%{dust}%'))
    kinsect_data = cursor.fetchall()

    kinsect_list =[
        {
            "ID":row[0],
            "Name":row[1],
            "Attack_Type":row[2],
            "Dust_Effect":row[3],
            "Power":row[4],
            "Speed":row[5],
            "Heal":row[6]
        }
        for row in kinsect_data
    ]

    return jsonify(kinsect_list)

    