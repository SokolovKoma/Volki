import requests
import json

all = ""
domain = 'public27456813'
count = 1000
token = 'a44af8afa44af8afa44af8af43a421aa2eaa44aa44af8aff964eece6179898ed8077f59'
url = "https://api.vk.com/method/wall.get?domain={}&count={}&access_token={}&v=5.95".format(domain, count, token)
ad = """🔥 Элитный мужской набор "DOMINIK" выгодно дополнит Ваш образ и заметно выделит Вас из толпы! Качество хирургической стали оставит приятное ощущение и прослужит Вам долго. Отличный подарок себе и близким. 🔥 
Заказать со скидкой:👉 vk.cc/au5Mdk 
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ 
В комплект "DOMINIK" входят: 
➡ современный и стильный крест "Steel Rage" с уникальным дизайном. 
➡ цепь "DOMINIK" , идеально сочетается с крестом! 
➡ мyжcкой Бpаcлет "DOMINIK" с 3-x cлoйным Зoлотым напылением! 
➡ Кольцо "Rock" с 3-x cлoйным Зoлотым напылением! 
Мужик осталось всего несколько комплектов по акции👉🏼 vk.cc/au5Mdk"""

response = requests.get(url)
answer = json.loads(response.text)
try:
    if "error" in answer:
        print(answer)
    for post in answer['response']['items']:
        if post['text'] == ad:
            continue
        all = all + post['text']
        f = open('datik.txt', 'w', newline="\n", encoding="utf-8")
        f.write(all)
        f.close()
except KeyError:
    all = all + ""
