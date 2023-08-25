
from flask import request, jsonify
from conn import db_connection

#subcategory?

#serch by name, category
def get_item(lg ='en', cty = ''):
    lang = request.args.get('lang',lg)
    #subcategory = request.args.get('subcategory',scty)
    category = request.args.get('category',cty)

    conn = db_connection()
    cursor = conn.cursor()

    query = "SELECT i.id, ittx.name, i.category, i.subcategory,i.sell_price, ittx.description FROM item AS i\
                                 JOIN item_text AS ittx ON i.id = ittx.id\
                                 WHERE ittx.lang_id = ?\
                                 AND i.category LIKE ?\
                                 "
    cursor.execute(query,(lang, f'%{category}%'))
    item_data = cursor.fetchall()

    item_list = [
            {
                "ID":row[0],
                "Name":row[1],
                "category":row[2],
                "subcategory":row[3],
                "sell_price":row[4],
                "Description":row[5]
            }
            for row in item_data
        ]
    return jsonify(item_list)