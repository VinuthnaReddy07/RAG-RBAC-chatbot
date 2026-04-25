# Retriever module
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load index
index = faiss.read_index("../faiss_index")

# Load metadata + docs
with open("../metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

with open("../documents.pkl", "rb") as f:
    documents = pickle.load(f)

def retrieve(query, top_k=5):
    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    results = []
    for i in indices[0]:
        results.append({
            "text": documents[i],
            "meta": metadata[i]
        })

    return results