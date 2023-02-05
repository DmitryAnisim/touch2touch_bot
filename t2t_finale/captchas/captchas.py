from captcha.image import ImageCaptcha
from random import randint
import os

def generate_captcha(user_id = 1):
    image = ImageCaptcha()
    key = str(randint(1000,9999))
    path = f'./captchas/captcha_{user_id}.png'
    image.generate(key)
    image.write(key, path)
    return key, path

def delete_all_captchas():
    captchas = [i for i in os.listdir('./captchas') if i.endswith('png') and i.startswith('captcha')]
    for i in captchas:
        os.remove(f'./captchas/{i}')

def delete_single_captcha(user_id):
    captchas = [i for i in os.listdir('./captchas') if str(user_id) in i]
    for i in captchas:
        os.remove(f'./captchas/{i}')

if __name__ == '__main__':
    key,path = generate_captcha(9412412451)
    print(key)