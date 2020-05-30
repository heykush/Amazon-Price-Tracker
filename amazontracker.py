import requests
from plyer import notification
from bs4 import BeautifulSoup
from time import sleep
url='https://www.amazon.in/Logitech-MK215-Wireless-Keyboard-Mouse/dp/B012MQS060/ref=sr_1_16?crid=2QQ3YMBOZECFT&dchild=1&keywords=wireless+keyboard+and+mouse+combo+for+laptop&qid=1590650010&sprefix=wireless+%2Caps%2C401&sr=8-16'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
wantedprice=1000

def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='gaurav',
        app_icon="C:\\Users\\gkush\\Downloads\\aa.ico",
        timeout=15
    )
if __name__ == "__main__":
    while True:
        page=requests.get(url, headers=headers)
        soup=BeautifulSoup(page.content,'html.parser')
        title=soup.find(id="productTitle").get_text().strip()
        price=(soup.find(id="priceblock_ourprice").get_text().strip())
        p=price[2:7].split(",")
        pp="".join(p)
        converted_price=int(pp)
        if converted_price>wantedprice:
            diff=converted_price-wantedprice
            ntitle='AMAZON TRACKER'
            nmessage=(f'''{title[:8]}{title[14:42]}\nCurrent Price: {price}\nIt's still {diff} expensive''')
            notifyme(ntitle, nmessage)
        else:
            ntitle='AMAZON TRACKER'
            nmessage='Hurraah !! Cheaper :)\nGo and Buy Now '
            notifyme(ntitle, nmessage)
        sleep(72000)

