
from flask import request, jsonify
from conn import db_connection

#serch by name, category
def get_itemcombination(lg ='en', nm = '', cty = ''):
    lang = request.args.get('lang',lg)
    name = request.args.get('name',nm)
    category = request.args.get('category',cty)

    conn = db_connection()
    cursor = conn.cursor()

    query = "SELECT it.name AS result, it2.name AS item1,it3.name AS item2, it.description FROM item_combination AS ic\
                                 JOIN item AS i ON i.id = ic.result_id\
                                 JOIN item AS i1 ON i1.id = ic.first_id \
                                 JOIN item AS i2 ON i2.id = ic.second_id\
                                 JOIN item_text AS it ON it.id = ic.result_id\
                                 JOIN item_text AS it2 ON i1.id = it2.id\
                                 JOIN item_text AS it3 ON i2.id = it3.id\
                                 WHERE it.lang_id = ?\
                                 AND it2.lang_id = ?\
                                 AND it3.lang_id = ?\
                                 AND i.category LIKE ?\
                                 "
    cursor.execute(query,(lang, lang, lang, f'%{category}%'))
    item_data = cursor.fetchall()

    item_list = [
            {
                "Name result":row[0],
                "Name item1":row[1],
                "Name item2":row[2],
                "Description":row[3]
            }
            for row in item_data
        ]
    return jsonify(item_list)