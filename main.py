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
#testing sql connection
async def connect():
    return await sql_connection.connect_to_database()
@app.post("/v1/users/user/create/{name}/{surname}")#creates user
async def createUser(name:str,surname:str):
    user = user_functions.UsersFunctions()#declaring a user
    return await user.create_user(name, surname)#await=must be used imidietely

@app.get("/v1/users/user/getUser/{id}")#gets user based on id
#@app.get("/v1/users/{id}")#gets user based on id
#if more ids then add array viz. fatapi docs

async def getUser(id:int):
    user = user_parametrs.UserParametrs()
    return await user.getUser(id)

@app.get("/v1/users/user/getUserParametr/{id}/{parameter_value}")#gets userparametrs based on id and parametr
#id behind users
async def getUserParametr(id:int,parameter_value:str):
    user_parametr = user_parametrs.UserParametrs()

    return await user_parametr.getUserParametrs(id,parameter_value)

@app.get("/v1/users/user/getMessages/{id_sender}")#gets messages based on the id of sender
async def getMessages(id_sender:int):
    message = messages_communication.Message()
    return await message.get_message(id_sender)
@app.post("/v1/users/user/sendMessage/{id_sender}/{id_receiver}/{text_message}")#posts a new communication
async def sendMessage(id_sender:int,id_receiver:int,text_message:str):
    try:
        message = messages_communication.Message()
        return await message.send_message(id_sender,id_receiver,text_message)
    except Exception as e:
        return {"Error":e}

@app.get("/v1/users/getAllUsers/")#gets all users
#openanpi document
#same with users but if there is none value
#add doccumetation(PDF)
async def getAllUsers():
    user = user_functions.UsersFunctions()
    return await user.get_all_users()
#look for the endpoints in api
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)