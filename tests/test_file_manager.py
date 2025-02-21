import pytest
from file_manager import FileManager

@pytest.fixture
def random_file(tmp_path):
    file = tmp_path / 'random.txt'
    file.write_text('this is random text for testing including angry tiger')
    return file

def test_search_for_existing_word(random_file, capsys):
    find_word = FileManager(random_file)
    find_word.searching_word_in("tiger")

    captured = capsys.readouterr()
    assert 'the file includes tiger word' in captured.out

def test_search_for_nonexisting_word(random_file, capsys):
    find_word = FileManager(random_file)
    find_word.searching_word_in("lion")

    captured = capsys.readouterr()
    assert "there is no lion word in the file" in captured.out

