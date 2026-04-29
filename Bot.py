import time
import random
import requests
from bs4 import BeautifulSoup

URL = "https://kolesa.kz/cars/bmw/e34/?year[from]=1994&price[to]=1500000"

sent = set()

messages = [
    "Салам. Живая или труп?",
    "Вложения есть? Сколько примерно?",
    "Краска родная или варилась?",
    "За сколько по факту отдашь?",
]

def get_cars():
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    
    cars = soup.find_all("a", class_="a-card__link")
    links = ["https://kolesa.kz" + car.get("href") for car in cars]
    
    return links

def send_whatsapp(link):
    text = random.choice(messages) + " " + link
    print("Отправка:", text)

while True:
    try:
        cars = get_cars()
        
        for car in cars:
            if car not in sent:
                send_whatsapp(car)
                sent.add(car)
                time.sleep(random.randint(60, 180))
                
        time.sleep(300)
        
    except Exception as e:
        print("Ошибка:", e)
        time.sleep(60)
