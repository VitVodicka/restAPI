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


async def sqlselectcommand(command):
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
        await cursor.execute(command)
        try:
        # fetch all results
            r = await cursor.fetchone()#finds list of resaults
            if(r is None):
                return{"Error 404 ":"not found"}
        except Exception as e:
            return {"Error":str(e)}
        # detach cursor from connection
        await cursor.close()

        # close connection
        conn.close()
        return r
    except Exception as e:
        print(e)

async def sqlselectcommandMultipleLines(command):
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
        await cursor.execute(command)
        try:
        # fetch all results
            r = await cursor.fetchall()#finds list of resaults
            if(r is None):
                return{"Error 404 ":"not found"}

        except Exception as e:
            return {"Error":str(e)}
        # detach cursor from connection
        await cursor.close()

        # close connection
        conn.close()
        return r
    except Exception as e:
        print(e)

