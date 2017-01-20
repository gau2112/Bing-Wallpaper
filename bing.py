
import urllib2
import urllib
import sys
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime


now = datetime.datetime.now()
save_path = 'Path to save the image'
url = "http://bingwallpaper.com/"
wallpaper = '/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://'
final='notify-send "Wallpaper Changed"'
#os.system(final)
#exit()
try:
	req = urllib.urlopen(url).read()
	#print req
	soup = BeautifulSoup(req)
	#k1 = soup.findAll('div',class_='panel')
	k = soup.findAll('div',class_='panel')[0]
	#for k in k1: 
	p = k.find('img')
	q = k.find('a')
	#print q['title']
	filename = q['href']
	url = p['src']
	fname =  filename.split('.')[0] + '.jpg'
	complete_path = os.path.join(save_path,fname)
	new_wallpaper =  wallpaper + complete_path
	#exit()
	#print complete_path
	#print url
	try:
		req = urllib.urlopen(url)
	#print req
		f = open(complete_path,'wb')
		f.write(req.read())
		f.close()
		os.system(new_wallpaper)
		os.system(final)
		#os.system('play --no-show-progress -n synth 2 sin 248')
	except:
		print 'Having Some Issues'	
except:
	print 'Having Some Issues'
#print 'done'
#print req
#file = open
#m = k.findAll('div',class_='panel')
#for l in k:
#	print l
