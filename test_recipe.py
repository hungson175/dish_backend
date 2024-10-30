import requests
import os

def test_recipe_endpoint(image_path):
    # API endpoint URL (adjust if your FastAPI server runs on a different port)
    url = "http://localhost:8000/get_recipe"
    
    # Prepare the files and data for the request
    files = {
        'image': ('image.jpg', open(image_path, 'rb'), 'image/jpeg')
    }
    
    data = {
        'message': 'Describe this dis \'Bo nuong la lot\' and provide the ingredients and recipe - all in Vietnamese'
    }
    
    # Make the POST request
    response = requests.post(url, files=files, data=data)
    
    # Print the response
    if response.status_code == 200:
        result = response.json()
        print("Recipe Description:")
        print(result['recipe'])
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Replace with the path to your local image
    image_path = "./food_image.jpg"
    test_recipe_endpoint(image_path)
