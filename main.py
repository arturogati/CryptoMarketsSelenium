from selenium import webdriver
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip



prostocashbuy=()
xchangebuy=()
platexbuy=()
cekbuy=()
ychangerbuy=()
prostocashsell=()
xchangesell=()
platexsell=()
ychangersell=()
ceksell=()

class Cripto_change:
    def __init__(self):
        print("start")

    def sigint_handler(self):
        print('Прерывание')

    def Telegram_bot(self, text):
        token = ""
        chat_id = "-"
        url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
        results = requests.get(url_req)
        print(results.json())






    def check(self):
        browser = webdriver.Chrome()
        browser.get("https://prostocash.com/sberbank-na-litecoin.html")
        browser.maximize_window()
        summ = browser.find_elements(By.NAME, "summ1")
        for i in summ:
            i.send_keys()
        time.sleep(5)
        ltc = browser.find_elements(By.NAME, "summ2")
        for i2 in ltc:
            i2.click()
            i2.send_keys(Keys.CONTROL + "A")
            time.sleep(4)
            i2.send_keys(Keys.CONTROL + "C")
            time.sleep(3)
            n = pyperclip.paste()
            m = (int(n))


    def prostocash_buy(self):
        global prostocashbuy
        browser = webdriver.Chrome()
        browser.get("https://prostocash.com/sberbank-na-litecoin.html")
        browser.maximize_window()
        ltc = browser.find_elements(By.NAME, "summ2")
        for i in ltc:
            i.send_keys("4")
        time.sleep(4)
        summ = browser.find_elements(By.NAME, "summ1")
        for i2 in summ:
            i2.click()
            i2.send_keys(Keys.CONTROL + "A")
            time.sleep(4)
            i2.send_keys(Keys.CONTROL + "C")
            time.sleep(3)
            prostocashbuy = pyperclip.paste()
            float(prostocashbuy)
            browser.close()

    def prostocash_sell(self):
        global prostocashsell
        browser = webdriver.Chrome()
        browser.get("https://prostocash.com/litecoin-na-sberbank.html")
        browser.maximize_window()
        ltc = browser.find_elements(By.NAME, "summ1")
        for i in ltc:
            i.send_keys("4")
        time.sleep(4)
        summ = browser.find_elements(By.NAME, "summ2")
        for i2 in summ:
            i2.click()
            i2.send_keys(Keys.CONTROL + "A")
            time.sleep(4)
            i2.send_keys(Keys.CONTROL + "C")
            time.sleep(3)
            prostocashsell = pyperclip.paste()
            float(prostocashsell)
            browser.close()


    def xchange_buy(self):
        global xchangebuy
        browser = webdriver.Chrome()
        browser.get("https://xchange.cash/sberbank-to-litecoin.html")
        browser.maximize_window()
        ltc = browser.find_elements(By.NAME, "summ2")
        for i in ltc:
            i.send_keys("4")
        time.sleep(4)
        summ = browser.find_elements(By.NAME, "summ1")
        for i2 in summ:
            i2.click()
            i2.send_keys(Keys.CONTROL + "A")
            time.sleep(4)
            i2.send_keys(Keys.CONTROL + "C")
            time.sleep(3)
            xchangebuy = pyperclip.paste()
            float(xchangebuy)
            browser.close()


    def xchange_sell(self):
        global xchangesell
        browser = webdriver.Chrome()
        browser.get("https://xchange.cash/litecoin-to-sberbank.html")
        browser.maximize_window()
        ltc = browser.find_elements(By.NAME, "summ1")
        for i in ltc:
            i.send_keys("4")
        time.sleep(4)
        summ = browser.find_elements(By.NAME, "summ2")
        for i2 in summ:
            i2.click()
            i2.send_keys(Keys.CONTROL + "A")
            time.sleep(4)
            i2.send_keys(Keys.CONTROL + "C")
            time.sleep(3)
            xchangesell = pyperclip.paste()
            float(xchangesell)
            browser.close()

    def platex_buy(self):
        global platexbuy
        browser = webdriver.Chrome()
        browser.get("https://platex.org/xchange_SBERRUB_to_ltc/")
        browser.maximize_window()
        ltc = browser.find_elements(By.NAME, "summ2")
        for i in ltc:
            i.click()
            i.send_keys(Keys.BACKSPACE)
            i.send_keys("4")
        time.sleep(4)
        summ = browser.find_elements(By.NAME, "summ1")
        for i2 in summ:
            i2.click()
            i2.send_keys(Keys.SPACE)
            i2.send_keys(Keys.CONTROL + "A")
            time.sleep(4)
            i2.send_keys(Keys.CONTROL + "C")
            time.sleep(3)
            platexbuy = pyperclip.paste()

            float(platexbuy)
            browser.close()




    def ychanger_buy(self):
        global ychangerbuy
        browser = webdriver.Chrome()
        browser.get("https://ychanger.net/sberbank-na-litecoin.html")
        browser.maximize_window()
        ltc = browser.find_elements(By.NAME, "summ2")
        for i in ltc:
            i.send_keys("4")
        time.sleep(4)
        summ = browser.find_elements(By.NAME, "summ1")
        for i2 in summ:
            i2.click()
            i2.send_keys(Keys.CONTROL + "A")
            time.sleep(4)
            i2.send_keys(Keys.CONTROL + "C")
            time.sleep(3)
            ychangerbuy = pyperclip.paste()
            float(ychangerbuy)
            browser.close()


    def ychanger_sell(self):
        global ychangersell
        browser = webdriver.Chrome()
        browser.get("https://ychanger.net/litecoin-na-sberbank.html")
        browser.maximize_window()
        ltc = browser.find_elements(By.NAME, "summ1")
        for i in ltc:
            i.send_keys("4")
        time.sleep(4)
        summ = browser.find_elements(By.NAME, "summ2")
        for i2 in summ:
            i2.click()
            i2.send_keys(Keys.CONTROL + "A")
            time.sleep(4)
            i2.send_keys(Keys.CONTROL + "C")
            time.sleep(3)
            ychangersell = pyperclip.paste()
            float(ychangersell)
            browser.close()




    def cek_buy(self):
        global cekbuy
        browser = webdriver.Chrome()
        browser.get("https://60cek.org/obmen-sberbank-na-litecoin.html")
        browser.maximize_window()
        ltc = browser.find_elements(By.NAME, "summ2")
        for i in ltc:
            i.send_keys("4")
        time.sleep(4)
        summ = browser.find_elements(By.NAME, "summ1")
        for i2 in summ:
            i2.click()
            i2.send_keys(Keys.CONTROL + "A")
            time.sleep(4)
            i2.send_keys(Keys.CONTROL + "C")
            time.sleep(3)
            cekbuy = pyperclip.paste()
            float(cekbuy)
            browser.close()

    def cek_sell(self):
        global ceksell
        browser = webdriver.Chrome()
        browser.get("https://60cek.org/obmen-litecoin-na-sberbank.html")
        browser.maximize_window()
        ltc = browser.find_elements(By.NAME, "summ1")
        for i in ltc:
            i.send_keys("4")
        time.sleep(4)
        summ = browser.find_elements(By.NAME, "summ2")
        for i2 in summ:
            i2.click()
            i2.send_keys(Keys.CONTROL + "A")
            time.sleep(4)
            i2.send_keys(Keys.CONTROL + "C")
            time.sleep(3)
            ceksell = pyperclip.paste()
            float(ceksell)
            browser.close()






    def run(self):


        self.prostocash_buy()
        #self.platex_buy()
        self.xchange_buy()
        self.cek_buy()
        self.ychanger_buy()

        self.prostocash_sell()
        #self.platex_sell()
        self.xchange_sell()
        self.cek_sell()
        self.ychanger_sell()

        forsellmax=(xchangesell, ychangersell, ceksell)

        forbuymin=( xchangebuy, ychangerbuy, cekbuy)


        Tobuy=()
        Tosell=()

        #minIndexbuy = forbuymin.index(max(forbuymin))
        #if minIndexbuy == 0:
            #a=str(platexbuy)
            #Tobuy = ("Platex" + " " + a)


        minIndexbuy = forbuymin.index(max(forbuymin))
        if minIndexbuy == 1:
            b=str(xchangebuy)
            Tobuy = ("Xchange" + " " + b)


        minIndexbuy = forbuymin.index(max(forbuymin))
        if minIndexbuy == 2:
            c=str(ychangerbuy)
            Tobuy=("Ychanger"+ " " + c)


        minIndexbuy = forbuymin.index(max(forbuymin))
        if minIndexbuy == 3:
            d=str(cekbuy)
            Tobuy=("60cek" + " " + d)






        maxIndexsell = forsellmax.index(max(forsellmax))
        if maxIndexsell == 0:
            a=str(xchangebuy)
            Tosell=("Xchange" + " " + a)

        maxIndexsell = forsellmax.index(max(forsellmax))
        if maxIndexsell == 1:
            b=str(ychangersell)
            Tosell=("Ychanger" + " " + b)

        maxIndexsell = forsellmax.index(max(forsellmax))
        if maxIndexsell == 2:
            c=str(ceksell)
            Tosell=("60cek" + " " + c)



        massage=(Tobuy + "-" + Tosell)
        self.Telegram_bot(massage)

        print(forbuymin)
        print(forsellmax)































