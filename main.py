# main.py
import asyncio

from MySqlConnection import sqlconnection;
import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def connect():
    return await sqlconnection.connectToDatabase()
@app.post("/v1/users/user/create")
async def createUser():
    return await sqlconnection.connectToDatabase()
@app.get("/v1/users/user/getUser/")#missing the numbers after getUSer
async def getUser():
    return await sqlconnection.connectToDatabase()
@app.get("/v1/users/user/getUserParametr/")#missing the numbers after getUserParametr and missing parametr
async def getUserParametr():
    return await sqlconnection.connectToDatabase()
@app.get("/v1/users/user/getMessages/")#missing parametr
async def getMessages():
    return await sqlconnection.connectToDatabase()
@app.post("/v1/users/user/sendMessage/")#missing send message parametr
async def sendMessage():
    return await sqlconnection.connectToDatabase()
@app.get(" /v1/users/getAllUsers/")#missing parametr
async def getAllUsers():
    return await sqlconnection.connectToDatabase()


if __name__ == "__main__":
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(connectToDatabase())
    uvicorn.run(app, host="0.0.0.0", port=8000)