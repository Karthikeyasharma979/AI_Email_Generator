import re
from smolagents import tools,DuckDuckGoSearchTool

class WebYoutubeGenerator(tools.Tool):
    name = "Web"
    description = "This tool helps to retrieve the web links."
    inputs = {
        "query": {
            "type": "string",
            "description": "The text from which to retrieve web links",
        }
    }
    output_type = "string"
    def __init__(self):
        super().__init__()
        
    def forward(self, query: str) -> str:
        search_results = self.duckduckgo_search(query)

        youtube_links = self.extract_youtube_links(search_results)

        return "\n".join(youtube_links) if youtube_links else "No YouTube links found."

    def duckduckgo_search(self, query: str) -> str:
        """Perform a DuckDuckGo search (Mocked, replace with actual search)"""
        web = DuckDuckGoSearchTool(max_results=5)
        response =web(query)
        return response

    def extract_youtube_links(self, text: str) -> list:
        """Extract YouTube links from search results"""
        youtube_links = re.findall(r"https://www\.youtube\.com/watch\?v=[\w-]+", text)
        return youtube_links
    
    
class WebLinks_Generator(tools.Tool):
    name = "Web"
    description = "This tool helps to retrieve the web links."
    inputs = {
        "query": {
            "type": "string",
            "description": "The text from which to retrieve web links",
        }
    }
    output_type = "string"
    def __init__(self):
        super().__init__()
        
    def forward(self, query: str) -> str:
        search_results = self.duckduckgo_search(query)

        youtube_links = self.extract_youtube_links(search_results)

        return "\n".join(youtube_links) if youtube_links else "No YouTube links found."

    def duckduckgo_search(self, query: str) -> str:
        """Perform a DuckDuckGo search (Mocked, replace with actual search)"""
        web = DuckDuckGoSearchTool(max_results=5)
        response =web(query)
        return response

    def extract_youtube_links(self, text: str) -> list:
        """Extract YouTube links from search results"""
        youtube_links = re.findall(r"https://www\.youtube\.com/watch\?v=[\w-]+", text)
        return youtube_links

sp1 = Web()
print(sp1.forward("Give me the youtube video on how to write a email to HR"))
