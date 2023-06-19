
# from fastapi import FastAPI, File, UploadFile, Form
# from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
# from pydantic import BaseModel
# import io
# import json
# import requests

from utils import * 
from modules import * 
from scrap_repo import get_repo_csv 
from create_raw_text import get_raw_text
from query import run_query


app = FastAPI(title="Github Automated Analysis API", description="An API for calculating most complex repository.")

class ImageCaption(BaseModel):
    caption: str

@app.post("/predict/", response_model=ImageCaption)
def predict(url: str = Form(...), OPENAI_API_KEY: str = Form(...)):
    # Process the text input
    df = get_repo_csv(url)
    df.to_csv("repo_report.csv", index=False)
    get_raw_text()
    ans= run_query(OPENAI_API_KEY)

    return JSONResponse(content={"Most Complex Repo:": ans})

# Redirect the user to the documentation
@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse(url="/docs")