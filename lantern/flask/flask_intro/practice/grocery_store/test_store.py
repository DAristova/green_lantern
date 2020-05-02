import inject

from store_app import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client
            self.users = self.setup_users()
            self.stores = self.setup_stores()

    def setup_users(self):
        response = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        return response

    def setup_stores(self):
        user_id = self.users.json['user_id']
        response = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': user_id}
        )
        return response

class TestUsers(Initializer):
    def test_create_new(self):
        assert self.users.status_code == 201
        assert self.users.json == {'user_id': 1}

    def test_successful_get_user(self):
        user_id = self.users.json['user_id']
        resp = self.client.get(f'/users/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_get_nonexistent_user(self):
        resp = self.client.get(f'/users/2')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 2'}

    def test_successful_update_user(self):
        user_id = self.users.json['user_id']
        resp = self.client.put(
            f'/users/{user_id}',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_nonexistent_update_user(self):
        resp = self.client.put(
            f'/users/2',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 2'}


class TestGoods(Initializer):
    def test_create_new_position(self):
        resp = self.client.post(
            '/goods',
            json=[
                {'name': 'Chocolate bar', 'price': '10'},
                {'name': 'Milk', 'price': '8'},
                {'name': 'Sausage', 'price': '18'},
                {'name': 'Sugar', 'price': '6'},
                {'name': 'Bread', 'price': '4'}
            ]
        )
        assert resp.status_code == 201
        assert resp.json == {'numbers of items created': 5}

    def test_get_goods(self):
        resp = self.client.post(
            '/goods',
            json=[
                {'name': 'Chocolate bar', 'price': '10'},
                {'name': 'Milk', 'price': '8'},
                {'name': 'Sausage', 'price': '18'},
                {'name': 'Sugar', 'price': '6'},
                {'name': 'Bread', 'price': '4'}
            ]
        )
        resp = self.client.get(f'/goods')
        assert resp.status_code == 200
        assert resp.json == [
            {'name': 'Chocolate bar', 'price': '10', 'id': 1},
            {'name': 'Milk', 'price': '8', 'id': 2},
            {'name': 'Sausage', 'price': '18', 'id': 3},
            {'name': 'Sugar', 'price': '6', 'id': 4},
            {'name': 'Bread', 'price': '4', 'id': 5}
        ]

    def test_successfully_goods_update(self):
        resp = self.client.post(
            '/goods',
            json=[
                {'name': 'Chocolate bar', 'price': '10'},
                {'name': 'Milk', 'price': '8'},
                {'name': 'Sausage', 'price': '18'},
                {'name': 'Sugar', 'price': '6'},
                {'name': 'Bread', 'price': '4'}
            ]
        )
        resp = self.client.put(
            f'/goods',
            json=[
                {'name': 'Cola', 'price': '10', 'id': 4},
                {'name': 'Juice', 'price': '12', 'id': 5},
                {'name': 'Cheese', 'price': '22', 'id': 6},
                {'name': 'Meat', 'price': '25', 'id': 7}
            ]
        )
        assert resp.status_code == 200
        assert resp.json == {'Successfully updated': 2, 'error': {'No such id in goods': [6, 7]}}


class TestStore(Initializer):
    def test_create_new_store(self):
        assert self.stores.status_code == 201
        assert self.stores.json == {'store_id': 1}

    def test_unsuccessful_create_store(self):
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 2'}

    def test_get_store(self):
        user_id = self.users.json['user_id']
        store_id = self.stores.json['store_id']
        resp = self.client.get(f'/store/{store_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': user_id}

    def test_get_nonexistent_store(self):
        resp = self.client.get('/store/2')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 2'}

    def test_update_store_by_id(self):
        user_id = self.users.json['user_id']
        store_id = self.stores.json['store_id']
        resp = self.client.put(
            f'/store/{store_id}',
            json={'name': 'Local Taste', 'location': 'Lviv', 'manager_id': user_id}
        )
        assert resp.status_code == 201
        assert resp.json == {'status': 'success'}

    def test_update_nonexistent_store_by_id(self):
        user_id = self.users.json['user_id']
        resp = self.client.put(
            f'/store/2',
            json={'name': 'Local Taste', 'location': 'Lviv', 'manager_id': user_id}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 2'}

    def test_update_store_by_nonexistent_manager(self):
        resp = self.client.put(
            f'/store/1',
            json={'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 2}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 2'}
