from unittest.mock import Mock
from datetime import datetime
from .user_repository import UserRepository

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()
        self.fetchall = Mock()

class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

# Teste realizado e APROVADO
def test_registry_user():
    username = "MyUsername"
    password = "MyPassword"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password)

    mock_connection.commit.assert_called_once()

# Teste realizado e APROVADO - Não foi realizada a remoção dos Microseconds
def test_add_orders():
    user_id = 1
    date_order = datetime.now()
    description = "description"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    cursor = mock_connection.cursor.return_value
    repo.add_orders(user_id, description, date_order)

    assert "INSERT INTO orders" in cursor.execute.call_args[0][0]
    assert "(user_id, date_order, description)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (user_id, date_order, description)

def test_get_user_orders():
    username = "Eduardo"

    mock_connection = MockConnection()
    repo =  UserRepository(mock_connection)
    cursor  = mock_connection.cursor.return_value
    repo.get_user_orders(username)

    assert "SELECT id, username,  orders" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)
