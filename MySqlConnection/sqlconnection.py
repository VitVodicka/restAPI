from aiomysql import connect

async def connectToDatabase():

    try:
        conn = await connect(
            host='eu-cdbr-west-03.cleardb.net',
            port=3306,
            user='b851f9ca828e56',
            password='ee570b81',
            db='heroku_1cba10abdc691b6'
        )
        return await conn
    except Exception as e:
        print(e)