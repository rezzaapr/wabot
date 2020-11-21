import json
import requests
from googletrans import Translator

class WABot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['messages']
        self.APIUrl = 'https://eu153.chat-api.com/instance197405/'
        self.token = 'wb79e26hfz0edwyl'
        print(self.dict_messages)
   
    def send_requests(self, method, data):
        url = f"{self.APIUrl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()
    
    def br(self, chatID):
        import requests as r
        import json
        from bs4 import BeautifulSoup as bs
        for message in self.dict_messages:
            tex = message['body']
            par = tex[5:]
            url = 'https://api.farzain.com/brainly.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z&'
            req= r.get(url)
            js = req.json()
            p= js[1]['url']
            reqq = r.get(p)
            be = bs(reqq.text, 'html.parser')
            find = be.find('div', class_='sg-text sg-text--break-words brn-rich-content js-answer-content')
            data = {
               "body": find.text,
               "chatId": chatID
            }
            answer = self.send_requests('sendMessage', data)
            return answer


    def en(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            par = text[11:]
            translator = Translator()
            result = translator.translate(par, src='en', dest='id')
            data = {
               "body": result.text,
               "chatId": chatID
            }
            answer = self.send_requests('sendMessage', data)
            return answer

    def idn(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            par = text[10:]
            translator = Translator()
            result = translator.translate(par, src='id', dest='en')
            data = {
               "body": result.text,
               "chatId": chatID
            }
            answer = self.send_requests('sendMessage', data)
            return answer

    def geo(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            from googlesearch import search 
            query = text[2:]
            for i in search(query, tld="com", num=10, stop=10, pause=5):
                data = {
                      "body" : "🔎 Results Pencarian Google :\n\n[1]" +i,
                      "chatId" : chatID
                      }
                answer = self.send_requests('sendMessage', data)
                return answer

    def yts(self, chatID):
        import pafy
        import urllib.request
        import re
        for message in self.dict_messages:
            text = message['body']
            html = requests.get("https://www.youtube.com/results?search_query="+text[4:])
            video_ids = re.findall(r"watch\?v=(\S{11})", html.text().decode())
            paf = pafy.new('https://www.youtube.com/watch?v=b'+video_ids[0])
            data = {
                  "body":'https://img.youtube.com/vi/'+video_ids[0],
                  "caption" : '🔎 *Hasil Pencarian Youtube Acak*\n\n*Judul Video* : '+paf.title,
                  "filename": 'jpg',
                  "chatId": chatID
                  }

            answer = self.send_requests('sendFile', data)
            return answer 

    def start(self, chatID):
        data = {
            "body": "🤖 _Halo Saya Adalah Recsec Bot, Ada Yang Bisa Saya Bantu?_\n\n*Admin :*\n\n📞 : 088299423038\n📱 : _fb.me/rezzapriatna12_ \n\n🚀 *Fitur* \n\n✅ _Youtube Downloader_ \n✅ _Facebook Downloader_ \n✅ _Instagram Downloader_ \n✅ _Google Search_ \n✅ _Text To Speech_ \n✅ _Stalking Profil Instagram_ \n✅ _Translate_ \n\n\n _Untuk Menampilkan Command Ketik_ *Menu*",
            "chatId": chatID
        }
        answer = self.send_requests('sendMessage', data)
        return answer

    def menu(self, chatID):
        data = {
              "body": '*List Of Command* :\n\n🔖 *tulis* _text_ ( Membuat Tulisan Dibuku )\n🔖 *ig* _url_ ( Unduh Video Instagram )\n🔖 *fb* _url_ ( Unduh Video Facebook )\n🔖 *ig-profil* _username_ ( Melihat Profil Instagram )\n🔖 *gs* _query_ ( Mencari Google Acak )\n🔖 *terjemahan* _text_ ( ENG > IDN )\n🔖 *translate* _text_ ( IDN > ENG )\n🔖 *tts* _text_ ( Mengubah Pesan Jadi Suara )\n🔖 *tanya* _pertanyaan_ ( Brainly Answer )',
              "chatId": chatID
              }
        answer = self.send_requests('sendMessage', data)
        return answer

    def er(self, chatID):
        p = "Yah Maaf:( Aku Gangerti Apa Yang Kakak Maksud, Kakak Bisa Ketik Start Atau Menu Untuk Menampilkn Apa Saja Yang Aku Bisa:)"
        data = {
              "body": p,
              "chatId": chatID
              }
        answer = self.send_requests('sendMessage', data)
        return answer

    def tts(self, chatID):
        for message in self.dict_messages:
            text = message['body'] 
            par = text[4:]
            data = {
                'chatId': chatID,
                'body': 'https://api.farzain.com/tts.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z&',
                'filename': 'hahah',
                'caption': 'example'
            }
            answer = self.send_requests('sendFile', data)
            return answer
    
    def fb(self, chatID):
        import requests as r
        import re
        for message in self.dict_messages:
            text = message['body'] 
            par = text[3:]
            html = r.get(par)
            video = re.search('sd_src:"(.+?)"', html.text).group(1)
            data = {
                'chatId': chatID,
                'body': video,
                'filename': 'hahah',
                'caption': '✅ *Video Berhasil Didownload*'
            }
            answer = self.send_requests('sendFile', data)
            return answer

    def igg(self, chatID):
        import requests as r
        for message in self.dict_messages:
            text = message['body'] 
            par = text[3:]
            a = r.get(par+'?__a=1')
            b = a.json()
            c = b['graphql']['shortcode_media']
            video = (c['video_url']) 
            data = {
                'chatId': chatID,
                'body': video,
                'filename': 'hahah',
                'caption': '✅ *Video Berhasil Didownload*'
            }
            answer = self.send_requests('sendFile', data)
            return answer


    def ig(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            tex = message['senderName']
            import requests as r
            import json
            par = text[10:]
            req= r.get('https://www.instagram.com/'+par+'/?__a=1')
            js1 = req.json()["graphql"]["user"]["biography"]
            js2 = req.json()["graphql"]["user"]["full_name"]
            js3 = req.json()["graphql"]["user"]["edge_followed_by"]["count"]
            js4 = req.json()["graphql"]["user"]["edge_follow"]["count"]
            js5 = req.json()["graphql"]["user"]["profile_pic_url_hd"]
            data = {
                  "chatId": chatID,
                  "body": js5,
                  "filename": 'png',
                  "caption" : '🔎 *Hasil Pencarian Instagram* \n\n*Username* : '+par+'\n*Nama* : '+str(js2)+'\n*Bio* : '+str(js1)+'\n*Followers* : '+str(js3)+'\n*Following* :'+str(js4)
                  
                  
                  }
            answer = self.send_requests('sendFile', data)
            return answer  


    def tulis(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            tex = message['senderName']
            import requests as r
            import json
            from nulis import tulis
            import base64
            par = text[5:]
            tulis=tulis(par)
            for i in tulis.tulis():
                i.save('gambar.jpg')
                image = open('gambar.jpg', 'rb')
                image_read = image.read()
                image_64_encode = base64.encodebytes(image_read)
                api = 'b76b9a5f05dafad41987044532b9e400'
                url = 'https://api.imgbb.com/1/upload'
                par = {
                 'key':api,
                 'image':image_64_encode,
                 'name':'nulis',
                 'expiration': 60
                }
                headers = {
                  'Accept': 'application/json'
                }
                req = r.post(url,data=par, headers=headers)
                p = req.json()['data']['display_url']
                data = {
                     "chatId": chatID,
                     "body": p,
                     "filename": 'png',
                     "caption" : '*Nih Ka Hasil Nya Maaf Kalo Jelek*'
                    }
                answer = self.send_requests('sendFile', data)
                return answer  

    def processing(self):
        if self.dict_messages != []:
            for message in self.dict_messages:
                text = message['body'].split()
                if not message['fromMe']:
                    id  = message['chatId']
                    if text[0].lower() == 'hi':
                        return self.welcome(id)
                    elif text[0].lower() == 'translate':
                        return self.idn(id)
                    elif text[0].lower() == 'terjemahan':
                        return self.en(id)
                    elif text[0].lower() == 'ig-profil':
                        return self.ig(id)
                    elif text[0].lower() == 'ig':
                        return self.igg(id)
                    elif text[0].lower() == 'start':
                        return self.start(id)
                    elif text[0].lower() == 'yts':
                        return self.yts(id)
                    elif text[0].lower() == 'fb':
                        return self.fb(id)
                    elif text[0].lower() == 'tts':
                        return self.tts(id)
                    elif text[0].lower() == 'gs':
                        return self.geo(id)
                    elif text[0].lower() == 'tulis':
                        return self.tulis(id)
                    elif text[0].lower() == 'tanya':
                        return self.br(id)
                    elif text[0].lower() == 'menu':
                        return self.menu(id)
                    else:
                        return self.er(id)
                else: return 'NoCommand'

            



        
        




