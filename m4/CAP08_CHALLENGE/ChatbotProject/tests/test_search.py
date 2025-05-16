from chatbot.search import search_query


def test_search_returns_links():
    result = search_query("Python programming")
    assert isinstance(result, list)
    assert all(isinstance(url, str) for url in result)
    assert len(result) <= 5
