from bottle_websocket import websocket
import eel
from random import randint
  
eel.init("web")  
  
# Exposing the random_python function to javascript
# @eel.expose    
# def random_python():
#     print("Random function running")
#     return randint(1,100) 
  
# # Start the index.html file 
@eel.expose

def random_python():
    print("Random function running")
random_python() 
#     return randint(1,100) 
# eel.start('index.html')  
eel.start('main.html', block=False, options={'port': 80, 'host': '0.0.0.0', 'close_callback': 'websocketClosed', 'mode': True})
    