import os
import openai



openai.api_key = "" #please go get ur own lol
yida="Say a random phrase with approximately 10 words about how boring today is?"
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content":""+yida+""}
  ]
)
#print(yida)
#print(completion.choices[0].message) 
reply=completion.choices[0].message['content']
print(reply)