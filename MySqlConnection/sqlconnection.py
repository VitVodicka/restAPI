from aiomysql import connect,cursors

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


async def connectToDatabase2():
    try:
        conn = await connect(
            host='eu-cdbr-west-03.cleardb.net',
            port=3306,
            user='b851f9ca828e56',
            password='ee570b81',
            db='heroku_1cba10abdc691b6'
        )
        cursor = await conn.cursor()

        # execute sql query
        await cursor.execute("SELECT * FROM heroku_1cba10abdc691b6.users WHERE (IdUser=11)")

        # fetch all results
        r = await cursor.fetchone()
        # detach cursor from connection
        await cursor.close()

        # close connection
        conn.close()
        return r
    except Exception as e:
        print(e)