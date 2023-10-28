import urllib.parse as up
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import asyncio
import re
import os

class Transcript:

    async def getTranscript(self,video_id):
        # loop = asyncio.get_event_loop()
        print("getting transcript...")
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        # transcript_list = loop.run_until_complete(YouTubeTranscriptApi.get_transcript(video_id))
        
        
        # normalization
        dum = []
        transcript_alone_list = []
        for i in transcript_list:
            transcript_alone_list.append(i['text'])
        for i in transcript_alone_list:
            name = re.sub(r'\[[^][]*\]', '', i) + ' '
            dum.append(name)
        while '' in dum:
            dum.remove('')
        
        transcript = ""

        for i in dum:
            transcript +=  i.replace("\n", " ") + ' '
        c = transcript.count('.')
        if c < 10:
            transcript = ""
            for i in range(len(dum)):
                
                if i%5 == 0 and i != 0:
                    transcript += dum[i] + '. '
                else:
                    transcript += dum[i]

        if os.path.isdir("out"):
            pass
        else:
            os.mkdir("out")
        with open("out/intermediate.txt", 'w', encoding="utf-8") as f:
            f.write(transcript)
            f.close()

        return transcript

if __name__ == "__main__":
    print(Transcript().getTranscript("liJVSwOiiwg"))
