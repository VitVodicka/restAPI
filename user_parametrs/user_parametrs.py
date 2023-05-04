from mySql_connection import sql_connection
class UserParametrs:
    async def getUserParametrs(self,id,parametr):
        if isinstance(id, int):#check if it is integer
            try:
                # execute a SQL SELECT command to get a specific parameter for a user
                sql_return = await sql_connection.sql_select_command(f"SELECT {parametr} FROM heroku_1cba10abdc691b6.users WHERE (IdUser={id})")
                return {parametr:sql_return[0]}#returns json type of return first will be the prpoerty, the second would be what it found


            except Exception as e:
                return {"Error": str(e)}
        else:
            return {"Error": "id is not an integer"}

    async def getUser(self, id: int):
        if isinstance(id, int):
            try:
                # execute a SQL SELECT command to get all user data for a specific user
                sql_return = await sql_connection.sql_select_command(f"SELECT * FROM heroku_1cba10abdc691b6.users WHERE (IdUser={id})")
                return {"Id":sql_return[0],"Name":sql_return[1],"Surname":sql_return[2]}

            except Exception as e:
                return {"Error": str(e)}#look for possible exceptions
        else:
            return {"Error": "id is not an integer"}#raise http exception

