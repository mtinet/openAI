import os
import openai
import requests

# api키 마지막자 수정해야 함
openai.api_key = "sk-5FnoGbFja1Gm1jDD4sRnT3BlbkFJ4HSCEGl6fFIglXt6Mv9-"

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

# print(image_url)

# 이미지 가져오기
image = requests.get(image_url)
img = image.open(BytesIO(image.content))

# 이미지 보여주기
img.show()
