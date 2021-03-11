from db import db_session
from models import User

user = User(name='Maria Sidorova', salary=5432, email='msidorova@example.com')
db_session.add(user)
db_session.commit()