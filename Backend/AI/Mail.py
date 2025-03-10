import google.generativeai as genai
from smolagents import tools
from dotenv import load_dotenv
import os
import urllib.parse
import webbrowser

# Load environment variables
load_dotenv()

class Tools(tools.Tool):  
    """
    A tool for performing various automated tasks such as opening YouTube videos and composing emails.

    - **YouTube Video Opener**: Opens a specified YouTube video in the browser.
    - **Email Generator**: Generates professional emails based on user input using Google's Gemini AI.

    Example use cases:
    - "Open this YouTube video: https://www.youtube.com/watch?v=xyz"
    - "Draft an email to follow up on a job interview."
    - "Generate an email requesting feedback on my recent project."
    """

    name = "Tools"
    description = (
        "This tool provides multiple functionalities including:\n"
        "- Opening YouTube videos.\n"
        "- Generating well-structured emails for professional communication using AI.\n"
        "Users should specify the request type ('youtube' or 'mail') along with relevant details."
    )

    inputs = {
        "type": {
            "type": "string",
            "description": "Specify 'youtube' to open a YouTube video or 'mail' to generate an email draft.",
        },
        "url": {
            "type": "string",
            "description": "YouTube video URL (required if type is 'youtube').",
            "required": False,
            "nullable": True,
        },
        "to": {
            "type": "string",
            "description": "Recipient email address (required if type is 'mail').",
            "required": False,
            "nullable": True,
        },
        "subject": {
            "type": "string",
            "description": "Subject of the email (required if type is 'mail').",
            "required": False,
            "nullable": True,
        },
        "body": {
            "type": "string",
            "description": "Brief description of the email content (required if type is 'mail').",
            "required": False,
            "nullable": True,
        },
    }

    output_type = "string"

    def __init__(self):
        super().__init__()

    def is_valid_email(self, email):
        """Basic email validation."""
        return "@" in email and "." in email

    def forward(self, type: str, url: str = "", to: str = "", subject: str = "", body: str = "") -> str:
        """
        Processes user requests for YouTube video opening or email generation.

        Args:
            type (str): Specify 'youtube' to open a YouTube video or 'mail' to generate an email draft.
            url (str): YouTube video URL (required if type is 'youtube').
            to (str): Recipient email address (required if type is 'mail').
            subject (str): Subject of the email (required if type is 'mail').
            body (str): Brief description of the email content (required if type is 'mail').

        Returns:
            str: A success message or an error message.
        """
        request_type = type.strip().lower()

        if request_type == "youtube":
            video_url = url.strip()
            if "youtube.com" in video_url or "youtu.be" in video_url:
                webbrowser.open(video_url)
                return "YouTube video opened successfully!"
            else:
                return "Error: Invalid YouTube URL."

        elif request_type == "mail":
            recipient = to.strip()
            subject = subject.strip()
            body = body.strip()

            if not recipient or not self.is_valid_email(recipient):
                return "Error: Invalid or missing email address."

            try:
                # Generate email content using Gemini AI
                genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
                model = genai.GenerativeModel("gemini-1.5-pro")
                response = model.generate_content(f"Write a professional email to {recipient} with subject '{subject}': {body}")
                generated_email = response.text.strip()

                # Combine user input + AI-generated email
                full_email_body = f"{body}\n\n---\n{generated_email}"

                # Encode parameters properly for Gmail compose
                params = urllib.parse.urlencode({
                    "view": "cm",
                    "to": recipient,
                    "su": subject,
                    "body": full_email_body
                })
                mailto_link = f"https://mail.google.com/mail/?{params}"

                print("Opening Gmail compose window...")
                webbrowser.open(mailto_link)
                return "Gmail compose window opened successfully!"

            except Exception as e:
                return f"Error: {str(e)}"

        else:
            return "Error: Invalid request type. Use 'youtube' or 'mail'."

# Example Usage:
# tools_instance = Tools()

# # Automatically Generate and Open Email Draft in Gmail
# email_data = {
#     "type": "mail",
#     "to": "example@example.com",
#     "subject": "Project Feedback Request",
#     "body": "Ask for feedback on the recent project I worked on."
# }
# print(tools_instance.forward(**email_data))
