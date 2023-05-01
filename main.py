# main.py
import asyncio

import aiomysql as aiomysql
import uvicorn
from fastapi import FastAPI

app = FastAPI()


async def connectToDatabase():
    try:
        conn = await aiomysql.connect(
            host='eu-cdbr-west-03.cleardb.net',
            port=3306,
            user='b851f9ca828e56',
            password='ee570b81',
            db='heroku_1cba10abdc691b6'
        )
        return await conn
    except Exception as e:
        print(e)



@app.get("/")
async def connect():
    return await connectToDatabase()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connectToDatabase())
    uvicorn.run(app, host="0.0.0.0", port=8000)