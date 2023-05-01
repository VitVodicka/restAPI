from MySqlConnection import sqlconnection
class Message:
    def __init__(self):
        self.conn = sqlconnection.connectToDatabase()
    async def getMessage(self,idSender):
        return
    async def sendMessage(self,idSender,idReciver):
        return