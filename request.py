import requests
import json
def reqe():
    x=requests.get("http://saral.navgurukul.org/api/courses")
    with open("meraki1.json","w")as f:
        json.dump((x.json()),f,indent=4)
    a=x.json()
    count=0
    list=[]
    print("no.>>>>::<<<courses>>>>::<<<<<id")
    for i in a["availableCourses"]:
        print(count,i["name"],i['id'])
        list.append(i["id"])
        count=count+1
    b=int(input("enter your seriyal num:--"))
    r=requests.get("http://saral.navgurukul.org/api/courses/"+(list[b])+"/exercises")

    x=r.json()
    list1=[]
    count=0
    for i in x['data']:
        print(count,i['slug'])
        list1.append(i["slug"])    
        count+=1
    num=int(input("enter your slug num:--"))
    req=requests.get("http://saral.navgurukul.org/api/courses/"+str(b)+"/exercise/getBySlug?slug="+list1[num])
    v1=req.json()
    print(req)
    print("content",v1["content"])


    print("do you want previous content then type up")
    print("do you want next content then type next")
    print("do you want previous content then type previous")
    print("do you want previous content then type exit")
    i=0
    for i in range(len(list1)):
        num1=input("enter your next step:--")
        if num1=="up":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(b)+"/exercise/getBySlug?slug="+list1[num-1])
            v1=req.json()
            print(num-1,"content",v1["content"])
        if num1=="next":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(b)+"/exercise/getBySlug?slug="+list1[num+1])
            v1=req.json()
            print(num+1,"content",v1["content"])
        if num1=="previous":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(b)+"/exercise/getBySlug?slug="+list1[num])
            v1=req.json()
            print(num,"content",v1["content"])
        if num1=="exit":
            reqe()
reqe()
