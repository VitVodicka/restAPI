from MySqlConnection import sqlconnection
class UsersFunctions:
    def __init__(self):
        self.conn = sqlconnection.connectToDatabase()

    async def createUser(self,name, surname):

        if (isinstance(name, str) == True and (surname, str) == True):
            try:
                async with self.conn.cursor() as cur:
                    await cur.execute(f"INSERT INTO heroku_1cba10abdc691b6.users(Name,Surname) VALUES({name},{surname}")
                    await self.conn.commit()
                return {"Success":"working createUser"}
            except Exception as e:
                return {"Error":str(e)}
        else:
            return {"Error:":"Inputed values should be string"}
    async def getAllUsers(self):
        return 0





