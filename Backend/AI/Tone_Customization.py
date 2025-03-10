import os
import google.generativeai as genai
from smolagents import Tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ToneCustomization(Tool):
    """
    This tool classifies the tone of the input text.

    Example tones: Formal, Informal, Friendly, Professional, Persuasive.
    """

    name = "ToneCustomization"
    description = """
    This tool analyzes the tone of a given text and classifies it into predefined categories: 
    'Formal', 'Informal', 'Friendly', 'Professional', or 'Persuasive'.
    
    It is useful in various applications, such as:
    - Refining communication style in emails, marketing content, or business proposals.
    - Ensuring appropriate tone in customer support or social media messages.
    - Adjusting text for a target audience by making it more formal, friendly, or persuasive.
    
    Example Queries:
    - "Analyze the tone of this email to ensure it sounds professional."
    - "What is the tone of this sales pitch?"
    - "Does this message sound too informal?"
    
    This tool leverages Google's `gemini-1.5-flash` model to provide **accurate** and **context-aware** tone classification.
    """
    inputs = {
        "text": {
            "type": "string",
            "description": "The input text to analyze for tone.",
        }
    }
    output_type = "string"

    def __init__(self):
        """Initializes the tool with Google Gemini API client."""
        super().__init__()
        api_key = os.getenv("GEMINI_API_KEY")  # ✅ Secure API Key Handling
        if not api_key:
            raise ValueError("Missing Gemini API key. Please set GEMINI_API_KEY in your .env file.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ Use Gemini Pro

    def forward(self, text: str) -> str:
        """
        Analyzes and classifies the tone of the given text.

        Args:
            text (str): The input text to analyze.

        Returns:
            str: The detected tone of the text.
        """
        try:
            # Define prompt for Gemini API
            prompt = (
                "Analyze the tone of the following text and classify it as one of these categories: "
                "'Formal', 'Informal', 'Friendly', 'Professional', 'Persuasive'.\n\n"
                f"Text: {text}\n\n"
                "Return only the tone category."
            )

            # Send request to Gemini API
            response = self.model.generate_content(prompt)

            # Extract the response text
            tone = response.text.strip()

            return f"The tone of the text is: {tone}"

        except Exception as e:
            return f"Error: {str(e)}. Please check your API key or model availability."

# Test the tool
# tp = ToneCustomization()
# print(tp.forward("Hey there! How's your day going?"))  # Expected: Friendly / Informal
# print(tp.forward("Dear Hiring Manager, I am excited to apply for this role."))  # Expected: Formal / Professional
# print(tp.forward("Buy now and get a 50% discount!"))  # Expected: Persuasive
