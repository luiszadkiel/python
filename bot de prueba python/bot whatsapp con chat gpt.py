import openai
import credentials




openai.api_key = credentials.api_key




#enviar prompt desde el cmd
input = input("Prompt: ")

response = openai.completions.create(model='test-davinci-003',
                                     prompt= input,
                                     max_tokens= 2048
                                     )
completion = response.choices[0].text

print(completion)