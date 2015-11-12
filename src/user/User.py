from state import State


class User(object):
    __desconectado = State.Disconnected()
    __conectado = State.Connected()
    __estado = __desconectado
    __login = ""
    __password = ""

    def __init__(self,login,password):
        User.__login = login
        User.__password = password            
    
    def get_login(self):
        return User.__login
            
    def get_password(self):
        return self.User.__password

    def send_message(self):
        User.__estado.send_message()
    
    def set_state(self,estado):
        User.__estado = estado
    
    def get_state(self):
        return __estado
    
    def get_connected(self):
        return User.__conectado
    
    def print_all(self):
        print (User.__login)
        print (User.__password)
        