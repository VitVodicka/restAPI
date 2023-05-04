# main.py
from asyncio import get_event_loop

from mySql_connection import sql_connection;
import uvicorn
from users import user_functions
from user_parametrs import user_parametrs
from message import messages_communication
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def connect():
    """
    Tests SQL connection and return connection status.

    Returns:
        Success: "202" if successful.
    """
    return await sql_connection.connect_to_database()

@app.post("/v1/users/create/{name}/{surname}")
async def createUser(name: str, surname: str):
    """
    Create a new user with the given name and surname.
    parametrs:
        name (str): The user's name.
        surname (str): The user's surname.

    Returns:
        json: A json containing the new user's ID and name.
    """
    user = user_functions.UsersFunctions()
    return await user.create_user(name, surname)

@app.get("/v1/users/{id}")
async def getUser(id: int):
    """
    Retrieve user information based on user id.
    Parametrs:
        id (int): The id of the user to retrieve.

    Returns:
        json: A json containing the user s name, surname, and ID.
    """
    user = user_parametrs.UserParametrs()
    return await user.getUser(id)

@app.get("/v1/users/{id}/getUserParametr/{parameter_value}")
async def getUserParametr(id: int, parameter_value: str):
    """
    Retrieve user parameters based on ID and parameter value.

    Parameters:
        id (int): The id of the user to retrieve parameters for.
        parameter_value (str): The parameter to retrieve.

    Returns:
        json: A json containing the user s ID, parameter name, and parameter value.
    """
    user_parametr = user_parametrs.UserParametrs()
    return await user_parametr.getUserParametrs(id, parameter_value)

@app.get("/v1/users/{id}/getMessages/{id_sender}")
async def getMessages(id_sender: int):
    """
    Retrieve messages sent by the user with the given ID.

    Parameters:
        id_sender (int): The ID of the user to retrieve messages for.

    Returns:
        json: A json of dictionaries containing the message ID, sender ID, receiver ID, and message text.
    """
    message = messages_communication.Message()
    return await message.get_message(id_sender)

@app.post("/v1/users/sendMessage/{id_sender}/{id_receiver}/{text_message}")
async def sendMessage(id_sender: int, id_receiver: int, text_message: str):
    """
    Send a new message from the user with the given ID to the user with the given receiver id.

    Parameters:
        id_sender (int): The ID of the user sending the message.
        id_receiver (int): The ID of the user receiving the message.
        text_message (str): The text of the message.

    Returns:
        json: A dictionary containing the new message s id, sender id, receiver id, and message text.
    """
    try:
        message = messages_communication.Message()
        return await message.send_message(id_sender, id_receiver, text_message)
    except Exception as e:
        return {"Error": e}

@app.get("/v1/users/")
async def getAllUsers():
    """
    Retrieve all users.

    Returns:
        list: A list of jsons containing each user's ID, name, and surname.
    """
    user = user_functions.UsersFunctions()
    return await user.get_all_users()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)