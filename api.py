import requests,json,os,pprint
try:
    if os.path.exists ('act.json'):
        f=open('act.json')
        s=f.read()
        s=json.loads(s)
        f.close()
    else:
        link='https://saral.navgurukul.org/api/courses'
        res=requests.get(link)
        soup=res.text
        s=json.loads(soup)
finally:
    li=[]
    d=0
    for j in s['availableCourses']:
        print(str(d)+'.',j['name'])
        d+=1
        li.append(j)
    inp=int(input('enter your id:-\n'))
    for j in range(len(li)):
        s=li[j]
        if inp==j:
            for k in s :
                link1='https://saral.navgurukul.org/api/courses/'+s['id']+'/exercises'
                res1=requests.get(link1).text
                r=json.loads(res1)
    s=1
    lis=[]
    for j in r['data']:
        lis1=[]
        print(str(s)+'.',j['name'])
        sl=link1[:-1]+'/getBySlug?slug='+j['slug']
        # print(sl)
        t=j['childExercises']
        lis1.append(sl)
        c=1
        for l in t:
            res2=link1[:-1]+'/getBySlug?slug='+l['slug']
            z=str(s)+'.'+str(c)
            print('         ',z,l['name'])
            a={z:res2}
            lis.append(a)
            lis1.append(res2)
            c+=1
        b={s:lis1}
        lis.append(b)
        s+=1
    n=input('enter a sequence \n')
    for k in lis:
        for j in k:
            try:
                if n==j:
                    res3=requests.get(k[j]).text
    
            
                    res3=json.loads(res3)
                    q=json.loads(res3['content'])
                    q=q[0]['value']
                    print(q.strip())
                if int(n)==j:
                    c=1
                    for g in k[j]:
                        print(g)
                        res3=requests.get(g).text
                        res3=json.loads(res3)
                        q=json.loads(res3['content'])
                        q=q[0]['value']
                        print(str(c)+'.',q.strip())
                        c+=1
            except Exception as e:
                pass
            
  