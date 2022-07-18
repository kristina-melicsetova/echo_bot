from requests import get

api_req = 'https://api.telegram.org/bot5373817312:AAFy7jBOLSXJgwyaHDjsuwbryHYj-w5FTOY'# ссылка на бота

updates = get(api_req + '/getUpdates?offset=-1').json() # получаем последнее сообщение и форматируем его в json

print(updates)

m = updates['result'][0]['message']

chat_id = m['from']['id']
text = m['text']
send_msg = get(api_req + f'/sendMessage?chat_id={chat_id}&text={text}')# ответ бота
