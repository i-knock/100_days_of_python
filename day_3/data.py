'''
Variation of the original code.

The data is now queried from an API every time the program is ran.
Base64 is requested and then decoded for best readibility of the questions.
'''
import base64
import requests
payload = {'amount': 10, 'type': 'boolean', 'encode': 'base64'}
r = requests.get('https://opentdb.com/api.php', params = payload)
print(r.json(), '\n')
information = r.json()['results']

question_data = list()
for result in information:
	# first decode b64 into bytes, then bytes into unicode
	question = base64.b64decode(result['question']).decode('utf-8')
	answer = base64.b64decode(result['correct_answer']).decode('utf-8')
	question_data.append({'text': question, 'answer': answer})
