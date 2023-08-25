from flask import request, jsonify
from conn import db_connection



#search by name and/or type
def get_tool(lg = 'en',nm = '', ty = ''):
    lang = request.args.get('lang',lg)
    name = request.args.get('name',nm)
    tool_type = request.args.get('tool_type',ty)

    conn = db_connection()
    cursor = conn.cursor()

    query = "SELECT t.id, name, tool_type, slot_1, slot_2, slot_3 FROM tool AS t \
                              JOIN tool_text AS ttx ON t.id = ttx.id \
                              WHERE ttx.lang_id = ?\
                              AND ttx.name LIKE ?\
                              AND t.tool_type LIKE ?"

    cursor.execute(query,(lang,f'%{name}%', f'%{tool_type}%'))
    
    tool_data = cursor.fetchall()

    tool_list = [
        {
            "ID:": row[0],
            "Name:": row[1],
            "Tool Type:": row[2],
            "Slot1:": row[3],
            "Slot2:": row[4],
            "Slot3:": row[5]
        }
        for row in tool_data
    ]

    return jsonify(tool_list)
