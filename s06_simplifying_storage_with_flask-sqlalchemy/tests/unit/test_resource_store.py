import json

def test_store_post(client):
    response = client.post("/store/test_store_pytest")

    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert 'test_store_pytest' == data['name']

def test_store_get(client):   
    response = client.get("/store/test_store_pytest")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert 'test_store_pytest' == data['name']

def test_store_delete(client):
    response = client.delete("/store/test_store_pytest")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert 'Store deleted' == data['message']