# main.py
from asyncio import get_event_loop

import Message.Messages
from MySqlConnection import sqlconnection;
import uvicorn
from Users import UserFunctions
from userParametrs import UserParametrs
from Message import Messages
from fastapi import FastAPI
app = FastAPI()

@app.get("/")#end points of get and post
#testing sql connection
async def connect():
    return await sqlconnection.connectToDatabase()
@app.post("/v1/users/user/create/{name}/{surname}")#creates user
async def createUser(name:str,surname:str):
    user = UserFunctions.UsersFunctions()#declaring a user
    return await user.createUser(name,surname)#await=must be used imidietely

@app.get("/v1/users/user/getUser/{id}")#gets user based on id
async def getUser(id:int):
    user = UserParametrs.UserParametrs()
    return await user.getUser(id)
    
@app.get("/v1/users/user/getUserParametr/{id}/{parameter_value}")#gets userparametrs based on id and parametr
async def getUserParametr(id:int,parameter_value:str):
    user_parametr = UserParametrs.UserParametrs()

    return await user_parametr.getUserParametrs(id,parameter_value)

@app.get("/v1/users/user/getMessages/{id_Sender}")#gets messages based on the id of sender
async def getMessages(id_Sender:int):
    messages = Message.Messages.Message()
    return await messages.getMessage(id_Sender)
@app.post("/v1/users/user/sendMessage/{id_sender}/{id_reciver}/{textMessage}")#posts a new communication
async def sendMessage(id_sender:int,id_reciver:int,textMessage:str):
    messages = Message.Messages.Message()
    return await messages.sendMessage(id_sender,id_reciver,textMessage)

@app.get("/v1/users/getAllUsers/")#gets all users
async def getAllUsers():
    user = UserFunctions.UsersFunctions()
    return await user.getAllUsers()

if __name__ == "__main__":
    loop = get_event_loop()#makes sure that database will be still connected
    loop.run_until_complete(connect())
    uvicorn.run(app, host="0.0.0.0", port=8000)