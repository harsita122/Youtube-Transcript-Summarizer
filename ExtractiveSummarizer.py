from transcript import Transcript
from summarizer_2 import Summarizer_2
import asyncio
import os

class ExtractiveSummarizer:
    async def createSummary(self):
        summ = Summarizer_2()
        summ.gen_summary()
        ans = ""
        with open("out/Output.txt", 'r', encoding="utf-8") as f:
            filedata = f.readlines()
            f.close()
        for i in filedata:
            ans += i
        return ans



if __name__ == "__main__":
    print(ExtractiveSummarizer().createSummary("zarll9bx6FI"))