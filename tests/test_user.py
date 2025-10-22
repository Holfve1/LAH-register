from lib.user import User

def test_user_initialises():
    user = User(1, "Dave", "Smith", "Camden")
    assert user.first_name == "Dave"
    assert user.last_name == "Smith"
    assert user.address == "Camden"

def test_users_are_equal():
    user1 = User(1, "Dave", "Smith", "Camden")
    user2 = User(1, "Dave", "Smith", "Camden")
    assert user1 == user2

def test_users_are_formatted_correctly():
    user = User(1, "Dave", "Smith", "Camden")
    assert str(user) == "User(1, Dave, Smith, Camden)"