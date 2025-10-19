# Creating AI Web Scraping Tool

# STEP 1 -> search the web 

import http.client
import json
import os
import httpx
import asyncio
from dotenv import load_dotenv
from fastmcp import FastMCP
from utils import clean_html_to_txt, get_response_from_llm


load_dotenv()

mcp = FastMCP("docs")

SERPER_URL= "https://google.serper.dev/search"

async def search_web(query: str) -> dict | None:
    payload = json.dumps({"q": query, "num": 2})
    headers = {
    'X-API-KEY': os.getenv("SERPER_API_KEY"),
    'Content-Type': 'application/json'
    }  
    async with httpx.AsyncClient() as client:
        response = await client.post(
            SERPER_URL, headers=headers, data=payload, timeout=30.0
        )
        response.raise_for_status()
        return response.json()


# STEP 2 -> open official documentation 

async def fetch_url(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=30.0)
        system_prompt = "You are an AI Web scraper. Only return valid text, remove and clean every other HTML component that is not required."
               
        chunk_size = 4000
        text_chunks = [response.text[i:i+chunk_size] for i in range(0, len(response.text), chunk_size)]
        
        cleaned_parts = []
        for chunk in text_chunks:
            cleaned_chunk = get_response_from_llm(
            user_prompt=chunk, 
            system_prompt=system_prompt, 
            model="llama-3.1-8b-instant"
            )
            cleaned_parts.append(cleaned_chunk)
        
        cleaned_response = "".join(cleaned_parts)
        return cleaned_response


# STEP 3 -> read documentation and write code acordingly

docs_urls = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai": "platform.openai.com/docs",
    "uv": "docs.astral.sh/uv",
}


@mcp.tool
async def get_docs(query: str, library: str):
    """
    Search the latest docs for a given query and library.
    Supports langchain, openai, llama-index and uv.

    Args:
        query: The query to search for (e.g. "Publish a package with UV")
        library: The library to search in (e.g. "uv")

    Returns:
        Summarized text from the docs with source links.
    """
    if library not in docs_urls:
        raise ValueError(f"Library {library} not supported by this tool")
    
    query = f"site:{docs_urls[library]} {query}"

    results = await search_web(query)

    if len(results["organic"]) == 0:
        return "No results found"

# sources of info
    text_parts = []
    for result in results["organic"]:
        link = result.get("link", "")
        raw = await fetch_url(link)
        if raw:
            labeled = f"SOURCE: {link}\n{raw}"
            text_parts.append(labeled)
    return "\n\n".join(text_parts)

def main():
    mcp.run(transport="stdio")
    

if __name__ == "__main__":
    main()