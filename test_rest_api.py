import requests


def get_response():
    url = 'https://poetrydb.org/author,poemcount/Dickinson;4'
    return requests.get(url)


# Verify code status
def test_response_code():
    response = get_response()
    assert response.status_code == 200


# Verify amount of poems retrieved.
def test_poem_title():
    response = get_response()
    assert len(response.json()) == 4
