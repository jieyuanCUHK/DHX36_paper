#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import re
import sys


sequence=open(sys.argv[1])
sequences=sequence.readlines()
output_f = open('middle_result','w')
all_set=set("")

strdic={}
Two_quar_set=set("")
count_three=0

count_g_abv_40=0
GGATG_2n_3n_4n=set("")
GGATG_1n_3n_4n=set("")
GGATG_1n_2n_3n=set("")
GGATG_1n_2n_4n=set("")
GGATG_3n_4n=set("")
GGATG_2n_4n=set("")
GGATG_2n_3n=set("")
GGATG_1n_4n=set("")
GGATG_1n_3n=set("")
GGATG_1n_2n=set("")
GGATG_4n_4n=set("")
GGATG_3n_3n=set("")
GGATG_2n_2n=set("")
GGATG_1n_1n=set("")
GGATG_2_3_4=set("")
GGATG_1_3_4=set("")
GGATG_1_2_4=set("")
GGATG_1_2_3=set("")
GGATG_3_4=set("")
GGATG_2_4=set("")
GGATG_2_3=set("")
GGATG_1_4=set("")
GGATG_1_3=set("")
GGATG_1_2=set("")
GGATG_4_4=set("")
GGATG_3_3=set("")
GGATG_2_2=set("")
GGATG_1_1=set("")
GGATG_4=set("")
GGATG_3=set("")
GGATG_2=set("")
GGATG_1=set("")

Cano_set=set("")
Cano_setnew=set("")
four_set=set("")
five_set=set("")
six_set=set("")

finaldic=set("")
for ele in range(len(sequences)-1):
	temp=sequences[ele][:-1]
	sequences[ele]=temp


for ele in range(len(sequences)-1):
#there will be postitive strand and negative strand g4 structures;
#	print sequences[ele][-4:] 
	if sequences[ele][-3:]=='(-)' or sequences[ele][-3:]=='(+)':
		
		tempname=sequences[ele][:-3].replace("-","\t").replace(":","\t")+"\t"+sequences[ele][-2]
		#print sequences[ele+1].upper()		
		all_set.add(sequences[ele+1].upper()+" "+str(tempname))

		#Example of regular experssion:
		#r'G{3,}[ATGC]{1,3}){3,}G{3,}'
		#G{total more than three}N(1-3 number)){total more than three}G{total more than three}
	
		#two quartet set: Two_quar_set 
		m = re.findall(r'G{2,}[ATGC]{1,9}G{2,}[ATGC]{1,9}G{2,}[ATGC]{1,9}G{2,}', sequences[ele+1].upper())

		if m:		#found
			Two_quar_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
	
		#canonical set: Cano_set	
		m = re.findall(r'G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:           #found
                        Cano_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		#long loop: four_set, five_set, six_set
		m = re.findall(r'G{3,}[ATGC]{8,12}G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:           #found
                        four_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		m = re.findall(r'G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}[ATGC]{8,12}G{3,}', sequences[ele+1].upper())
                if m:           #found
                        five_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		m = re.findall(r'G{3,}[ATGC]{1,7}G{3,}[ATGC]{13,21}G{3,}[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:           #found
                        six_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		#########################################################
		#for bulges:
		m= re.findall(r"G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
			GGATG_2n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


                #for bulges:
                m= re.findall(r"G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_2n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #for bulges:
                m= re.findall(r"G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_2n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #for bulges:
                m= re.findall(r"G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_2n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #for bulges:
                m= re.findall(r"G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_2n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #for bulges:
                m= re.findall(r"G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_2n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #for bulges:
                m= re.findall(r"G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_2n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #for bulges:
                m= re.findall(r"G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_2n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		
		m= re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		#GGATG_1n_2n_3n
                m = re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                
                m = re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m = re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		
		#GGATG_3n_4n
                m = re.findall(r"G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m = re.findall(r"G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_3n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		#GGATG_2n_4n
                m= re.findall(r"G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		m= re.findall(r"G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_2n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_2n_3n
                m= re.findall(r"G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}", sequences[ele+1].upper())
                if m:
                        GGATG_2n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1n_4n
                m= re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_1n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_1n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G", sequences[ele+1].upper())
                if m:
                        GGATG_1n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r"G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG", sequences[ele+1].upper())
                if m:
                        GGATG_1n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1n_3n
                m= re.findall(r'GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		
                m= re.findall(r'GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r'G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m= re.findall(r'G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		#GGATG_1n_2n
                m =re.findall(r'GG[AT]{2,5}G[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m =re.findall(r'GG[AT]{2,5}G[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m =re.findall(r'G[AT]{2,5}GG[ATGC]{1,7}GG[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m =re.findall(r'G[AT]{2,5}GG[ATGC]{1,7}G[AT]{2,5}GG[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1n_2n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_4n_4n
                m=re.findall(r'G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}G[AT]{2,5}G', sequences[ele+1].upper())
                if m:
                        GGATG_4n_4n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_3n_3n
                m=re.findall(r'G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G[AT]{2,5}G[AT]{2,5}G[ATGC]{1,7}G{3,}',sequences[ele+1].upper())
                if m:
                        GGATG_3n_3n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_2n_2n
                m=re.findall(r'G{3,}[ATGC]{1,7}G[AT]{2,5}G[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_2n_2n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1n_1n
                m=re.findall(r'G[AT]{2,5}G[AT]{2,5}G[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}[ATGC]{1,7}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1n_1n.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		#GGATG_2_3_4
                m=re.findall(r'G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}GG[AT]G[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_2_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_2_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G[AT]GG[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_2_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_2_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}GG[AT]G[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_2_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_2_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G[AT]GG[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_2_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_2_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1_3_4
                m=re.findall(r'GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_1_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_1_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_1_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_1_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_1_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_1_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_1_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_1_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1_2_4
                m=re.findall(r'GG[AT]G[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'GG[AT]G[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'GG[AT]G[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'GG[AT]G[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1_2_3
                m=re.findall(r'GG[AT]G[ATGC]{1,9}GG[AT]G[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'GG[AT]G[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'GG[AT]G[ATGC]{1,9}G[AT]GG[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'GG[AT]G[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}GG[AT]G[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G[AT]GG[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_3_4
                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_3_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_2_4
                m=re.findall(r'G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_2_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		#GGATG_2_3
                m=re.findall(r'G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_2_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1_4
                m=re.findall(r'GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_1_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_1_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G', sequences[ele+1].upper())
                if m:
                        GGATG_1_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG', sequences[ele+1].upper())
                if m:
                        GGATG_1_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1_3
                m=re.findall(r'GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1_2
                m=re.findall(r'GG[AT]G[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1_2
                m=re.findall(r'GG[AT]G[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


                #GGATG_1_2
                m=re.findall(r'G[AT]GG[ATGC]{1,9}GG[AT]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1_2
                m=re.findall(r'G[AT]GG[ATGC]{1,9}G[AT]GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_2.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


                #GGATG_4_4
                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G[ATC]G[ATC]G', sequences[ele+1].upper())
                if m:
                        GGATG_4_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		#GGATG_3_3
                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G[ATC]G[ATC]G[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_3_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_2_2
                m=re.findall(r'G{3,}[ATGC]{1,9}G[ATC]G[ATC]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_2_2.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_1_1
                m=re.findall(r'G[ATC]G[ATC]G[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_1_1.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_4
                m=re.findall(r'GG[C]{1,1}G[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[C]{1,1}GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


                m=re.findall(r'GG[AT]{1,9}G[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G[AT]{1,9}GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_4.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		
		#GGATG_3
                m=re.findall(r'G{3,}[ATGC]{1,9}GG[C]{1,1}G[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G[C]{1,1}GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}GG[AT]{1,9}G[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G[AT]{1,9}GG[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_3.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                #GGATG_2
                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[C]{1,1}G[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_2.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G[C]{1,1}GG[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_2.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]{1,9}G[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_2.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]{1,9}GG[ATGC]{1,9}G{3,}', sequences[ele+1].upper())
                if m:
                        GGATG_2.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))



                #GGATG_1
                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[C]{1,1}G', sequences[ele+1].upper())
                if m:
                        GGATG_1.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G[C]{1,1}GG', sequences[ele+1].upper())
                if m:
                        GGATG_1.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}GG[AT]{1,9}G', sequences[ele+1].upper())
                if m:
                        GGATG_1.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

                m=re.findall(r'G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G{3,}[ATGC]{1,9}G[AT]{1,9}GG', sequences[ele+1].upper())
                if m:
                        GGATG_1.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

#generate output sets
long_set=set("")
long_set=four_set | five_set | six_set -Cano_set

#Two_quar_set2=Two_quar_set-(long_set | Cano_set)

bulge_temp=set("")
bulge_temp=GGATG_1 | GGATG_2 | GGATG_3 | GGATG_4 | GGATG_1_1 | GGATG_2_2 | GGATG_3_3 | GGATG_4_4 | GGATG_1_2 | GGATG_1_3 | GGATG_1_4 | GGATG_2_3 | GGATG_2_4 | GGATG_3_4 | GGATG_1_2_3| GGATG_1_2_4 | GGATG_1_3_4 | GGATG_2_3_4 | GGATG_1n_1n | GGATG_2n_2n | GGATG_3n_3n | GGATG_4n_4n | GGATG_1n_2n | GGATG_1n_3n | GGATG_1n_4n | GGATG_2n_3n | GGATG_2n_4n | GGATG_3n_4n | GGATG_1n_2n_4n | GGATG_1n_2n_3n | GGATG_1n_3n_4n | GGATG_2n_3n_4n

bulge_set=bulge_temp

Two_quar_set2=Two_quar_set-long_set-Cano_set-bulge_temp

for things in bulge_set:
        output_f.write(things.replace('[\'>','\t').replace('\', \'','\t').replace(' ','\t').replace(']','').replace("'","").replace("[","").replace('\t\t','\t').replace(':','\t').replace('>','').replace("(-)","\t-\t").replace("(+)","\t+\t")+'\t'+'Bulge'+'\t'+'\n')

for things in long_set:
        output_f.write(things.replace('[\'>','\t').replace('\', \'','\t').replace(' ','\t').replace(']','').replace("'","").replace("[","").replace('\t\t','\t').replace(':','\t').replace('>','').replace("(-)","\t-\t").replace("(+)","\t+\t")+'\t'+'Long'+'\t'+'\n')


for things in Two_quar_set2:
	output_f.write(things.replace('[\'>','\t').replace('\', \'','\t').replace(' ','\t').replace(']','').replace("'","").replace("[","").replace('\t\t','\t').replace(':','\t').replace('>','').replace("(-)","\t-\t").replace("(+)","\t+\t")+'\t'+'Two_qu'+'\t'+'\n')

for things in Cano_set:
	output_f.write(things.replace('[\'>','\t').replace('\', \'','\t').replace(' ','\t').replace(']','').replace("'","").replace("[","").replace('\t\t','\t').replace(':','\t').replace('>','').replace("(-)","\t-\t").replace("(+)","\t+\t")+'\t'+'Canonical'+'\t'+'\n')

output_f.close()
