from aiomysql import connect,cursors

async def connectToDatabase():#does it asynchronously based on the program=can be done during programme
    # Establishes connection to the database
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
            r = await cursor.fetchone()#finds resault
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
        await cursor.execute(command) #creates a new  object which allows to interact with the database
        try:
        # fetch all results
            r = await cursor.fetchall()#finds list of resaults
            if(r is None):
                return{"Error 404 ":"not found"}

        except Exception as e:
            return {"Error":str(e)}#more specific exceptions
        # detach cursor from connection
        await cursor.close()

        # close connection
        conn.close()
        return r
    except Exception as e:
        print(e)

async def sqlinsert(command):
    # Executes a SQL insert command on the database
    try:

        conn = await connect(#host, ports etc. config in file
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
            await conn.commit()#commit updates value on SQL COMMANDS except SELECT(INSERT,UPDATE...)
        except Exception as e:
            return {"Error":str(e)}
        # detach cursor from connection
        await cursor.close()

        # close connection
        conn.close()
        return {"Success":202}
    except Exception as e:
        return {"Failure":str(e)}
