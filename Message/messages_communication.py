from mySql_connection import sql_connection


class Message:
    # get message by sender id
    async def get_message(self, id_sender: int):
        # check if idSender is an integer
        if isinstance(id_sender, int):
            try:
                #change heroku to property
                # execute sql command to select user with idSender
                sql_return = await sql_connection.sql_select_command(
                    f"SELECT * FROM heroku_1cba10abdc691b6.users WHERE (IdUser={id_sender})")#TODO a sql command

                # return json with user's information
                return {"Id": sql_return[0], "Name": sql_return[1], "Surname": sql_return[2]}#TODO a json command

            except Exception as e:
                return {"Error": str(e)}
        else:
            return {"Error": "id is not an integer"}

    # send message by sender id, receiver id, and text message
    async def send_message(self, id_sender: int, id_reciver: int, text_message: str):

        if (isinstance(id_sender, int) == True and isinstance(id_reciver, int) == True and isinstance(text_message, str)):

            sql_return = await sql_connection.sql_insert(
                f"INSERT INTO heroku_1cba10abdc691b6.users(Name,Surname) VALUES('{id_sender}','{id_reciver}','{text_message}')")#TODO a sql command

            # return json with sql_return value
            return sql_return#TODO a return
        else:
            return {"Error:": "Inputed values should be string"}

        return None# TODO