import re
from smolagents import tools
from smolagents import DuckDuckGoSearchTool
class WebYoutubeGenerator(tools.Tool):
    """
    A tool for retrieving YouTube video links based on a given search query.

    This tool performs a DuckDuckGo search with the provided query and extracts 
    relevant YouTube video links from the search results. It is useful for finding 
    educational videos, tutorials, or other video content related to the given topic.

    Example use cases:
    - "Find YouTube videos on how to write a professional email."
    - "Search for tutorials on Python web development."
    - "Get YouTube links for time management tips."
    """

    name = "WebYoutubeGenerator"
    description = (
        "A tool that retrieves relevant YouTube video links for a given search query. "
        "It fetches search results using DuckDuckGo and extracts YouTube links from them. "
        "Users should provide a clear query related to the videos they need, such as:\n"
        "- 'Find YouTube videos about writing a resume.'\n"
        "- 'Search for tutorials on JavaScript frameworks.'\n"
        "- 'Get YouTube links for AI and Machine Learning concepts.'\n"
        "This tool ensures only valid YouTube links are extracted."
    )

    inputs = {
        "query": {
            "type": "string",
            "description": "A descriptive search query for retrieving relevant YouTube video links.",
        }
    }

    output_type = "string"

    def __init__(self):
        """Initializes the tool with DuckDuckGo search functionality."""
        super().__init__()
        self.web_search_tool = DuckDuckGoSearchTool(max_results=5)

    def forward(self, query: str) -> str:
        """
        Processes the query, performs a search, and extracts YouTube links.

        Args:
            query (str): The search query.

        Returns:
            str: A newline-separated list of extracted YouTube video links, or an error message.
        """
        search_results = self.duckduckgo_search(query+"search in youtube")
        youtube_links = self.extract_youtube_links(search_results)
        return "\n".join(youtube_links) if youtube_links else "No YouTube links found."

    def duckduckgo_search(self, query: str) -> str:
        """
        Performs a DuckDuckGo search using the query.

        Args:
            query (str): The search query.

        Returns:
            str: The raw search results as a string.
        """
        try:
            response = self.web_search_tool(query)
            return str(response)  # Convert response to string format for regex processing
        except Exception as e:
            return f"Error while searching: {str(e)}"

    def extract_youtube_links(self, text: str) -> list:
        """
        Extracts YouTube links from the given search results.

        Args:
            text (str): The text containing potential YouTube links.

        Returns:
            list: A list of extracted YouTube video links.
        """
        youtube_pattern = r"https?://(?:www\.)?(?:youtube\.com/(?:watch\?v=|embed/|shorts/)|youtu\.be/)[\w-]+"
        return re.findall(youtube_pattern, text)

# Example Usage
# yt_generator = WebYoutubeGenerator()
# print(yt_generator.forward("How to write an email"))


class WebLinks_Generator(tools.Tool):
    """
    A tool for retrieving general web links from a search query.

    This tool searches the web using DuckDuckGo and extracts relevant website links 
    based on the user's input. It is useful for finding articles, blogs, research papers, 
    and other web resources.

    Example use cases:
    - "Find articles on best practices for writing emails."
    - "Search for web links related to Python programming tutorials."
    - "Retrieve links to the latest AI research papers."
    """

    name = "WebLinks_Generator"
    description = (
        "A web search tool that retrieves relevant web links based on a user query. "
        "It fetches results from DuckDuckGo and extracts valid website links. "
        "Users should provide a clear and specific query, such as:\n"
        "- 'Find web articles on software development trends in 2025.'\n"
        "- 'Retrieve links for online courses on Data Science.'\n"
        "- 'Search for research papers on Natural Language Processing.'\n"
        "This tool ensures only relevant web links are extracted and returned."
    )

    inputs = {
        "query": {
            "type": "string",
            "description": "A descriptive search query for retrieving web links.",
        }
    }

    output_type = "string"

    def __init__(self):
        """Initializes the tool with DuckDuckGo search functionality."""
        super().__init__()
        self.web_search_tool = DuckDuckGoSearchTool(max_results=5)

    def forward(self, query: str) -> str:
        """
        Processes the query, performs a search, and extracts web links.

        Args:
            query (str): The search query.

        Returns:
            str: A newline-separated list of extracted web links, or an error message.
        """
        search_results = self.duckduckgo_search(query)
        web_links = self.extract_web_links(search_results)
        return "\n".join(web_links) if web_links else "No relevant web links found."

    def duckduckgo_search(self, query: str) -> str:
        """
        Performs a DuckDuckGo search using the query.

        Args:
            query (str): The search query.

        Returns:
            str: The raw search results as a string.
        """
        response = self.web_search_tool(query)
        return str(response)  # Convert response to string format for regex processing

    def extract_web_links(self, text: str) -> list:
        """
        Extracts web links from the given text.

        Args:
            text (str): The text containing potential web links.

        Returns:
            list: A list of extracted web links.
        """
        web_pattern = r"https?://[^\s\]\)]+"
        return re.findall(web_pattern, text)

# Example Usage
# web_links_gen = WebLinks_Generator()

# print(web_links_gen.forward("Best practices for writing professional emails"))


# Example Usage
# yt_generator = WebYoutubeGenerator()
# print(yt_generator.forward("How to write an email to hr"))