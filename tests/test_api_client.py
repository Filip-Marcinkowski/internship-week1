import pytest
from api_client import APIClient

@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_output.txt"

def test_fetch_data_from_api(temp_file):
      
    url = "https://jsonplaceholder.typicode.com/posts" 
    api_client = APIClient(url, temp_file)

    api_client.fetch_data_from_api()

    assert temp_file.exists() 
    assert temp_file.stat().st_size > 0

    with open(temp_file, "r") as f:
        first_line = f.readline().strip()
        assert first_line != ""  

    