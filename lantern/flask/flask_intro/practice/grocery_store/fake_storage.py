from itertools import count
from store_app import NoSuchUserError, NoSuchStoreError


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._stores = FakeStores()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def stores(self):
        return self._stores


class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count(1)

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._users:
            self._users[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class FakeGoods:
    def __init__(self):
        self._goods = {}

    def add_new_position(self, goods):
        id_counter = count(1)
        for good in goods:
            good['id'] = next(id_counter)
            self._goods[good['id']] = good
        return len(goods)

    def get_all_goods(self):
        goods = [self._goods[good] for good in self._goods]
        return goods

    def update_positions(self, goods):
        goods_update = 0
        error_id = []
        for good in goods:
            if good['id'] in self._goods:
                self._goods[good['id']] = good
                goods_update += 1
            else:
                error_id.append(good['id'])
        return goods_update, error_id


class FakeStores:
    def __init__(self):
        self._stores = {}
        self._id_counter = count(1)
                
    def add(self, store):
        store_id = next(self._id_counter)
        self._stores[store_id] = store
        return store_id

    def get_store_by_id(self, store_id):
        try:
            return self._stores[store_id]
        except KeyError:
            raise NoSuchStoreError(store_id)

    def update_store_by_id(self, store_id, store):
        if store_id in self._stores:
                self._stores[store_id] = store
        else:
            raise NoSuchStoreError(store_id)

