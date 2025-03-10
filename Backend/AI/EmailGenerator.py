import google.generativeai as genai
from smolagents import tools
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class EmailGenerator(tools.Tool):
    """
    A tool for generating professional emails based on user-provided input.

    This tool helps users draft well-structured emails for various purposes, 
    such as job applications, meeting requests, interview follow-ups, and more.
    It leverages Google's Gemini AI model to generate appropriate email content.

    Example use cases:
    - "Write a job application email for a software engineer position."
    - "Draft a polite follow-up email after a job interview."
    - "Compose an email to request a recommendation letter from my professor."

    The tool ensures the email follows professional etiquette and appropriate tone.
    """

    name = "EmailGenerator"
    description = (
        "This tool generates professional and well-structured emails based on the user's request. "
    )

    inputs = {
        "prompt": {
            "type": "string",
            "description": (
                "A brief description of the email to be generated. It should specify the "
                "purpose and key details of the email, such as the recipient and context."
            ),
        }
    }

    output_type = "string"

    def __init__(self):
        super().__init__()

    def forward(self, prompt: str) -> str:
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel("gemini-1.5-pro")  # Use a Gemini model for text generation
            response = model.generate_content("write a email to "+prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error: {str(e)}"

# Example Usage:
# email_gen = EmailGenerator()
# prompt = "Write an email to request a recommendation letter from my professor. add emojis"
# print(email_gen.forward(prompt))
