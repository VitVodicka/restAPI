from MySqlConnection import sqlconnection


class Message:
    # get message by sender id
    async def getMessage(self, idSender: int):
        # check if idSender is an integer
        if isinstance(idSender, int):
            try:
                # execute sql command to select user with idSender
                sqlreturn = await sqlconnection.sqlselectcommand(
                    f"SELECT * FROM heroku_1cba10abdc691b6.users WHERE (IdUser={idSender})")#TODO a sql command

                # return json with user's information
                return {"Id": sqlreturn[0], "Name": sqlreturn[1], "Surname": sqlreturn[2]}#TODO a json command

            except Exception as e:
                return {"Error": str(e)}
        else:
            return {"Error": "id is not an integer"}

    # send message by sender id, receiver id, and text message
    async def sendMessage(self, idSender: int, idReciver: int, textmessage: str):

        if (isinstance(idSender, int) == True and isinstance(idReciver, int) == True and isinstance(textmessage, str)):

            sqlreturn = await sqlconnection.sqlinsert(
                f"INSERT INTO heroku_1cba10abdc691b6.users(Name,Surname) VALUES('{idSender}','{idReciver}','{textmessage}')")#TODO a sql command

            # return json with sqlreturn value
            return sqlreturn#TODO a return
        else:
            return {"Error:": "Inputed values should be string"}

        return None# TODO