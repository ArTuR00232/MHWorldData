#future work make an new table to user crate and save the presets 
import sqlite3


#connection with the data base
conn = sqlite3.connect("mhw.db")

#create an object
class setArmor:
    def __init__(self, head = '',chest = '', arms = '', waist = '', legs = '', weapon = '', charm = ''):
        self.head = head
        self.chest = chest
        self.arms = arms
        self.waist = waist
        self.legs = legs
        self.weapon = weapon 
        self.charm = charm 


    #section to adding each part of the set
    def setHead(self, head):
        if(head[1] == 'head'):
            self.head = head[0]
        else:
            print('nn')
    def setChest(self, chest):
        if(chest[1] == 'chest'):
            self.chest = chest
        else:
            print('nn')
    def setArms(self, arms):
        if(arms[1] == 'arms'):        
            self.arms = arms
        else:
            print('nn')
    def setWaist(self, waist):
        if(waist[1] == 'waist'):            
            self.waist = waist
        else:   
            print('nn')
    def setLegs(self, legs):
        if(legs[1] == 'legs'):        
            self.legs = legs
        else:
            print('nn')   
    def setWeapon(self, weapon):
        if(weapon[1] == 'weapon'):           
            self.weapon = weapon
        else:
            print('nn')
    def setCharm(self, charm):
        if(charm[1] == 'charm'):
            self.charm = charm
        else:
            print('nn')    

    #print(all preset armor)
    def setComplete(self):
        print(self.head)
        print(self.chest)
        print(self.arms)
        print(self.waist)
        print(self.legs)
        print(self.weapon)
        print(self.charm)



# head = Armor.armor('pt','Orelhas Serperianas α+','head')
# chest = Armor.armor('pt','artemis mail','chest')
# arms = Armor.armor('pt','artemis guards','arms')
# waist = Armor.armor('pt','artemis coil','waist')
# legs = Armor.armor('pt','artemis greaves','legs')

# armor = setArmor()
# armor.setHead(head)
# armor.setChest(chest)
# armor.setArms(arms)
# armor.setWaist(waist)
# armor.setLegs(legs)
# armor.setComplete()
