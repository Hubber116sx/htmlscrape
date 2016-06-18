import urllib2
from  urllib2 import urlopen
import re 
from bs4 import BeautifulSoup 
from urlparse import urljoin
import csv
import httplib
import sys,getopt

class walk:
    starturl= 'http://www.globalscape.com/'
    visited = []
    checked = []
    errors = []
    redirects = [] 
    errorfile='errors.csv'
    visitedfile='visited.csv'
    def start(self,starturl):
        self.starturl=starturl
        self.perform(self.starturl,'/')
        print self.errors

    def perform(self, pageurl,parent):
        links = self.extractLinks(pageurl,urljoin(self.starturl,parent))
        if links:
            for link in links:
                # if the link is on this same site and we haven't visisted it yet, then drill into iti
                if link.startswith(self.starturl):
                    if not self.haveVisited(link):
                        print "visiting " + link + " from " + pageurl
                        self.perform(link,pageurl)

        
    def checkForErrors(self,url,parent):
        err = None
        try:
            if not self.haveVisited(url) and not url in self.redirects:
                req = urllib2.Request(url,headers={"User-Agent":"Magic Browser"})
                page = urlopen(req)
                # handle redirect
                if urljoin(self.starturl,page.url) != url:
                    self.redirects.append(url)
                    req = urllib2.Request(url,headers={"User-Agent":"Magic Browser"})
                    err = ('Redirect Detected from: ', url,  page.url)
                    page = urlopen(req)
                    url = urljoin(self.starturl,page.url)
                if not self.haveVisited(url):    
                    self.visited.append(url)
            #print 'loaded  ' + url
                    with open(self.visitedfile,'a+') as f:
                        writer = csv.writer(f,delimiter=',')
                        writer.writerow((parent,url))
                    return page
            else:
                return None
        except urllib2.HTTPError, e:
            err = ('HTTPError = ' + str(e.code),parent,url)
        except urllib2.URLError, e:
            err = ('URLError = ' + str(e.reason),parent,url)
        except httplib.HTTPException, e:
            err = ('HTTPError (no code)', parent, url)
        except Exception:
            err = ('Unknown error', parent, url)
        self.printToError(err)  

    def printToError(self,err):
        print err
        with open(self.errorfile, 'a+') as f:
            writer = csv.writer(f,delimiter=',')
            writer.writerow(err)

    def haveVisited(self,url):
        if url in self.visited:
            return True
        else:
            return False    
        
    def extractLinks(self,page,parent):
        #print 'before everything'
        links = []
        try:
            #print 'before check 4 errors'
            p = self.checkForErrors(urljoin(self.starturl,page),parent)
            if p:
                #print ' checkforerrors done '
                content = BeautifulSoup(p)
                for link in content.find_all('a'):
                    linkhref = link.get('href')
                    if linkhref:
                        #print ' considering ' + str(linkhref)
                        links.append(urljoin(self.starturl,linkhref))
                return links
            else:
                return None
        except Exception ,e:
            print 'error on ' + page + " " + str(e)

def main(argv):
    starturl = ''
    try:
        opts, args = getopt.getopt(argv,"hs:",["starturl="])
    except getopt.GetoptError:
        print 'walk.py -s <starturl>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'walk.py -s <starturl>'
            sys.exit()
        elif opt in ("-s", "--starturl"):
            starturl = arg
    x = walk()
    x.start(starturl)
if __name__ == '__main__':
    main(sys.argv[1:])
