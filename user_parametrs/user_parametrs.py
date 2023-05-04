from mySql_connection import sql_connection
from fastapi import HTTPException
class UserParametrs:
    async def getUserParametrs(self,id,parametr):
        try:

            # execute a SQL SELECT command to get a specific parameter for a user
            sql_return = await sql_connection.sql_select_command(f"SELECT {parametr} FROM heroku_1cba10abdc691b6.users WHERE (IdUser={id})")
            return {parametr:sql_return[0]}#returns json type of return first will be the prpoerty, the second would be what it found


        except (TypeError, ValueError) as e:

            raise HTTPException(status_code=400, detail="TypeError or Value Error:" + e)

        except (KeyError, IndexError) as k:

            raise HTTPException(status_code=404, detail="Not Found:" + k)

        except(IOError) as io:

            raise HTTPException(status_code=500, detail="Internal Server Error:" + io)

    async def getUser(self, id: int):

            try:
                # execute a SQL SELECT command to get all user data for a specific user
                sql_return = await sql_connection.sql_select_command(f"SELECT * FROM heroku_1cba10abdc691b6.users WHERE (IdUser={id})")
                return {"Id":sql_return[0],"Name":sql_return[1],"Surname":sql_return[2]}

            except (TypeError, ValueError) as e:

                raise HTTPException(status_code=400, detail="TypeError or Value Error:" + e)

            except (KeyError, IndexError) as k:

                raise HTTPException(status_code=404, detail="Not Found:" + k)

            except(IOError) as io:

                raise HTTPException(status_code=500, detail="Internal Server Error:" + io)

