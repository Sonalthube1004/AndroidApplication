import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
#from plyer import notification
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from bs4 import BeautifulSoup as bs
import requests

class MainWindow(Screen, Widget) :
    script_id = StringProperty('')
    def notify_me(self):
    	
        dict = {'ADANIPORTS':'mundra-port-special-eco.-zone', 'AMBUJACEM':'ambuja-cements', 'ASIANPAINT':'asian-paints', 'AUROPHARMA':'aurobindo-pharma', 'AXISBANK':'axis-bank', 
        'BAJAJ-AUTO':'bajaj-auto', 'BAJFINANCE':'bajaj-finance', 'BPCL':'bharat-petroleum', 'BHARTIARTL':'bharti-airtel', 'INFRATEL':'bharti-infratel-ltd', 'BOSCHLTD':'bosch',
        'CIPLA':'cipla', 'COALINDIA':'coal-india', 'DRREDDY':'dr-reddys-laboratories', 'EICHERMOT':'eicher-motors', 'GAIL':'gail-(india)', 'HCLTECH':'hcl-technologies',
        'HDFCBANK':'hdfc-bank-ltd', 'HEROMOTOCO':'hero-motocorp', 'HINDALCO':'hindalco-industries', 'HINDPETRO':'hindustan-petroleum', 'HINDUNILVR':'hindustan-unilever',
        'HDFC':'housing-development-finance', 'ITC':'itc', 'ICICIBANK':'icici-bank-ltd', 'IBULHSGFIN':'indiabulls', 'IOC':'indian-oil-corporation', 'INDUSINDBK':'indusind-bank',
        'INFY':'infosys', 'KOTAKBANK':'kotak-mahindra-bank', 'LT':'larsen---toubro', 'LUPIN':'lupin', 'M&M':'mahindra---mahindra', 'MARUTI':'maruti-suzuki-india',
        'NTPC':'ntpc', 'ONGC':'oil---natural-gas-corporation', 'POWERGRID':'power-grid-corp.-of-india', 'RELIANCE':'reliance-industries', 'SBIN':'sbi-nifty-junior',
        'SUNPHARMA':'sun-pharma-advanced-research', 'TCS':'tata-consultancy-services', 'TATAMOTORS':'tata-motors-ltd', 'TATASTEEL':'tata-steel', 'TECHM':'tech-mahindra',
        'ULTRACEMCO':'ultratech-cement', 'UPL':'united-phosphorus', 'VEDL':'sesa-goa', 'WIPRO':'wipro-ltd', 'YESBANK':'yes-bank', 'ZEEL':'zee-entertainment-enterprises', 'BAJAJFINSV':'bajaj-finserv-limited' } 
        ticker1 = self.manager.ids.main_w.ids["script_id"].text
        ticker = dict.get(ticker1.upper())
        script_link = 'https://in.investing.com/equities/' + ticker #unique target link for the selected script
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'}
        response = requests.get(script_link, headers = headers)
        content =  response.content
        soup1 = bs(content, 'html.parser') 
        current_price_1 = soup1.find("bdo", class_ = "last-price-value js-streamable-element")
        x = str(current_price_1.get_text())
        y = x.replace(',', '')
        buy_target = round(float(self.manager.ids.main_w.ids["high_id"].text) * 0.01,2) + float(self.manager.ids.main_w.ids["high_id"].text)
        sell_target = float(self.manager.ids.main_w.ids["low_id"].text) - round(float(self.manager.ids.main_w.ids["low_id"].text) * 0.01,2)
        current_price = float(y)
        current_price = float(y)
        if current_price >= float(self.manager.ids.main_w.ids["high_id"].text):
            popup1 = Popup(title ='High Triggered', title_align = 'center', title_size = 20, size_hint = (None, None), size = (250,150), content = Label(text = 'Target : ' + str(buy_target)))   
            popup1.open() 
            self.sound = SoundLoader.load("High.wav")
            self.sound.play()
        if current_price <= float(self.manager.ids.main_w.ids["low_id"].text):
            popup2 = Popup(title ='Low Triggered', title_align = 'center', title_size = 20, size_hint = (None, None), size = (250,150), content = Label(text = 'Target : ' + str(sell_target)))   
            popup2.open() 
            self.sound = SoundLoader.load("Low.wav")
            self.sound.play()
        # schedule.every(10).seconds.do()
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)
     
    

class LoginPage(Screen, Widget):

    def verify_credentials(self):
        if self.ids["login_id"].text == "Capital" and self.ids["pass_id"].text == "Nest":
            self.manager.current = "main"
        else:
            popup = Popup(title ='Invalid Credentials!', title_align = 'center', title_size = 20, size_hint = (None, None), size = (250,150), content = Label(text = 'Press the Screen'))   
            popup.open() 
            self.manager.current = "login"

    

class SecondWindow(Screen, Widget):
    def run(self):
        
        MainWindow.notify_me(self)

        
class WindowManager(ScreenManager):
    pass





class MyApp(App): 
    def build(self):
        
        kv = Builder.load_file("og.kv")
        return kv
        
        

   
   

if __name__ == "__main__":
    MyApp().run()
