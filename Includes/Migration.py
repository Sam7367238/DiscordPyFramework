import asyncio
from Internals.Configuration import initialize
from Internals.Database import queryDatabase
from colorama import Back, Fore, Style
import time





migrationSQL = """
CREATE TABLE IF NOT EXISTS Users (
    ID INT NOT NULL PRIMARY KEY,
    Money INT
);
"""





async def main():
    await queryDatabase("../AppDatabase.db", migrationSQL)

    prfx = (
            Back.BLACK +
            Fore.GREEN +
            time.strftime(
                "%H:%M:%S UTC",
                time.gmtime()
            ) +
            Back.RESET +
            Fore.WHITE +
            Style.BRIGHT
    )

    print(prfx + " Successfully Migrated Database")

if __name__ == "__main__":
    initialize("../configuration.json")
    asyncio.run(main())