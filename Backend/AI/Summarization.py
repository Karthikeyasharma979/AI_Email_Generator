import os
import google.generativeai as genai
from smolagents import tools
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Summarization(tools.Tool):
    """
    A tool for summarizing text or generating a subject line from the given content.

    This tool interacts with Google Gemini API (Gemini Pro 1.5) to perform text summarization.
    It can be used in two modes:
    1. **Summary Mode**: Generates a concise summary of the provided text.
    2. **Subject Line Mode**: Extracts a short subject line from the given content.
    """

    name = "Summarization"
    description = (
        "This tool can generate a summary or a subject line from the given text. "
        "The user must specify whether they want a 'summary' or 'subject' in the 'mode' parameter.\n"
        "Example usage:\n"
        "- 'Summarize this job application email.'\n"
        "- 'Generate a subject line for my sales pitch.'"
    )

    inputs = {
        "text": {
            "type": "string",
            "description": "The text from which to generate a summary or subject line.",
        },
        "mode": {
            "type": "string",
            "description": "Specify 'summary' to get a summarized version of the text, or 'subject' to get a subject line.",
            "nullable": True,
        },
    }

    output_type = "string"

    def __init__(self):
        """Initializes the tool with Google Gemini API client."""
        super().__init__()
        api_key = os.getenv("GEMINI_API_KEY")  # ✅ Secure API key usage
        if not api_key:
            raise ValueError("Missing Gemini API key. Please set GEMINI_API_KEY in your .env file.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")  # ✅ Use Gemini Pro

    def forward(self, text: str, mode: str = "summary") -> str:
        """
        Processes the text and generates either a summary or a subject line.

        Args:
            text (str): The input text to summarize or extract a subject from.
            mode (str): The operation mode, either 'summary' or 'subject'. Defaults to 'summary'.

        Returns:
            str: The generated summary or subject line.
        """
        try:
            if mode.lower() not in ["summary", "subject"]:
                return "Invalid mode! Please specify either 'summary' or 'subject'."
            
            if mode.lower() == "summary":
                prompt = f"Summarize the following text:\n{text}"
            else:
                prompt = f"Generate a concise subject line for this text:\n{text}"

        
            response = self.model.generate_content(prompt)

            result = response.text.strip()

            if mode.lower() == "subject":
                return f"Suggested Subject: {result}"  # Shorten for subject lines
            return result

        except Exception as e:
            return f"Error: {str(e)}. Please check your API key or input."

# Example Usage:
# sp = Summarization()
# text = """Dear Hiring Manager, I hope you’re doing well. I wanted to follow up on my job application for the Software Engineer role at XYZ Company. I’m very excited about this opportunity and would love to discuss how my skills align with the position. Please let me know if there are any updates. Thank you for your time and consideration."""
# print(sp.forward(text, "summary"))  # ✅ Get summary
# print(sp.forward(text, "subject"))  # ✅ Get subject line
