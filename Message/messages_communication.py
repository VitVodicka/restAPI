from mySql_connection import sql_connection
from fastapi import  HTTPException


class Message:
    # get message by sender id
    async def get_message(self, id_sender: int):
        # check if idSender is an integer
        try:

                # execute sql command to select user with idSender
                sql_return = await sql_connection.sql_select_command(
                    f"SELECT * FROM heroku_1cba10abdc691b6.communications WHERE idSender={id_sender}")
                # return json with user's information
                return {"id_communication": sql_return[0], "id_sender": sql_return[1], "id_reciver": sql_return[2],"text_message":sql_return[3]}#TODO a JSOn


        except (TypeError, ValueError) as e:
            raise HTTPException(status_code=400, detail="TypeError or Value Error:" + e)
        except (KeyError, IndexError) as k:
            raise HTTPException(status_code=404, detail="Not Found:" + k)
        except(IOError) as io:
            raise HTTPException(status_code=500, detail="Internal Server Error:" + io)

    # send message by sender id, receiver id, and text message
    async def send_message(self, id_sender: int, id_reciver: int, text_message: str):

        try:

            sql_return = await sql_connection.sql_insert(
                f"INSERT INTO heroku_1cba10abdc691b6.communications(idSender,idReciver,textMessage) VALUES({id_sender},{id_reciver},'{text_message}')")
            return sql_return
            # return json with sql_return value

        except (TypeError, ValueError) as e:
            raise HTTPException(status_code=400,detail="TypeError or Value Error:"+e)
        except (KeyError, IndexError) as k:
            raise HTTPException(status_code=404,detail="Not Found:"+k)
        except(IOError) as io:
            raise HTTPException(status_code=500,detail="Internal Server Error:"+io)





