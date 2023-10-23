with open('word to links.txt','r',encoding='UTF8') as fp:
	lines = fp.readlines()

with open('../../index.html','r',encoding='UTF8') as fp:
	html = fp.read()
    
for line in lines:
    word,link = line.strip().split(',')
    link = '<a href="'+link+'">'+word+'</a>'
    print(word,link)
    
    html = html.replace('>'+word+'<','>BLA<')
    html = html.replace(word, link)
    html = html.replace('>BLA<','>'+word+'<')

with open('../../index.html','w',encoding='UTF8') as fp:
	fp.write(html)