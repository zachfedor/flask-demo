import flaskdemo

def test_import():
    assert flaskdemo

def test_config():
    assert not flaskdemo.create_app().testing
    assert flaskdemo.create_app({ 'TESTING': True }).testing

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>Flask Demo</h1>' in response.data
    assert b'Welcome to the home page' in response.data

