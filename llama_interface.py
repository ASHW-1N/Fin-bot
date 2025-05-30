from llama_cpp import Llama
from financial_news import retrieve_similar_news

# Load your model
llm = Llama(
    model_path=r"C:\finance-assistant\models\llama-2-7b-chat.Q8_0.gguf",
    n_ctx=2048,
    n_threads=8,
    use_mlock=False
)

def ask_llama(query):
    # Get context from RAG
    context_chunks = retrieve_similar_news(query)

    # Format context safely
    context = "\n\n".join(
        f"{chunk.get('title', '')}: {chunk.get('summary', '')}"
        for chunk in context_chunks if isinstance(chunk, dict)
    )

    prompt = f"""You are a financial assistant. Use the following recent news to answer the query.

Context:
{context}

Query: {query}

Answer:"""

    response = llm(prompt, max_tokens=500, stop=["</s>"], echo=False)
    return response["choices"][0]["text"].strip()
