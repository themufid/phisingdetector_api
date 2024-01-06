# phishingdetector/detector/main.py
from fastapi import FastAPI, HTTPException, Depends
from django.db import models
from detector.models import TextSample
from detector.serializers import TextSampleSerializer

app = FastAPI()

@app.post("/detect-phishing/", response_model=TextSampleSerializer)
async def detect_phishing(text_sample: TextSampleSerializer):
    is_phishing = "phishing" in text_sample.text.lower()

    text_instance = TextSample(text=text_sample.text, is_phishing=is_phishing)
    text_instance.save()

    return {"text": text_sample.text, "is_phishing": is_phishing}
