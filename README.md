# RAG RBAC Chatbot

A secure Retrieval-Augmented Generation (RAG) chatbot with Role-Based Access Control (RBAC) for enterprise use. This system ensures that users can only access information appropriate to their role, preventing unauthorized data exposure.

## Features

- **Role-Based Access Control (RBAC)**: Different user roles (admin, manager, employee, auditor) with specific access permissions
- **Retrieval-Augmented Generation (RAG)**: Uses vector search with FAISS and sentence transformers for context retrieval
- **Secure AI Responses**: LLM responses are strictly limited to provided context, preventing information leakage
- **Department-Specific Data**: Organized data for HR, Finance, and Legal departments
- **Local LLM Integration**: Uses Ollama with Llama3 model for offline AI generation

## Installation

### Prerequisites

- Python 3.8+
- Ollama installed and running (for Llama3 model)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/VinuthnaReddy07/RAG-RBAC-chatbot.git
   cd RAG-RBAC-chatbot
   ```

2. Install Python dependencies:
   ```bash
   pip install -r Requirements.txt
   ```

3. Install and start Ollama:
   ```bash
   # Install Ollama from https://ollama.ai/
   ollama pull llama3
   ollama serve
   ```

4. Run data ingestion to create the FAISS index:
   ```bash
   python src/ingestion.py
   ```

## Usage

Run the main application:

```bash
python src/main.py
```

The chatbot will prompt for:
- User role (admin, manager, employee, auditor)
- User ID (for employee role)
- Query

Example interaction:
```
Enter your role: employee
Enter your user ID: 123
Enter your query: What is my salary?
```

## Project Structure

```
├── README.md              # This file
├── Requirements.txt       # Python dependencies
├── data/                  # Raw data files
│   ├── finance.txt        # Financial data
│   ├── hr.txt            # Human resources data
│   └── legal.txt         # Legal documents
├── docs/                  # Documentation
│   ├── adversarial_tests.md  # Security test cases
│   ├── client_brief.md       # Project requirements
│   └── prompt_design.md      # Prompt engineering tests
└── src/                   # Source code
    ├── ingestion.py       # Data processing and indexing
    ├── main.py           # Main application entry point
    ├── rbac.py           # Role-based access control logic
    └── retriever.py      # Vector search retrieval
```

## Roles and Permissions

### Admin
- Full access to all departments and data

### Manager
- Access to all departments except full legal documents (only summaries)
- Can view HR data and general finance/legal info

### Employee
- Limited HR access (only own records and general HR info)
- No access to finance or legal data

### Auditor
- Access to finance and legal data only
- No HR data access

## Security Features

- **Context-Only Responses**: AI can only answer using retrieved context
- **Access Control**: Strict RBAC prevents unauthorized data access
- **No External Knowledge**: LLM cannot use training data or external information
- **Adversarial Protection**: Designed to resist prompt injection and role escalation attacks

## Contributing

This is an assignment project. For improvements or bug fixes, please create an issue or pull request on GitHub.

## License

[Add license information if applicable]
