from aiomysql import connect
from fastapi import HTTPException
import json

async def connect_to_database():#does it asynchronously based on the program=can be done during programme
    # Establishes connection to the database
    try:
        with open('config_database/config.json') as f:
            connection=json.load(f)
        conn = await connect(
            host=connection["host"],
            port=connection["port"],
            user=connection["user"],
            password=connection["password"],
            db=connection["db"]
        )

        return conn
    except (KeyError, IndexError) as k:
        raise HTTPException(status_code=404, detail="Not Found:" + k)
        return None
    except(IOError) as io:
        raise HTTPException(status_code=500, detail="Internal Server Error:" + io)
        return None



async def sql_select_command(command):
    try:
        with open('config_database/config.json') as f:
            connection = json.load(f)
        conn = await connect(
            host=connection["host"],
            port=connection["port"],
            user=connection["user"],
            password=connection["password"],
            db=connection["db"]
        )

        cursor = await conn.cursor()

        # execute sql query
        await cursor.execute(command)

        # fetch all results
        r = await cursor.fetchone()#finds resault

        # detach cursor from connection
        await cursor.close()
        if(r==None):
            raise HTTPException(status_code=404, detail="Not Found:")
        # close connection
        conn.close()
        return await r

    except (KeyError, IndexError) as k:
        raise HTTPException(status_code=404, detail="Not Found:" + k)
        return None
    except(IOError) as io:
        raise HTTPException(status_code=500, detail="Internal Server Error:" + io)
        return None

async def sql_select_command_multiple_lines(command):

    try:
        with open('config_database/config.json') as f:
            connection = json.load(f)
        conn = await connect(
            host=connection["host"],
            port=connection["port"],
            user=connection["user"],
            password=connection["password"],
            db=connection["db"]
        )

        cursor = await conn.cursor()

        # execute sql query
        await cursor.execute(command) #creates a new  object which allows to interact with the database
        try:
        # fetch all results
            r = await cursor.fetchall()#finds list of resaults
            if(r is None):
                raise HTTPException(status_code=404, detail="Not Found")
                return None
            return r
        except Exception as e:
            return {"Error":str(e)}#more specific exceptions
        # detach cursor from connection
        await cursor.close()

        # close connection
        conn.close()
        return r
    except (KeyError, IndexError) as k:
        raise HTTPException(status_code=404, detail="Not Found:" + k)
        return None
    except(IOError) as io:
        raise HTTPException(status_code=500, detail="Internal Server Error:" + io)
        return None

async def sql_insert(command):
    # Executes a SQL insert command on the database
    try:
        with open('config_database/config.json') as f:
            connection = json.load(f)
        conn = await connect(
            host=connection["host"],
            port=connection["port"],
            user=connection["user"],
            password=connection["password"],
            db=connection["db"]
        )

        cursor = await conn.cursor()

        # execute sql query
        await cursor.execute(command)

        await conn.commit()#commit updates value on SQL COMMANDS except SELECT(INSERT,UPDATE...)
        # detach cursor from connection
        await cursor.close()

        # close connection
        conn.close()
        return {"Success":200}
    except (KeyError, IndexError) as k:
        raise HTTPException(status_code=404, detail="Not Found:" + k)
        return None
    except(IOError) as io:
        raise HTTPException(status_code=500, detail="Internal Server Error:" + io)
        return None
