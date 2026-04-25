# Data ingestion module
import os
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

DATA_PATH = "data/"
INDEX_PATH = "../faiss_index"

documents = []
metadata = []

def load_documents():
    for file in os.listdir(DATA_PATH):
        file_path = os.path.join(DATA_PATH, file)

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Split into chunks (simple split)
        chunks = text.split("\n\n")

        for chunk in chunks:
            if chunk.strip() == "":
                continue

            documents.append(chunk)

            # Assign metadata
            if "finance" in file:
                metadata.append({"department": "finance"})
            elif "legal" in file:
                # differentiate summary vs full
                if "Summary" in chunk:
                    metadata.append({"department": "legal", "access": "summary"})
                else:
                    metadata.append({"department": "legal", "access": "full"})
            elif "hr" in file:
                # check employee ID
                if "Employee ID" in chunk:
                    owner = chunk.split("Employee ID")[1].split(":")[0].strip()
                    metadata.append({"department": "hr", "owner": owner})
                else:
                    metadata.append({"department": "hr"})

def create_index():
    embeddings = model.encode(documents)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    # Save index
    faiss.write_index(index, INDEX_PATH)

    # Save metadata + documents
    with open("../metadata.pkl", "wb") as f:
        pickle.dump(metadata, f)

    with open("../documents.pkl", "wb") as f:
        pickle.dump(documents, f)

if __name__ == "__main__":
    print("Loading documents...")
    load_documents()

    print(f"Total chunks: {len(documents)}")

    print("Creating FAISS index...")
    create_index()

    print("Done ✅")