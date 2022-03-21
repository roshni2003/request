import requests
import json
def reqe():
    x=requests.get("http://saral.navgurukul.org/api/courses")
    with open("meraki1.json","w")as f:
        json.dump((x.json()),f,indent=4)
    a=x.json()
    c=0
    n=[]
    print("no.>>>>::<<<courses>>>>::<<<<<id")
    for i in a["availableCourses"]:
        print(c,i["name"],i['id'])
        n.append(i["id"])
        c=c+1
    b=int(input("enter your seriyal num:--"))
    r=requests.get("http://saral.navgurukul.org/api/courses/"+(n[b])+"/exercises")

    x=r.json()
    n1=[]
    c=0
    for i in x['data']:
        print(c,i['slug'])
        n1.append(i["slug"])    
        c+=1
    num=int(input("enter your slug num:--"))
    req=requests.get("http://saral.navgurukul.org/api/courses/"+str(b)+"/exercise/getBySlug?slug="+n1[num])
    v1=req.json()
    print(req)
    print("content",v1["content"])


    print("do you want previous content then type up")
    print("do you want next content then type next")
    print("do you want previous content then type previous")
    print("do you want previous content then type exit")
    i=0
    for i in range(len(n1)):
        num1=input("enter your next step:--")
        if num1=="up":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(b)+"/exercise/getBySlug?slug="+n1[num-1])
            v1=req.json()
            print(num-1,"content",v1["content"])
        if num1=="next":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(b)+"/exercise/getBySlug?slug="+n1[num+1])
            v1=req.json()
            print(num+1,"content",v1["content"])
        if num1=="previous":
            req=requests.get("http://saral.navgurukul.org/api/courses/"+str(b)+"/exercise/getBySlug?slug="+n1[num])
            v1=req.json()
            print(num,"content",v1["content"])
        if num1=="exit":
            reqe()
reqe()