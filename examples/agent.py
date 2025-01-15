from pathlib import Path
import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="Find remote jobs that match my skills based on my resume, create a list of these jobs, and then apply to them",
        llm=llm,
    )
    resume = Path(__file__).parents[1] / 'static' / 'David-Porkka-Web-Dev-Resume.pdf'
    result = await agent.run()
    print(result)

asyncio.run(main())