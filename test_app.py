

import pytest
from app import app


@pytest.fixture
def client():
    """
    Pytest fixture to create a test client.
    The 'TESTING' config makes Flask behave in testing mode:
     - Exceptions bubble up rather than being handled by the app
     - We'll get more helpful error info
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_recommend_from_id_success(client):
    """
    Test sending a valid request to /recommend/from_id
    """
    # Example valid ID; adjust to something you know exists in your model
    payload = {"id": "All Be Okay Lissie"}  
    response = client.post("/recommend/from_id", json=payload)

    assert response.status_code == 200, "Expected status code 200 for valid request"
    data = response.get_json()
    assert "processed_data" in data, "Response JSON should contain 'processed_data'"
    # You can add more assertions here based on your expected response data


def test_recommend_from_id_no_json(client):
    """
    Test calling /recommend/from_id without a JSON body
    """
    response = client.post("/recommend/from_id")  # No JSON body
    assert response.status_code == 400, "Expected status code 400 for missing JSON"


def test_recommend_from_id_list_success(client):
    """
    Test sending a valid request to /recommend/from_id_list
    """
    # Example list of valid IDs; adjust to your actual IDs
    payload = {"ids": ["All Be Okay Lissie", "Beautiful Joe Echo"]}  
    response = client.post("/recommend/from_id_list", json=payload)

    assert response.status_code == 200, "Expected status code 200 for valid request"
    data = response.get_json()
    assert "processed_data" in data, "Response JSON should contain 'processed_data'"
    # Add further assertions about the structure of "processed_data" if desired


def test_recommend_from_id_list_no_json(client):
    """
    Test calling /recommend/from_id_list without a JSON body
    """
    response = client.post("/recommend/from_id_list")  # No JSON
    assert response.status_code == 400, "Expected 400 for missing JSON"


def test_search_from_str_success(client):
    """
    Test sending a valid request to /search/from_str
    """
    payload = {"search_input": "Danza"}  
    response = client.post("/search/from_str", json=payload)

    assert response.status_code == 200, "Expected status code 200 for valid request"
    data = response.get_json()
    assert "processed_data" in data, "Response JSON should contain 'processed_data'"
    # Check the results structure
    assert "results" in data["processed_data"], "'processed_data' should contain 'results'"


def test_search_from_str_no_json(client):
    """
    Test calling /search/from_str without a JSON body
    """
    response = client.post("/search/from_str")  # No JSON
    assert response.status_code == 400, "Expected 400 for missing JSON"
