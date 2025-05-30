import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# ✅ Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Dummy fetch function (replace with actual logic or API/file load)
def load_news():
    """Load news articles from a local file or API. Expected format: List of dicts."""
    try:
        with open("news.json", "r", encoding="utf-8") as f:
            articles = json.load(f)
            return articles
    except Exception as e:
        print("❌ Error loading news:", e)
        return []

# ✅ Safely process and encode news
def fetch_and_index_news():
    articles = load_news()

    if not articles:
        print("⚠️ No articles found.")
        return None

    # Validate structure
    if isinstance(articles[0], dict):
        news_articles = [
            (article.get("title") or "") + ". " + (article.get("description") or "")
            for article in articles
        ]
    elif isinstance(articles[0], str):
        news_articles = articles  # already cleaned strings
    else:
        raise ValueError("Unsupported article format.")

    # Generate embeddings
    embeddings = model.encode(news_articles)

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    # Store article texts in same order
    global indexed_texts
    indexed_texts = news_articles

    return index

# ✅ Global FAISS index
faiss_index = fetch_and_index_news()

# ✅ Retrieve similar news using the FAISS index
def retrieve_similar_news(query, top_k=3):
    if faiss_index is None:
        return ["No news index available."]

    query_embedding = model.encode([query])[0].reshape(1, -1)
    distances, indices = faiss_index.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
        if 0 <= idx < len(indexed_texts):
            results.append(indexed_texts[idx])

    return results
