from MySqlConnection import sqlconnection
class UserParametrs:
    def __init__(self):

        try:
            self.conn = sqlconnection.connectToDatabase()

        except Exception as e:
            return e

    async def getUser(self, id: int):
        parameters =sqlconnection.connectToDatabase2()
        return parameters

        """if isinstance(id, int):
            try:

                async with self.conn.cursor() as cur:
                    await cur.execute(f"SELECT * FROM heroku_1cba10abdc691b6.users WHERE (IdUser={id})")
                    await self.conn.commit()
                    return {"Working"}
            except Exception as e:
                return {"Error": str(e)}
        else:
            return {"Error": "id is not an integer"}
         #implement here a User"""
    async def getUserParamaetrs(self,id,parametr):
        return #paramaetr and TODO