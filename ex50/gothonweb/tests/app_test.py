from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects = True)
    assert_equal(rv.status_code, 200)

def test_index_hello():
    rv = web.get('/hello', follow_redirects = True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out this Form", rv.data)

    data = {'name': 'Ankit', 'greet': 'Jai Yeshu'}
    rv = web.post('/hello', follow_redirects = True, data = data)
    assert_in(b"Ankit", rv.data)
    assert_in(b"Jai Yeshu", rv.data)
