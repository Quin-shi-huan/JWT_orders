
from sqlite3 import Connection
from datetime import datetime

class UserRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_user(self, username: str, password: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO users
                (username, password)
            VALUES
                (?,?);
            ''', (username, password)
        )
        self.__conn.commit()

    def add_orders(self, user_id: int, description: str, date_order: datetime) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO orders
                (user_id, date_order, description)
            VALUES
                (?,?,?)
            ''', (user_id, date_order   , description)
        )
        self.__conn.commit()

    def get_user_orders(self,  username: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT id, username,  orders
            FROM users
            WHERE username = ?
            ''', (username,)
        )
        user = cursor.fetchone()
        return user
