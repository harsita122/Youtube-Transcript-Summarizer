from flask import Flask
from flask import request
from transcript import Transcript
from AbstractiveSummarizer import AbstractiveSummarizer
import asyncio
from flask import Flask
from ExtractiveSummarizer import ExtractiveSummarizer

loop = asyncio.get_event_loop()
app = Flask(__name__)

@app.route('/abstractivesummarizer/<path:link>')
def get_as(link):
    video_id=request.args.get("v")
    ans = ""
    ans += "Abstractive Summarized version: <br>"
    transcript = loop.run_until_complete(Transcript().getTranscript(video_id))
    temp = loop.run_until_complete(AbstractiveSummarizer().createSummary(transcript))
    ans += temp
    ans += "<br> Words: " + str(len(temp.split()))

    ans += "<br><br> Transcript: <br>" + transcript
    ans += "<br> Words: " + str(len(transcript.split())) 
    return ans

@app.route('/extractivesummarizer/<path:link>')
def get_es(link):
    video_id=request.args.get("v")
    ans = ""
    ans += "Extractive Summarized version: <br>"
    transcript = loop.run_until_complete(Transcript().getTranscript(video_id))
    temp = loop.run_until_complete(ExtractiveSummarizer().createSummary())
    ans += temp
    ans += "<br> Words: " + str(len(temp.split()))

    ans += "<br><br> Transcript: <br>" + transcript
    ans += "<br> Words: " + str(len(transcript.split())) 
    return ans


app.run(debug=True)