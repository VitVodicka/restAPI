# main.py
from asyncio import get_event_loop


from mySql_connection import sql_connection;
import uvicorn
from users import user_functions
from user_parametrs import user_parametrs
import message
from fastapi import FastAPI
app = FastAPI()

@app.get("/")#end points of get and post
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


#camelcase to snake_case
async def getUser(id:int):
    user = user_parametrs.UserParametrs()
    return await user.getUser(id)

@app.get("/v1/users/user/getUserParametr/{id}/{parameter_value}")#gets userparametrs based on id and parametr
#id behind users
async def getUserParametr(id:int,parameter_value:str):
    user_parametr = user_parametrs.UserParametrs()

    return await user_parametr.getUserParametrs(id,parameter_value)

@app.get("/v1/users/user/getMessages/{id_Sender}")#gets messages based on the id of sender
async def getMessages(id_sender:int):
    messages = message.messages_communication.Message()
    return await messages.getMessage(id_sender)
@app.post("/v1/users/user/sendMessage/{id_sender}/{id_reciver}/{textMessage}")#posts a new communication
async def sendMessage(id_sender:int,id_reciver:int,text_message:str):
    messages = message.messages_communication.Message()#nastavit autoincrement o 1
    return await messages.send_message(id_sender, id_reciver, text_message)#raise 404 etc. endpoints
#swagger
@app.get("/v1/users/getAllUsers/")#gets all users
#openapi document
#same with users but if there is none value
#add doccumentation(PDF)
async def getAllUsers():
    user = user_functions.UsersFunctions()
    return await user.get_all_users()
#look for the endpoints in api
if __name__ == "__main__":
    #loop = get_event_loop()#makes sure that database will be still connected
    #loop.run_until_complete(connect())
    uvicorn.run(app, host="0.0.0.0", port=8000)