from flask import jsonify, request
from conn import db_connection

#search charm by name
def get_charm(lg = 'en', nm = ''):
    lang = request.args.get('lang',lg)
    name = request.args.get('name',nm)

    conn = db_connection()
    cursor = conn.cursor()

    query= "SELECT c.id, ct.name, c.rarity, sktx.description,COALESCE(c.previous_id,'N/A'),\
                            CASE WHEN c.previous_id == 'N/A' THEN 'N/A'\
                                ELSE c.previous_id END as previous_name\
                             FROM charm AS c \
                            JOIN charm_text AS ct ON c.id = ct.id \
                            JOIN charm_skill AS cs ON c.id = cs.charm_id\
                            JOIN skilltree AS skt ON cs.skilltree_id = skt.id\
                            JOIN skilltree_text AS sktx ON skt.id = sktx.id\
                            WHERE ct.lang_id == ?\
                            AND ct.name LIKE ?\
                            AND ct.lang_id = ?\
                            AND sktx.lang_id = ?\
                            "
    
    cursor.execute(query,(lang,f'%{name}%',lang, lang))
    charm_data = cursor.fetchall()

    charm_list = [
            {
                "ID:": row[0],
                "Name:": row[1],
                "Rarity:": row[2],
                "skill": row[3],
                "previous_id": row[4],
                "previous_name": row[5]
            }
            for row in charm_data
        ]
    return jsonify(charm_list)

#search decoration by name
def get_Decoration(lg = 'en', nm = ''):
    lang = request.args.get('lang',lg)
    name = request.args.get('name',nm)
    
    conn = db_connection()
    cursor = conn.cursor()
    query = "SELECT dect.id, dect.name AS named, stx.name,dec.rarity, max_level, description FROM decoration AS dec \
                                   JOIN decoration_text AS dect ON dec.id = dect.id \
                                   LEFT JOIN skilltree AS st ON st.id = dec.skilltree_id \
                                   LEFT JOIN skilltree_text AS  stx ON stx.id = dec.skilltree_id \
                                   WHERE dect.lang_id == ?\
                                   AND dect.name LIKE ?\
                                   AND stx.lang_id = ?"
    
    cursor.execute(query,(lang, f'%{name}%', lang))
    decoration_data = cursor.fetchall()
    
    decoration_list = [
            {
                "ID:": row[0],
                "Name:": row[1],
                "Name Skill:": row[2],
                "Rarity:": row[3],
                "max_level:": row[4],
                "Description:": row[5]
            }
            for row in decoration_data
        ]
    return jsonify(decoration_list)