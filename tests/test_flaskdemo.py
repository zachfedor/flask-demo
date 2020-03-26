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


def test_about_page(client):
    response = client.get('/about')
    assert b'This is a quick demo application' in response.data


def test_greeting_page(client):
    response1 = client.get('/greet/Amy')
    assert b'Hello Amy' in response1.data

    response2 = client.get('/greet/Bob')
    assert b'Hello Amy' not in response2.data
    assert b'Hello Bob' in response2.data

