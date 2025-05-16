from chatbot.extractor import extract_text_from_urls


def test_extractor_valid_url():
    urls = ["https://en.wikipedia.org/wiki/Apple"]
    result = extract_text_from_urls(urls)
    assert isinstance(result, str)
    assert "apple" in result.lower() or "manzana" in result.lower()


def test_extractor_invalid_url():
    urls = ["https://thisurldoesnotexist.tld/123"]
    result = extract_text_from_urls(urls)
    assert result.startswith("[No se pudo extraer")
