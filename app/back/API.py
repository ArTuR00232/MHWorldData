import sys

sys.path.append('./app/front/')
#flask to api, front react and electron to .exe
from flask import Flask, jsonify
import Armor, Monsters , Quests, Tools, ItemCombination, Item, Kinsect, Weapon,setArmor, CharmDecoration

app = Flask(__name__)
#app = Flask(__name__, template_folder = '../front')


@app.route('/api/armor', methods = ['GET'])
def get_armor():
    result = Armor.get_armor()
    return (result)

@app.route('/api/monster', methods = ['GET'])
def get_Monster():
    result = Monsters.get_monster()
    return (result)

@app.route('/api/quest', methods = ['GET'])
def get_Quest():
    result = Quests.get_quests()
    return (result)

@app.route('/api/tool', methods = ['GET'])
def get_Tools():
    result = Tools.get_tool()
    return (result)


@app.route('/api/item', methods = ['GET'])
def get_Item():
    result = Item.get_item()
    return (result)

@app.route('/api/item_combination', methods = ['GET'])
def get_ItemCombination():
    result = ItemCombination.get_itemcombination()
    return (result)

@app.route('/api/kinsect', methods = ['GET'])
def get_Kinsect():
    result = Kinsect.get_kinsect()
    return(result)

@app.route('/api/weapon', methods = ['GET'])
def get_Weapon():
    result = Weapon.get_weapon()
    return (result)

@app.route('/api/charm', methods = ['GET'])
def get_Charm():
    result = CharmDecoration.get_charm()
    return (result)

@app.route('/api/decoration', methods = ['GET'])
def get_decoration():
    result = CharmDecoration.get_Decoration()
    return(result)



if __name__ == '__main__':
    app.run(debug=True)