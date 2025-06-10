# RAG (Retrieval-Augmented Generation)

Se você escolher `use_rag: 'y'`, o template irá gerar uma estrutura dedicada para construir sistemas RAG. A pasta `rag` será criada com os seguintes módulos:

-   **`embeddings.py`**: Responsável por carregar o modelo de embedding e transformar textos em vetores. É aqui que você define qual modelo usar (ex: da HuggingFace, OpenAI, etc.).

-   **`vector_store.py`**: Gerencia a criação e o acesso ao banco de dados vetorial (ex: FAISS, ChromaDB). Ele usa os embeddings para indexar e armazenar seus documentos.

-   **`retriever.py`**: Contém a lógica para realizar a busca de similaridade. Dado um prompt do usuário, ele consulta o `vector_store` para encontrar os trechos de documentos mais relevantes.

Essa estrutura modular permite que você construa e mantenha sistemas RAG complexos de forma organizada.