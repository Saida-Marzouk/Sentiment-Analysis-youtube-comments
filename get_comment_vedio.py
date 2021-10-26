


import googleapiclient.discovery


video_id = "xZn_JrIHfDE"


youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyBOBGXZBxLxvaTDtIwLz3DC8TNZl7BKZCc")

desc_dic = []

try:
    request = youtube.commentThreads().list( part="snippet,replies", videoId = video_id )
    res = request.execute()
    response =  res
    
    for key in res.keys():
        ncoms =(res['pageInfo']['totalResults'])
    for i in range(0,ncoms):
        rpcom = (res['items'][i]['snippet']['topLevelComment'] ['snippet']['textOriginal'])
        print(rpcom)   
           
        
        
except:
    print("No comments Available",video_id)
      

print(desc_dic)
