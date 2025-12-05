import discord
import aiosqlite
    
async def DBRegistered(member):
  async with aiosqlite.connect("AppDatabase.db") as db:
    async with db.cursor() as cursor:
      await cursor.execute(f"SELECT User_ID FROM Statistics WHERE User_ID = ?", (member.id,))
      row = await cursor.fetchone()
      if row == None:
        return False
      else:
        return True

async def get_columns(table):
  async with aiosqlite.connect("AppDatabase.db") as db:
    async with db.cursor() as cursor:
      await cursor.execute(f"PRAGMA table_info({table})")
      columns = await cursor.fetchall()
      return [column[1] for column in columns]

async def getStat(member, stat: str, returnType: str = "int"):
  async with aiosqlite.connect("AppDatabase.db") as db:
    async with db.cursor() as cursor:
      await cursor.execute(f'''SELECT {stat} FROM Statistics WHERE User_ID = ?''', (member.id,))
      fetch = await cursor.fetchone()
      if returnType == "int":
        return int(fetch[0])
      elif returnType == "str":
        return str(fetch[0])

async def setStat(member, stat: str, new: any):
  async with aiosqlite.connect("AppDatabase.db") as db:

    async with db.cursor() as cursor:
      await cursor.execute(f'''SELECT {stat} FROM Statistics WHERE User_ID = ?''', (member.id,))
      fetch = await cursor.fetchone()

      statistic = fetch[0]

      sql = (f"UPDATE Statistics SET {stat} = ? WHERE User_ID = ?")
      val = (new, member.id)
      await cursor.execute(sql, val)
      
    await db.commit()

async def removeStat(member, stat, amount: int):
  async with aiosqlite.connect("AppDatabase.db") as db:
    async with db.cursor() as cursor:
      await cursor.execute(f'''SELECT {stat} FROM Statistics WHERE User_ID = ?''', (member.id,))
      statistic = await cursor.fetchone()
      fetched = statistic[0]

      if fetched < amount:
        sql = (f"UPDATE Statistics SET {stat} = ? WHERE User_ID = ?")
        val = (0, member.id)
        await cursor.execute(sql, val)
      else:
        sql = (f"UPDATE Statistics SET {stat} = ? WHERE user_id = ?")
        val = (fetched - amount, member.id)
        await cursor.execute(sql, val)
      
    await db.commit()
  
async def addStat(member, stat, amount: int):
  async with aiosqlite.connect("AppDatabase.db") as db:
    async with db.cursor() as cursor:
      await cursor.execute(f'''SELECT {stat} FROM Statistics WHERE User_ID = ?''', (member.id,))
      statistic = await cursor.fetchone()
      fetched = statistic[0]

      sql = (f"UPDATE Statistics SET {stat} = ? WHERE user_id = ?")
      val = (fetched + amount, member.id)
      await cursor.execute(sql, val)
      
    await db.commit()
