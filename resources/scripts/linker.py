with open('word to links.txt','r',encoding='UTF8') as fp:
	lines = fp.readlines()

with open('../../index.html','r',encoding='UTF8') as fp:
	html = fp.read()
    
for line in lines:
    word,link = line.strip().split(',')
    link = '<a href="'+link+'">'+word+'</a>'
    print(word,link)
    
    html = html.replace('>'+word+'</a>','>BLA</a>')
    for c in ' ,.\r\n':
        html = html.replace(word+c, link+c)
    html = html.replace('>BLA</a>','>'+word+'</a>')

with open('../../index.html','w',encoding='UTF8') as fp:
	fp.write(html)
