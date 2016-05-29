from  urllib2 import urlopen
import re 
from bs4 import BeautifulSoup 
from urlparse import urljoin
 
class walk:
	starturl= 'http://www.globalscape.com/'
	visited = []

	def start(self):
		self.perform(self.starturl)

	def perform(self, pageurl):
		links = self.extractLinks(pageurl)
		if links:
			self.visited.append(pageurl)
			for link in links:
				joinedurl = urljoin(self.starturl, link)
				if  joinedurl.startswith(self.starturl):
					if not self.haveVisited(joinedurl):
						print "visiting " + joinedurl
						self.visited.append(joinedurl)
						self.perform(joinedurl)

		
	def haveVisited(self,url):
		if url in self.visited:
			return True
		else:
			return False	
		
	def extractLinks(self,page):
		links = []
		try:
			page = BeautifulSoup(urlopen(page),"html5lib")
			for link in page.find_all('a'):
				linkhref = link.get('href')
				if linkhref:
					#print ' considering ' + linkhref
					links.append(linkhref)
			return links
		except:
			print 'error loading ' + page

if __name__ == '__main__':
	x = walk()
	x.start()
