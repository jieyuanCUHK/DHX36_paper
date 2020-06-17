import re
import sys

data=open(sys.argv[1])

data1=data.readlines()

for items in data1:
	temp=re.split('[\t]',items.strip())
	if str(temp[5]).find("and") != -1:
		s_temp=re.split("[and]",temp[5])	

	else:
		s_temp=temp[5]
	
	s_temp=filter(None, s_temp)
	if isinstance(s_temp,list):
		print s_temp
		for matches in s_temp:
			process=[i.start() for i in re.finditer(matches, temp[0])]
			

			for things in process:
				#then check for the strandness:
				if temp[4]=='+':
				#	print things
					print temp[1],int(temp[2])+things,int(temp[2])+len(matches)+things,matches,0,temp[4],temp[6]	

				if temp[4]=='-':
				#	print things
				#if negative strand, then the sequences were from right to left;
					print temp[1],int(temp[3])+1-len(matches)-things,int(temp[3])-things,matches,0,temp[4],temp[6] 

	else:
		process=[i.start() for i in re.finditer(s_temp, temp[0])]
		for things in process:
			if temp[4]=='+':
                        	#print things
                                print temp[1],int(temp[2])+things,int(temp[2])+len(s_temp)+things,s_temp,0,temp[4],temp[6]
			if temp[4]=='-':
				#print things
				print temp[1],int(temp[3])+1-len(s_temp)-things,int(temp[3])-things,s_temp,0,temp[4],temp[6]    
				

