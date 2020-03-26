import flaskdemo

def test_import():
    assert flaskdemo

def test_config():
    assert not flaskdemo.create_app().testing
    assert flaskdemo.create_app({ 'TESTING': True }).testing

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flask demo is working' in response.data

