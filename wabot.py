import json
import requests


class WABot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['messages']
        self.APIUrl = 'https://eu81.chat-api.com/instance133843/'
        self.token = '8r40flia6zqtu8io'
        print(self.dict_messages)
   
    def send_requests(self, method, data):
        url = f"{self.APIUrl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def tts(self, chatID):
        data = {
        "audio" : 'https://api.farzain.com/tts.php?id=rezza&apikey=JsaChFteVJakyjBa0M5syf64z&',
        "chatId" : chatID }
        return self.send_requests('sendAudio', data)

    def geo(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            from googlesearch import search 
            query = text[2:]
            for i in search(query, tld="com", num=10, stop=10, pause=2):
                data = {
                      "body" : "🔎 Results :\n" +i,
                      "chatId" : chatID
                      }
                answer = self.send_requests('sendMessage', data)
                return answer

    def yts(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            import requests as r
            import json
            par = text[3:]
            req= r.get('http://api.farzain.com/yt_search.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z&')
            js1 = req.json()[1]['title']
            js2 = req.json()[1]['url']
            js3 = req.json()[1]['videoThumbs']
            js4 = req.json()[1]['videoId']
            data = {
                  "body": js3,
                  "caption" : '🔎 *Hasil Pencarian Youtube Acak*\n\n *Judul Video* : '+js1+'\n\n*Url Video* :'+js2+'\n\n*Video ID* :'+js4,
                  "filename": 'jpg',
                  "chatId": chatID
                  }

            answer = self.send_requests('sendFile', data)
            return answer 

    def menu(self, chatID):
        data = {
              "body": '*List Of Command* :\n\n*[x>]* _yt query_\n*[x>]* _ig username_ \n*[x>]* _gs query_',
              "chatId": chatID
              }
        answer = self.send_requests('sendMessage', data)
        return answer

    def ig(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            import requests as r
            import json
            par = text[3:]
            req= r.get('https://www.instagram.com/'+par+'/?__a=1')
            js1 = req.json()['graphql']['user']['biography']
            js2 = req.json()['graphql']['user']['full_name']
            js3 = req.json()["graphql"]["user"]["edge_followed_by"]["count"]
            js4 = req.json()["graphql"]["user"]["edge_follow"]["count"]
            js5 = req.json()["graphql"]["user"]["profile_pic_url_hd"]
            data = {
                  "body": js5,
                  "caption" : '🔎 *Hasil Pencarian Instagram* \n\n*Username* : '+par+'\n*Nama* : '+js2+'\n*Bio* : '+js1+'*Followers* : '+str(js3)+'\n*Following* :'+str(js4),
                  "filename": 'png',
                  "phone": chatID
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
                    elif text[0].lower() == 'time':
                        return self.time(id)
                    elif text[0].lower() == 'chatid':
                        return self.show_chat_id(id)
                    elif text[0].lower() == 'ig':
                        return self.ig(id)
                    elif text[0].lower() == 'file':
                        return self.file(id, text[1])
                    elif text[0].lower() == 'yt':
                        return self.yts(id)
                    elif text[0].lower() == 'gs':
                        return self.geo(id)
                    elif text[0].lower() == 'menu':
                        return self.menu(id)
                    else:
                        return self(id)
                else: return 'NoCommand'

            



        
        




