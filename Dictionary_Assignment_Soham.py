# Write a Python script to sort (ascending and descending) a dictionary by value.
dic={'ele1':'beta','ele2':'gamma','ele3':'alpha'}
def get_val(item):
    return item[1]
sorted_dict=dict(sorted(dic.items(),key=get_val))
rev_sort=dict(sorted(dic.items(),key=get_val,reverse=True))
print(sorted_dict)
print(rev_sort)


# Write a Python program to remove duplicates from the dictionary. 
def remove_dupe(dupe_dic):
    uniq_dic={}
    for key,value in dupe_dic.items():
        if value not in uniq_dic.values():
            uniq_dic[key]=value
    return uniq_dic
result=remove_dupe({'e1':2,'e2':5,'e3':5,'e4':8,'e5':2,'e6':3})
print(result)


# Write a Python program to combine two dictionary by adding values for common keys.
def combine_dict(d1,d2):
    dsum={}
    for key in d1:
        if key in d2:
            dsum[key]=int(d1[key])+int(d2[key])
        else:
            dsum[key]=int(d1[key])
    for key in d2:
        if key not in d1:
            dsum[key]=int(d2[key])
    return dsum
d1={'a':3,'b':4,'c':5,'d':6}
d2={'a':1,'b':2,'c':3,'e':6}
resul=combine_dict(d1,d2)
print(resul)


# Write a Python program to create a dictionary from a string. ( Track the count of the letters from the string.)
tracker=input("Enter the string: ")
dt={}
for i in tracker:
    if i in dt:
        dt[i]+=1
    else:
        dt[i]=1
print(dt)


# Write a Python program to match key and values both, in two dictionaries
def match_dict(dic1,dic2):
    ckey=0
    cval=0
    matches=[]
    for key in dic1:
        if key in dic2:
            ckey+=1
        if key in dic2 and dic1[key]==dic2[key]:
            cval+=1
    for key in dic1:
        if key in dic2 and dic1[key]==dic2[key]:
            matches.append((key,dic1[key]))

    print("The matching keys are:",ckey)
    print("The matching values are:",cval)
    print("The same key value pairs are:",matches)

dic1={'a':3,'b':4,'c':5,'d':6}
dic2={'a':1,'b':2,'c':5,'d':6}
match_dict(dic1,dic2)