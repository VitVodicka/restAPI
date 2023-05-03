from MySqlConnection import sqlconnection
class UsersFunctions:
    async def getAllUsers(self):
        # select all users from the database
        try:
            sqldictionary = []
            sqlreturn = await sqlconnection.sqlselectcommandMultipleLines(f"SELECT * FROM heroku_1cba10abdc691b6.users")
            # convert the returned results to json
            for i in sqlreturn:
                help_dictionary ={"ID":i[0],"Name":i[1],"Surname":i[2]}
                sqldictionary.append(help_dictionary)
            return sqldictionary

        except Exception as e:
            return {"Error": str(e)}
    async def createUser(self,name:str, surname:str):
        # create a new user in the database with the given name and surname
        if (isinstance(name, str) == True and isinstance(surname, str) == True):
            sqlreturn = await sqlconnection.sqlinsert(f"INSERT INTO heroku_1cba10abdc691b6.users(Name,Surname) VALUES('{name}','{surname}')")
            return sqlreturn

        else:
            return {"Error:":"Inputed values should be string"}







