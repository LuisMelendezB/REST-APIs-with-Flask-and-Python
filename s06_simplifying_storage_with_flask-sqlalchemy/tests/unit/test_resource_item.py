import json 

def test_item_post(client):
    response = client.post("/item/test_item_pytest",
                            data=json.dumps(dict(price=999.99,
                                                store_id=1)),
                            content_type='application/json'
                            )

    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert 'test_item_pytest' == data['name']
    assert 999.99 == data['price']
    assert 1 == data['store_id']

def test_item_get(client):   
    response = client.get("/item/test_item_pytest")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert 'test_item_pytest' == data['name']
    assert 999.99 == data['price']
    assert 1 == data['store_id']

def test_item_put(client):
    response = client.put("/item/test_item_pytest",
                            data=json.dumps(dict(price=888.88,
                                                store_id=1)),
                            content_type='application/json'
                            )               

    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert 'test_item_pytest' == data['name']
    assert 888.88 == data['price']
    assert 1 == data['store_id']

def test_item_delete(client):
    response = client.delete("/item/test_item_pytest")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert 'Item deleted' == data[0]['message']

