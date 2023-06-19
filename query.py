# from PyPDF2 import PdfReader
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS


# from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI
from modules import * 


def run_query(open_ai_key):
    
    os.environ["OPENAI_API_KEY"] = open_ai_key

    with open("a.txt", "r", encoding="utf-8") as x:
        raw_text = x.read()


    chunk_size = 1000  # Set the desired chunk size
    chunk_overlap = 200  # Set the desired overlap size

    chunks = []
    start_index = 0
    text_length = len(raw_text)

    while start_index < text_length:
        end_index = min(start_index + chunk_size, text_length)
        chunk = raw_text[start_index:end_index]

        # Adjust the end index to include the overlap
        end_index += chunk_overlap
        if end_index > text_length:
            end_index = text_length

        chunks.append(chunk)
        start_index = end_index

    texts = chunks

    # Download embeddings from OpenAI
    embeddings = OpenAIEmbeddings(disallowed_special=())

    docsearch = FAISS.from_texts(texts, embeddings)

    chain = load_qa_chain(OpenAI(), chain_type="stuff")

    query = "Based on the given codebase, please analyze the complexity of each repository/project and identify the repository/project that appears to have the highest level of complexity. Complexity in this context represents the level of sophistication and depth of the code, indicating the amount of effort and work invested in the project. Consider factors such as algorithmic complexity, control flow, coupling and cohesion, adherence to design patterns, and architectural principles. Provide your analysis and reasoning for determining the file that showcases the highest level of complexity, emphasizing the positive aspects of the intricate and well-crafted code."
    docs = docsearch.similarity_search(query)
    answer = chain.run(input_documents=docs, question=query)
    return answer

