from MySqlConnection import sqlconnection
class UsersFunctions:
    async def getAllUsers(self):

        try:
            sqlreturn = await sqlconnection.sqlselectcommand(f"SELECT * FROM heroku_1cba10abdc691b6.users")
            return {"Id": sqlreturn[0], "Name": sqlreturn[1], "Surname": sqlreturn[2]}

        except Exception as e:
            return {"Error": str(e)}
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







