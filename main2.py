from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from pydantic import BaseModel
import io
import json
import requests
import sys 
from utils import * 

from modules import * 
from utils import * 
from scrap_repo import get_repo_csv 
from create_raw_text import get_raw_text
from query import run_query


app = FastAPI(title="Github Automated Analysis API", description="An API for calculating most complex repository.")



if __name__ == "__main__":
    url = sys.argv[1]
    OPENAI_API_KEY = sys.argv[2]
    df = get_repo_csv(url)
    df.to_csv("repo_report.csv", index=False)
    get_raw_text()
    ans= run_query(OPENAI_API_KEY)
    print(ans)
