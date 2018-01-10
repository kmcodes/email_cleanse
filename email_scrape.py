import re
import pandas as pd
import time
import sys
import os

class getname:
	def breakdown(self):
		if len(sys.argv)>1:
			input_file=sys.argv[-1]
			filename, file_extension = os.path.splitext(input_file)
			return input_file, filename, file_extension
		else:
			return """Please provide the input file name as an argument. For example $
						python email_scrape.py to_clean.csv"""	

def txtfile(input_file, filename):
	with open(input_file,'r') as myfile:
		emails=myfile.read().replace('\n', '')
	r = ur"[\w\.-]+@[\w\.-]+"
	namer = ur"^([^@]+)@[^@]+$"
	match = re.findall(r,emails)
	deduped = list(set(match))

	match_name,domains = [],[]
	for email in deduped:
		domains.append(email.split('@')[1]) 
		match = re.findall(namer,email)
		c=match[0].replace("."," ").replace("_"," ").title()
		match_name.append(c)

	final = pd.DataFrame({'Name': match_name,'Email-ID':deduped,'Domains':domains})
	fname = filename+'_'+str(time.time())[0:10]+'_.csv'
	final.to_csv(fname)

	os.system('clear')
	print " Document has been cleansed and uploaded to: ",
	print fname


#experimental conversion to dataframes driven 
def txt_alt(input_file, filename):
	with open(input_file,'r') as myfile:
		emails=myfile.read().replace('\n', '')
	r = ur"[\w\.-]+@[\w\.-]+"
	namer = ur"^([^@]+)@[^@]+$"
	emails = pd.DataFrame({'Emails':re.findall(r,emails)})
	deduped = emails.drop_duplicates(subset='Emails', keep='first', inplace=False)
	deduped=deduped.reset_index(drop=True)
	match = (deduped['Emails'].str.extractall(namer))
	print type(match)
	# for index, email in deduped.iterrows():
	# 	print email
		# domains.append(str(email).split('@')) 
		# match = re.findall(namer,str(email))
		# #print match
		# c=match[0].replace("."," ").replace("_"," ").title()
		# match_name.append(c)

	final = pd.DataFrame({'Name': match_name,'Email-ID':deduped,'Domains':domains})
	fname = filename+'_'+str(time.time())[0:10]+'_.csv'
	#final.to_csv(fname)
	#print final

	#os.system('clear')
	print " Document has been cleansed and uploaded to: ",
	print fname


def csvfile(input_file, filename):
	emails = pd.read_csv(input_file)
	cleaned = emails.drop_duplicates(subset='Email Address', keep='first', inplace=False)
	fname = filename+'_'+str(time.time())[0:10]+'_cleaned.csv'
	cleaned.to_csv(fname, index=False)
	os.system('clear')
	print " Document has been cleansed and uploaded to: ",
	print fname


alpha = getname()
input_file,filename, file_extension = alpha.breakdown()

if file_extension=='.txt':
	#please use the txtfile() function instead of txt_alt for using.
	txt_alt(input_file,filename)
elif file_extension=='.csv':
	csvfile(input_file, filename)
else:
	print "Wrong input type. Please provide either csv or txt file"	