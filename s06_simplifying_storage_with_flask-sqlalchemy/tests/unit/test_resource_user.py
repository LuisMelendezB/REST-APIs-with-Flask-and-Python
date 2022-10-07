import json

def test_user_post(client):
    response = client.post("/register",
                            data=json.dumps(dict(username="test_user_pytest",
                                                password="abcdefg")),
                            content_type='application/json'
                            )

    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert 'User created successfully' == data['message']

def test_user_auth_get(client):   
    response = client.post("/auth",
                            data=json.dumps(dict(username="test_user_pytest",
                                                password="abcdefg")),
                            content_type='application/json'
                            )
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert isinstance(data['access_token'], str)

def test_user_delete(client):
    response = client.delete("/userdelete/test_user_pytest")
    data = json.loads(response.data.decode())
    assert 'User deleted' == data[0]['message']
    assert response.status_code == 200
    

