import os
import openai

# api키 마지막자 수정해야 함
openai.api_key = "sk-5FnoGbFja1Gm1jDD4sRnT3BlbkFJ4HSCEGl6fFIglXt6Mv9-"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=" How have you been, friend?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
