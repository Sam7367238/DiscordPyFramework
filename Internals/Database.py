import aiosqlite
from Internals.Configuration import getConfig

async def queryDatabase(filePath, sql, parameters = None):
    async with aiosqlite.connect(filePath) as db:
        async with db.cursor() as cursor:
            await cursor.execute(sql, parameters)

        await db.commit()

async def fetchDatabase(filePath, sql, parameters = None, fetchMultiple = False):
    async with aiosqlite.connect(filePath) as db:
        async with db.cursor() as cursor:
            await cursor.execute(sql, parameters)

            if fetchMultiple:
                return await cursor.fetchall()
            else:
                return await cursor.fetchone()