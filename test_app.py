from app import soma, get_user


def test_soma():
    assert soma(2, 3) == 5


def test_get_user():
    assert get_user("ana") == [("ana",)]
