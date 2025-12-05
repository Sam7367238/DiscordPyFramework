import asyncio
from Internals.Configuration import initialize
from Internals.Database import queryDatabase
from colorama import Back, Fore, Style


# Run this file by itself and it will set up your database.


setupSQL = """
CREATE TABLE IF NOT EXISTS Users (
    ID INT NOT NULL PRIMARY KEY,
    Money INT
);
"""





async def main():
    await queryDatabase("../AppDatabase.db", setupSQL)

    prfx = (
            Back.GREEN +
            Fore.LIGHTWHITE_EX +
            "SUCCESS" +
            Back.RESET +
            Fore.WHITE +
            Style.BRIGHT
    )

    print(prfx + Fore.LIGHTWHITE_EX + " Successfully Set Up Database")

if __name__ == "__main__":
    initialize("../configuration.json")
    asyncio.run(main())