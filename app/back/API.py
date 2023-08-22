import sys

sys.path.append('./app/front/')
#flask to api, front react and electron to .exe
from flask import Flask, jsonify
import Armor, Monsters , Quests, Tools, Item, Kinsect, Weapon,setArmor

app = Flask(__name__)
#app = Flask(__name__, template_folder = '../front')


@app.route('/api/armor', methods = ['GET'])
def get_armor():
    result = Armor.get_armor()
    return (result)

# @app.route('/api/Monster', mothods = ['GET'])
# def getMonster(lang, name = '', size = ''):
#     result = Monsters.monster(lang, name = '', size = '')
#     return jsonify(result)

# @app.route('/api/Quest', mothods = ['GET'])
# def getQuest(lang, monster = '', rank = '', type = '', item = ''):
#     result = Quests.quests(lang, monster = '', rank = '', type = '', item = '')
#     return jsonify(result)

# @app.route('/api/Tool', mothods = ['GET'])
# def getTools(lang,name = '', type = ''):
#     result = Tools.tool(lang,name = '', type = '')
#     return jsonify(result)

# @app.route('/api/Item', mothods = ['GET'])
# def getItem(lang, name = '', category = ''):
#     result = Item.item(lang, name = '', category = '')
#     return jsonify(result)

# @app.route('/api/Kinsect', mothods = ['GET'])
# def getKinsect(lang, name = '', attack = '', dust = ''):
#     result = Kinsect.kinsect(lang, name = '', attack = '', dust = '')
#     return jsonify(result)

# @app.route('/api/Weapon', mothods = ['GET'])
# def getWeapon(lang, name = '', attack = '', dust = ''):
#     result = Weapon.weapon(lang, name = '', attack = '', dust = '')
#     return jsonify(result)

# @app.route('/')
# def home():
#     return 'oi'
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)