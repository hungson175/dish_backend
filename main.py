import base64
import os
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, UploadFile
from openai import OpenAI
load_dotenv()
app = FastAPI()


@app.post("/get_recipe")
async def get_recipe(
    image: UploadFile = File(...),
    message: str = Form("Describe this dish and provide the ingredients and recipe")
):
    try:
        # Read the image file data
        image_bytes = await image.read()
        
        # Encode the image to base64
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")
        
        # Initialize OpenAI client
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Prepare the message for GPT-4 Vision
        response = client.chat.completions.create(
            # model="gpt-4-vision-preview",
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": message},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1000
        )
        
        # Extract the response
        recipe_description = response.choices[0].message.content
        
        return {"recipe": recipe_description}

    except Exception as e:
        return {"error": str(e)}

@app.get("/get_my_name")
async def get_my_name():
    return {"name": "John Doe"}
