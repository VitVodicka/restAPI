from MySqlConnection import sqlconnection
class UserParametrs:
    async def getUserParametrs(self,id,parametr):
        if isinstance(id, int):
            try:

                sqlreturn = await sqlconnection.sqlselectcommand(f"SELECT {parametr} FROM heroku_1cba10abdc691b6.users WHERE (IdUser={id})")
                return {parametr:sqlreturn[0]}#returns json type of return first will be the prpoerty, the second would be what it found


            except Exception as e:
                return {"Error": str(e)}
        else:
            return {"Error": "id is not an integer"}

    async def getUser(self, id: int):
        if isinstance(id, int):
            try:
                sqlreturn = await sqlconnection.sqlselectcommand(f"SELECT * FROM heroku_1cba10abdc691b6.users WHERE (IdUser={id})")
                return {"Id":sqlreturn[0],"Name":sqlreturn[1],"Surname":sqlreturn[2]}

            except Exception as e:
                return {"Error": str(e)}
        else:
            return {"Error": "id is not an integer"}
         #implement here a User
