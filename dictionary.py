dic = {2:'bb'}
dic2 = {4:'dd'}
#del dic[2]
'''print dic.items()
print len(dic)
dic.update(dic2)
print dic.items()'''
#dic.clear()
dic.update({5:'tt'})
print dic.items()
print dic.get(5)
print dic.has_key(2)
print cmp(dic2, dic)