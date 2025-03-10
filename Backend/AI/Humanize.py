import google.generativeai as genai
from smolagents import tools
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Humanize(tools.Tool):
    """
    A smart AI-powered tool for crafting personalized and context-aware emails.

    This tool assists users in generating well-structured, engaging, and natural-sounding emails 
    tailored to different situations. Whether it's a formal business inquiry, a casual follow-up, 
    or a heartfelt thank-you message, this tool ensures the email aligns with the intended tone 
    and professionalism. It leverages Google's Gemini AI model to produce high-quality email drafts.

    Example use cases:
    - "Write a persuasive email to pitch my startup idea to an investor."
    - "Generate a friendly reminder email for an upcoming client meeting."
    - "Draft a professional networking email to reconnect with a former colleague."

    The tool ensures clarity, proper etiquette, and personalization, making each email impactful.
    """

    name = "SmartEmailComposer"
    description = (
        "This AI-powered email drafting assistant generates well-structured, personalized emails for various scenarios, "
        "such as professional communications, networking, invitations, and customer outreach. "
        "It tailors emails based on user input, ensuring the right tone and etiquette. "
        "Users can request specific email types, such as:\n"
        "- 'Write a warm and professional introduction email for a new business partnership.'\n"
        "- 'Draft a concise follow-up email after a job interview.'\n"
        "- 'Generate a thank-you email for a mentor's guidance.'\n"
        "The tool enhances readability, engagement, and professionalism to match the intended purpose."
    )

    inputs = {
    "prompt": {
        "type": "string",
        "description": (
            "Provide a brief text or message that needs to be humanized. Specify key details such as the tone, "
            "intended audience, and any important elements that should be retained while making the text sound "
            "more natural and engaging."
        ),
    }
}


    output_type = "string"

    def __init__(self):
        super().__init__()

    def forward(self, prompt: str) -> str:
        """
            Generates a natural, engaging, and human-like text based on user input.

            Args:
                prompt (str): A short description of the text’s purpose and key details.

            Returns:
                str: A refined, well-structured, and humanized version of the input text, or an error message if the process fails.
            """

        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel("gemini-1.5-pro") 
            response = model.generate_content(f"Refine and humanize the following text to make it more natural and engaging: {prompt}")
            return response.text.strip()
        except Exception as e:
            return f"Error: {str(e)}"


# # Example Usage:
# email_gen = Humanize()
# # prompt = "Write an email to thank a professor for their recommendation letter."
# print(email_gen.forward("Make this message more polite: 'Send me the report now.'"))
