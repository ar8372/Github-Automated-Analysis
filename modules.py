
try: 
    import requests 
    from bs4 import BeautifulSoup 
    import pandas as pd
    import os   
    import sys 

    from fastapi import FastAPI, File, UploadFile, Form
    from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
    from pydantic import BaseModel
    import io
    import json
    import requests

    from PyPDF2 import PdfReader
    from langchain.embeddings.openai import OpenAIEmbeddings
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS


    from langchain.chains.question_answering import load_qa_chain
    from langchain.llms import OpenAI

except Exception as e: 
    print("Some Modules are Missing {}".format(e))

