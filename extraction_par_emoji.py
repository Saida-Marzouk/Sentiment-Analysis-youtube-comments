
import re
import emoji
import os
from pprint import pprint
import googleapiclient.discovery
import json
import csv


def text_has_emoji(text):
    for character in text:
        if character in emoji.UNICODE_EMOJI:
            return True
    return False




os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBOBGXZBxLxvaTDtIwLz3DC8TNZl7BKZCc"

youtube = googleapiclient.discovery.build( 
    api_service_name, api_version, developerKey = DEVELOPER_KEY)


video_id = "TJv9MsRSPeA"
                
def extract_emojis(a_list):
    emojis_list = map(lambda x: ''.join(x.split()), emoji.UNICODE_EMOJI.keys())
    r = re.compile('|'.join(re.escape(p) for p in emojis_list))
    aux=[','.join(r.findall(s)) for s in a_list]
    return(aux)
l_pos = ["\U0001f600","\U0001F601","\U0001F602","\U0001F603","\U0001F604","\U0001F60D","\U0001F618","\U0001F60A","\U00002764","\U0001F44C","\U0001F44F","😀","😃","😄","😁","😆","😅","😂","🤣","☺️","😊","😇","🙂","🙃","😉","😌","😍","😘","😗","😙","😚","😋","😛","😝","😎","🤩","👍","💪🏻","👏🏻","❤️"]
l_neg = ["\U0001F612","\U0001F629","\U0001F62D","\U0001F622","\U0001F623","\U0001F61E","\U0001F621","\U0001F620","💩","🍋","😑","😷","😏","😞","🤕","😖","😠","😫","😖","😰","😬","🙄","👎","😤","😢","🖕","❌","😡","🚫","😒","😕","😓","😒","😞","😔","😟","😕","🙁 ","😣","😖","😫","😩","😢","😤","😠","🤬","🤯","😱","😨","😰","😥","😓","🤗","🤭","😴","👎"]
         
try:
     request = youtube.commentThreads().list(part="snippet,replies",videoId = video_id, maxResults = 500 ,textFormat='plainText')
     res = request.execute()
     response =  res
     
     for key in res.keys():
                    ncoms =(res['pageInfo']['totalResults'])
     k_pos=0 
     k_neg=0               
     desc_dic = {}
     
     list_pos = {}
     list_neg = {}
     for i in range(0,ncoms):
         
                    #
           rpcom = (res['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
           d_items = ( rpcom )
           desc_dic[i] = ([d_items ])
           
           if(text_has_emoji(rpcom)==True) :
               print(desc_dic[i])
               list_emoji = "".join(extract_emojis(desc_dic[i])[0:1])
               if(list_emoji[0:1] in l_pos) :
                   
                   #print ("positif",k_pos)
                   #print(list_emoji[0:1] )
                   list_pos[k_pos]=(d_items,)
                   k_pos=k_pos+1
                   #with open("desc_pos.json", 'a') as json_file:
                       #json.dump(desc_dic2[i],json_file,indent=4)
               if(list_emoji[0:1] in l_neg) :
                   #print ("negatif")
                   #print(list_emoji[0:1] )
                   list_neg[k_neg]=(d_items,)
                   k_neg=k_neg+1
     with open("desc_pos.json", 'a+') as json_file2:
         json.dump(list_pos,json_file2,indent=4)          
     with open("desc_neg.json", 'a+') as json_file3:
         json.dump(list_neg,json_file3,indent=4)      
           #with open("desc.json", 'a') as json_file:
                #json.dump(desc_dic[i],json_file,indent=4)
    # with open("pos_neg.json", 'w') as json_file2:
         #json.dump(desc_dic,json_file2,indent=4)  
     #print(desc_dic)
     i=0
     
    #for b in desc_dic:
         #b2=extract_emojis(desc_dic[b])
         #print(desc_dic[b])
         #if any(word in b2[0] for word in l_pos):
             #if not(any(word in b2[0] for word in l_neg)):
                 #print(b[0])
     
                
         
               
except:
    print("No comments Available - Write minimum to csv")
    
    






