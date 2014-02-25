import feedparser
d = feedparser.parse('http://pavel.zaikin.pro/feeds/posts/default')
for e in d.entries:
	title = e.title.replace('"',"'")
	content = e.content
	f = open(title + ".html", "w",encoding='utf-8')
	f.write('<html><body>')
	f.write(content[0]['value'])
	f.write("</body></html>")
	f.close()

