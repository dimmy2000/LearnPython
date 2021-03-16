import sys

from getpass import getpass

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
    username = input("Введите имя пользователя:")

    if User.query.filter(User.username == username).count():
        print("Пользователь с таким именем уже существует")
        sys.exit(0)

    password1 = getpass("Введите пароль")
    password2 = getpass("Повторите пароль")

    if not password1 == password2:
        print("Пароли не совпадают")
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('User with id {} added'.format(new_user.id))