from Internals.Database import fetchDatabase

class UserRepository:
    async def fetchAll(self):
        users = await fetchDatabase("AppDatabase.db", "SELECT * FROM Users;", fetchMultiple=True)
        return users

    async def fetchOne(self, id):
        user = await fetchDatabase(
            "AppDatabase.db",
            "SELECT * FROM Users WHERE ID = ?;",
            (id,)
        )

        return user

    async def create(self):
        ...

    async def isRegistered(self, id):
        user = await self.fetchOne(id)

        if user:
            return True
        else:
            return False
