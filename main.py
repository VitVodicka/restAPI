# main.py
from asyncio import get_event_loop
from MySqlConnection import sqlconnection;
import uvicorn
from Users import UserFunctions
from userParametrs import UserParametrs
from Message import Messages
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def connect():
    return await sqlconnection.connectToDatabase()
@app.post("/v1/users/user/create")
async def createUser(name,surname):
    return await UserFunctions.UsersFunctions.createUser(name,surname)

@app.get("/v1/users/user/getUser/{id}")
async def getUser(id:int):
    user = UserParametrs.UserParametrs()
    return await user.getUser(id)


    
@app.get("/v1/users/user/getUserParametr/{id}/{parameter_value}")#missing the numbers after getUserParametr and missing parametr
async def getUserParametr(id:int,parameter_value:str):
    user_parametr = UserParametrs()

    return await user_parametr.getUserParametrs(id,parameter_value)
"""
@app.get("/v1/users/user/getMessages/")#missing parametr
async def getMessages():
    return await Messages.Message.getMessage(idSender)
@app.post("/v1/users/user/sendMessage/")#missing send message parametr
async def sendMessage():
    return await Messages.Message.sendMessage(idSender,idReciver)
"""
@app.get("/v1/users/getAllUsers/")
async def getAllUsers():
    user = UserFunctions()#cannot fiund UseFunctions
    return await user.getAllUsers()



if __name__ == "__main__":
    loop = get_event_loop()
    loop.run_until_complete(connect())
    uvicorn.run(app, host="0.0.0.0", port=8000)