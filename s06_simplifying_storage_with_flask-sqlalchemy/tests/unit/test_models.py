from models.user import UserModel
from models.store import StoreModel
from models.item import ItemModel


def test_new_user():
    user = UserModel('test_username','test_password')
    assert user.username == 'test_username'
    assert user.password == 'test_password'


def test_new_item():
    item = ItemModel('test_item_name',13.99,1)
    assert item.name == 'test_item_name'
    assert item.price == 13.99
    assert item.store_id == 1


def test_new_store():
    store = StoreModel('test_store_name')
    assert store.name == 'test_store_name'