import os
import openai

openai.api_key = "sk-5FnoGbFja1Gm1jDD4sRnT3BlbkFJ4HSCEGl6fFIglXt6Mv9-"

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)
