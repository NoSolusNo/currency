import sqlite3

connection = sqlite3.connect('./Chinook_Sqlite.sqlite')
connection.row_factory = sqlite3.Row
cur = connection.cursor()

sql = '''
select CustomerId, FirstName, LastName from customer;
'''
cur.execute(sql)
result = cur.fetchall()
connection.close()


# for user in result:
# print(f'{user["CustomerId"]} {user["FirstName"]} {user["LastName"]}')
# print(user)
# print(dict(user))


class User:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


    def save(self):
        import sqlite3

        connection = sqlite3.connect('./Chinook_Sqlite.sqlite')
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()

        sql = '''
        UPDATE customer
        SET FirstName = "{self.FirstName}",
            LastName = "{self.LastName}"
        WHERE
            CustomerId = "{self.CustomerId}"
        '''
        cur.execute(sql)
        connection.commit()
        connection.close()

users = [
    User(**data) for data in result
]
breakpoint()
