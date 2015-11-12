# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
class State(object):
    def send_message(self):
        print("A classe deve implementar do something")
    
class Connected(State):
    def send_message(self):
        print ("Usuario Conectado")

class Disconnected(State):
    def send_message(self):
        print ("Nao foi possivel conectar")


