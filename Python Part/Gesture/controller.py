"""
from main import Gesture
from data import DataManager

app_id = 1
app = Gesture(app_id)

manager = DataManager()

app.train(manager.folders,manager.names,manager.labels)	
#print len(app.features[0])
app.initClassifier()


test = app.getDataFromFile("./dataset/circle/one.txt")
print manager.folders[app.predict(test)-1]
print app.predict(test)
app.plotImage("./dataset/circle/one.txt")"""

from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()


def fun(inp):
    if(inp==4):
        k.tap_key(k.space)
    elif(inp==3):
        k.press_key(k.alt_key)
        k.tap_key(k.right_key,n=8)
        k.release_key(k.alt_key)
    elif(inp==2):
        k.press_keys([k.windows_l_key,'d'])
    else:
        k.press_key(k.alt_key)
        k.tap_key(k.left_key,n=8)
        k.release_key(k.alt_key)
        
