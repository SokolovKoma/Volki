from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import textwrap
from PIL import *
import telebot
import time
import markovify

token = "1215663903:AAHauF_WNa0abfzZXxH3iGskyR8XNex4w_Y"
bot = telebot.TeleBot(token=token)


@bot.message_handler(content_types=['text'])
def handler_text(message):
    text = message.text
    if text == '/start':
        while True:
            for i in range(1, len(os.listdir('volki'))):
                margin = offset = 40
                img = Image.open(f'volki/{i}.jpg')
                file = open('datik.txt', 'r')
                width = img.width
                height = img.height
                p = width * height
                a = file.read()
                file.close()
                m = markovify.Text(a)

                if p < 1000:
                    res = m.make_short_sentence(10)
                    font = ImageFont.truetype('us.ttf', 20)
                else:
                    res = m.make_short_sentence(80)
                    font = ImageFont.truetype('us.ttf', 40)
                time.sleep(10)
                draw = ImageDraw.Draw(img)
                string = res
                l = len(string) + 1
                if len(string) % 2 == 0:
                    part1 = string[0:l // 2]
                    part2 = string[l // 2:]
                else:
                    part1 = string[0:l // 2 + 1]
                    part2 = string[l // 2 + 1:]
                for line in textwrap.wrap(res, width=40):
                    draw.text((width / 1000, height / 2), part1, (255, 255, 255), font=font)
                    draw.text((width / 1000, height / 1.5), part2, (255, 255, 255), font=font)
                    offset += font.getsize(line)[1]
                img.save('volk4.jpg')
                bot.send_photo(-1001465032255, open('volk4.jpg', 'rb'))
    if text == '/exit':
        bot.send_message(-1001465032255, 'GoodBye')
        exit()


bot.polling(none_stop=True, interval=0)
