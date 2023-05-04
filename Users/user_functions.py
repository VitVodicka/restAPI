from mySql_connection import sql_connection
from fastapi import HTTPException
class UsersFunctions:
    async def get_all_users(self):
        # select all users from the database
        try:
            sql_dictionary = []
            sql_return = await sql_connection.sql_select_command_multiple_lines(f"SELECT * FROM heroku_1cba10abdc691b6.users")
            # convert the returned results to json
            for i in sql_return:
                help_dictionary ={"ID":i[0],"Name":i[1],"Surname":i[2]}
                sql_dictionary.append(help_dictionary)
            return sql_dictionary

        except Exception as e:
            return {"Error": str(e)}
    async def create_user(self, name:str, surname:str):
        # create a new user in the database with the given name and surname
        try:
            sqlreturn = await sql_connection.sql_insert(f"INSERT INTO heroku_1cba10abdc691b6.users(Name,Surname) VALUES('{name}','{surname}')")
            return sqlreturn


        except (TypeError, ValueError) as e:
            raise HTTPException(status_code=400, detail="TypeError or Value Error:" + e)
        except (KeyError, IndexError) as k:
            raise HTTPException(status_code=404, detail="Not Found:" + k)
        except(IOError) as io:
            raise HTTPException(status_code=500, detail="Internal Server Error:" + io)







