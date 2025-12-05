from Internals.Database import fetchDatabase


class UserRepository:
    async def get(self):
        return await fetchDatabase("AppDatabase.db", "SELECT * FROM Users;", fetchMultiple=True)