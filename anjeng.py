import requests

API_URL = "https://api-inference.huggingface.co/models/cagliostrolab/animagine-xl-3.1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "Astronaut riding a chicken",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
image.show()