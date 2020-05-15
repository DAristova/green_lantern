import csv

from sqlalchemy_utils import create_database, drop_database, database_exists
from app import app, db
from models import User, Good, Store


def get_user():
    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
    return users


def get_goods():
    with open('goods.csv', 'r') as f:
        reader = csv.DictReader(f)
        goods = [i for i in reader]
    return goods


def get_stores():
    with open('stores.csv', 'r') as f:
        reader = csv.DictReader(f)
        stores = [i for i in reader]
    return stores


with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print('db exist')
    else:
        print(f'db dose not exist {db.engine.url}')
        create_database(db.engine.url)
        print('Database created')


with app.app_context():
    users = get_user()
    for user in users:
        db.session.add(User(**user))
    db.session.commit()
    print('Data have written in database')


with app.app_context():
    goods = get_goods()
    for good in goods:
        db.session.add(Good(**good))
    db.session.commit()
    print('Goods have written in database')


with app.app_context():
    stores = get_stores()
    for store in stores:
        db.session.add(Store(**store))
    db.session.commit()
    print('Stores have written in database')
