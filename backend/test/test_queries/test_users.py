from dependencies.constants import USER_COLL, CLIENT
from schemas.users import UserCreate
from schemas.security_classes import *


client = CLIENT

def test_create_user(client):
    data = {"username":"testuser", "full_name":"Test User", "email":"testuser@nofoobar.com","password":"testing", "disabled": False}
    response = client.insert_one(data).inserted_id
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] == True


def test_create_new_user(user: UserCreate, db = USER_COLL):
    user = User(
        username = user.username,
        email = user.email,
        hashed_password = Hasher.get_password_hash(user.password),
        is_active = True,
        is_superuser = False
        )

    db.insert_one(user).inserted_id
    return(user)


#test_create_user(client=user_coll)
test_create_new_user(user={"username": "fancypants", "email":"fancy.pants@noshirtsgiven.com", "password":"321drowssaP"})


client.close()