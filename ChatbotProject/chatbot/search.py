from typing import List, Dict, Any
import os
import requests
from requests import Response
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY: str | None = os.getenv("SERPER_API_KEY")

HEADERS: Dict[str, str] = {
    "X-API-KEY": SERPER_API_KEY or "",
    "Content-Type": "application/json",
}

API_URL: str = "https://google.serper.dev/search"


def search_query(prompt: str) -> List[str]:
    if not SERPER_API_KEY:
        raise ValueError("SERPER_API_KEY no definido en .env")

    payload: Dict[str, str | int] = {"q": prompt, "num": 5}

    try:
        res: Response = requests.post(API_URL, json=payload, headers=HEADERS)
        res.raise_for_status()
        data: Dict[str, Any] = res.json()

        links: List[str] = []
        organic_results: List[Dict[str, Any]] = data.get("organic", [])
        for item in organic_results[:5]:
            if isinstance(item.get("link"), str):
                links.append(item["link"])

        return links

    except Exception as e:
        print(f"[Error al buscar]: {e}")
        return []
