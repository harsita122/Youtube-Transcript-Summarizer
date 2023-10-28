import transformers
from transcript import Transcript
from tqdm import tqdm
import asyncio

class AbstractiveSummarizer:
    async def createSummary(self,original_text):
        loop = asyncio.get_event_loop()
        if len(original_text.split()) < 100:
            return original_text
        
        summarization = transformers.pipeline("summarization")
        summary_text = []
        num_iters =  int(len(original_text)/1000)
        print("summarizing...")
        print("it may take a while depending on size of vid...")
        for i in tqdm(range(num_iters+1)):
            start = i*1000
            end = (i+1)*1000
            out = summarization(original_text[start:end])
            out = out[0]['summary_text']
            summary_text.append(out)
        
        summary_text = "".join(summary_text)
        print("*"*50)
        return summary_text



if __name__ == "__main__":
    print(AbstractiveSummarizer().createSummary("Ddzf9Mm4hdY"))