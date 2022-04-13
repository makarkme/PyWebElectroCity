from flask import Flask
from data import db_session
# from data.users import User

app = Flask(__name__)
# user = User()
# user.name = "Пользователь 1"
# user.about = "биография пользователя 1"
# user.email = "email@email.ru"
# db_sess = db_session.create_session()
# db_sess.add(user)
# db_sess.commit()


def users():
    db_session.global_init("users.db")


def products():
    db_session.global_init("products.db")


if __name__ == '__main__':
    users()
    products()
    app.run()
