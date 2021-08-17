#! /usr/bin/python

import os, datetime, time, fnmatch, shutil, platform
from datetime import datetime as dt
from datetime import date

YEARS=['2017','2018','2019']
MarsY=['2013-2014','2018']
Months=[]

SS=['/Personal/C-Archives/Astronomy/10-Raws', '/Personal/C-Archives/Astronomy/20-SavedStacks', '/Personal/C-Archives/Astronomy/30-FinalAssembly', '/Personal/C-Archives/Astronomy/90-UnfinishedStacks', '/Personal/C-Archives/Astronomy/40-FinalWeb']

DirsAndYears=['/Personal/B-Sorted/Photos', '/Personal/B-Sorted/Videos', '/Personal/C-Archives/Photos', '/Personal/C-Archives/Videos']
DirsAndYearsAndMonths=['/Personal/B-Sorted/Photos', '/Personal/C-Archives/Photos']

if platform.system() == 'Linux':
	with open('/home/miphilli/Dropbox/5-Permanent/Notes/2ndGenerationDataWorkflow.txt') as F1:
		F = F1.read().split()
	with open('/home/miphilli/Dropbox/5-Permanent/Notes/2ndGenerationDataWorkflowcommon.txt') as Fc1:
		Fc = Fc1.read().split()
	with open('/home/miphilli/Dropbox/5-Permanent/Notes/months.txt') as Months1:
		Months = Months1.read().split()
else:
	pass

if platform.system() == 'Windows':
        DropboxBase='D:\\Dropbox\\5-Permanent\\Notes\\'
        with open(os.path.join(DropboxBase,'2ndGenerationDataWorkflow.txt')) as F1:
                F = F1.read().split()
        with open(os.path.join(DropboxBase,'2ndGenerationDataWorkflowcommon.txt')) as Fc1:
                Fc = Fc1.read().split()
        with open(os.path.join(DropboxBase,'months.txt')) as Months1:
                Months = Months1.read().split()
else:
	pass




for d1 in F:
	try:
		os.makedirs(os.path.normpath(d1))
	except:
		pass

for S in SS:
	for d2 in Fc:
		if 'Mars' in d2:
			for Y in MarsY:
				try:
					print S+os.path.normpath(d2)+Y
					os.makedirs(os.path.join(os.path.normpath(S),os.path.normpath(d2),Y))
				except:
					pass
		elif 'Jupiter' in d2:
			for Y in YEARS:
				try:
					print S+os.path.normpath(d2)+Y
					os.makedirs(os.path.join(os.path.normpath(S),os.path.normpath(d2),Y))
				except:
					pass
		elif 'Saturn' in d2:
			for Y in YEARS:
				try:
					print S+os.path.normpath(d2)+Y
					os.makedirs(os.path.join(os.path.normpath(S),os.path.normpath(d2),Y))
				except:
					pass
		else:
			try:
				print S+os.path.normpath(d2)
				os.makedirs(os.path.join(os.path.normpath(S),os.path.normpath(d2)))
			except:
				pass


for i in DirsAndYearsAndMonths:
	for Y in YEARS:
		for M in Months:
			try:
				os.makedirs(os.path.join(os.path.normpath(i),Y,M))
			except:
				pass

for i in DirsAndYears:
	for Y in YEARS:
		try:
			os.makedirs(os.path.join(os.path.normpath(i),Y))
		except:
			pass

for i in DirsAndYearsAndMonths:
	for Y in YEARS:
		for M in Months:
			try:
				shutil.copy2('/home/miphilli/Documents/Dropbox/5-Permanent/Webs/dot.gif',os.path.join(os.path.normpath(i),Y,M))
			except:
				pass
