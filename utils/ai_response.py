import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, TextContentItem, ImageContentItem, ImageUrl
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()
endpoint = "https://models.github.ai/inference"
model = "gpt-4o-mini"
token = os.getenv("sir_token", "")

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def get_completion(user_message, images=None, system_message="You are a helpful assistant."):
    """
    Get a completion from the AI model.
    
    Args:
        user_message: The user's message/question
        images: Optional list of base64 image strings
        system_message: The system prompt (default: "You are a helpful assistant.")
    
    Returns:
        The model's response
    """
    content = [TextContentItem(text=user_message)]
    
    if images:
        for img_base64 in images:
            # Ensure base64 string has the correct prefix
            if not img_base64.startswith("data:image"):
                img_data = f"data:image/png;base64,{img_base64}"
            else:
                img_data = img_base64
            content.append(ImageContentItem(image_url=ImageUrl(url=img_data)))

    response = client.complete(
        messages=[
            SystemMessage(system_message),
            UserMessage(content=content),
        ],
        model=model
    )
    return response.choices[0].message.content