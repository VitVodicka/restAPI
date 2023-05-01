from MySqlConnection import sqlconnection
class UserParametrs:
    def __init__(self):
        self.conn = sqlconnection.connectToDatabase()
    async def getUser(self,id):
        return #implement here a User
    async def getUserParamaetrs(self,id,parametr):
        return #paramaetr and TODO