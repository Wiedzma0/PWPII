from fastapi import FastAPI
from pydantic import BaseModel
from transformers.pipelines import pipeline
from typing import List, Dict

app = FastAPI()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_text(item: TextInput):
    summary: List[Dict[str, str]] = summarizer(item.text, max_length=130, min_length=30, do_sample=False) # type: ignore
    return {"summary": summary[0]['summary_text']}
