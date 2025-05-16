from typing import List
from newspaper.article import Article as ArticleType
from newspaper import Article


def extract_text_from_urls(urls: List[str]) -> str:
    corpus: List[str] = []
    for url in urls:
        try:
            article: ArticleType = Article(url)
            article.download()
            article.parse()

            text: str = str(article.text).strip()
            if text:
                corpus.append(f"--- [{url}] ---\n{text}\n")
        except Exception as e:
            print(f"[Extractor Error]: {url} - {e}")
            continue

    return (
        "\n\n".join(corpus)
        if corpus
        else "[No se pudo extraer contenido válido de los enlaces.]"

    )