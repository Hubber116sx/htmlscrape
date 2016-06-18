from walk import walk
import os

os.environ['http_proxy']=''
p = 'http://www.spiegel.de'
w = walk()
print 'walk created'
l = w.extractLinks(p,'root')
print 'extracted links'


