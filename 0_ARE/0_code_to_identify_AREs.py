import re
import sys

sequence=open(sys.argv[1])
sequences=sequence.readlines()
output_f = open('middle_result','w')
all_set=set("")

strdic={}
class1_set=set("")
class2_set=set("")
class3_set=set("")

###########################storing the final data dictionary########
finaldic=set("")
for ele in range(len(sequences)-1):
	temp=sequences[ele][:-1]
	sequences[ele]=temp

for ele in range(len(sequences)-1):
	
	if sequences[ele][-3:]=='(-)' or sequences[ele][-3:]=='(+)':
		
		tempname=sequences[ele][:-3].replace("-","\t").replace(":","\t")+"\t"+sequences[ele][-2]
		all_set.add(sequences[ele+1].upper()+" "+str(tempname))

		#Example of regular experssion:
		#r'(G{3,}?[ATGC]{1,3}?){3,}?G{3,}?'
		#(G{total more than three}N(1-3 number)){total more than three}G{total more than three}
	
		#Class 3: 
		m = re.findall("T{5,}", sequences[ele+1].upper())
		if m:		#found
			class3_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		
		#class 2: 
		m = re.findall("(ATTTATTTATTTATTTATTTA){s<=1}", sequences[ele+1].upper())
		#zero or one mismatch
                if m:           #found
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		
		m=re.findall("ATTTATTTATTTATTTA", sequences[ele+1].upper())
		if m:
			
			class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		
		m=re.findall("ATTTATTTATTTA", sequences[ele+1].upper())
		if m:
	                class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		
		#class 1:
		m=re.findall("[ATCG][ATCG]ATATTTAAT[AT][AT]", sequences[ele+1].upper())
		#AT-AT, mismatch in the front
		if m and "ATTTATTTA" not in str(m):
			class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))			
		elif m and "ATTTATTTA" in str(m):
			class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		

		m=re.findall("[ATCG][ATCG]ATATTTATA[AT][AT]", sequences[ele+1].upper())
                #AT-TA, mismatch in the front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][ATCG]ATATTTATT[AT][AT]", sequences[ele+1].upper())
                #AT-TT, mismatch in the front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][ATCG]TAATTTAAT[AT][AT]", sequences[ele+1].upper())
                #TA-AT, mismatch in the front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][ATCG]TAATTTATA[AT][AT]", sequences[ele+1].upper())
                #TA-TA, mismatch in the front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][ATCG]TAATTTATT[AT][AT]", sequences[ele+1].upper())
                #TA-TT, mismatch in the front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][ATCG]TTATTTAAT[AT][AT]", sequences[ele+1].upper())
                #TT-AT, mismatch in the front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                


		m=re.findall("[ATCG][ATCG]TTATTTATA[AT][AT]", sequences[ele+1].upper())
                #TT-TA, mismatch in the front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][ATCG]TTATTTAAA[AT][AT]", sequences[ele+1].upper())
                #TT-AA, mismatch in the front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                

		m=re.findall("[ATCG][ATCG]TTATTTATT[AT][AT]", sequences[ele+1].upper())
                #TT-TT, mismatch in the front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][ATCG]AAATTTATT[AT][AT]", sequences[ele+1].upper())
                #AA-TT, mismatch in the front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		m=re.findall("[AT][AT]ATATTTAAT[ATCG][ATCG]", sequences[ele+1].upper())
		#AT-AT, mismatch in the back
		if m and "ATTTATTTA" not in str(m):
			class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))			
		elif m and "ATTTATTTA" in str(m):
			class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		

		m=re.findall("[AT][AT]ATATTTATA[ATCG][ATCG]", sequences[ele+1].upper())
                #AT-TA, mismatch in the back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][AT]ATATTTATT[ATCG][ATCG]", sequences[ele+1].upper())
                #AT-TT, mismatch in the back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][AT]TAATTTAAT[ATCG][ATCG]", sequences[ele+1].upper())
                #TA-AT, mismatch in the back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][AT]TAATTTATA[ATCG][ATCG]", sequences[ele+1].upper())
                #TA-TA, mismatch in the back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][AT]TAATTTATT[ATCG][ATCG]", sequences[ele+1].upper())
                #TA-TT, mismatch in the back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][AT]TTATTTAAT[ATCG][ATCG]", sequences[ele+1].upper())
                #TT-AT, mismatch in the back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                


		m=re.findall("[AT][AT]TTATTTATA[ATCG][ATCG]", sequences[ele+1].upper())
                #TT-TA, mismatch in the back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][AT]TTATTTAAA[ATCG][ATCG]", sequences[ele+1].upper())
                #TT-AA, mismatch in the back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                

		m=re.findall("[AT][AT]TTATTTATT[ATCG][ATCG]", sequences[ele+1].upper())
                #TT-TT, mismatch in the back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][AT]AAATTTATT[ATCG][ATCG]", sequences[ele+1].upper())
                #AA-TT, mismatch in the back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))		
		
	        m=re.findall("[ATCG][AT]ATATTTAAT[ATCG][AT]", sequences[ele+1].upper())
		#AT-AT, mismatch in back and front
		if m and "ATTTATTTA" not in str(m):
			class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))			
		elif m and "ATTTATTTA" in str(m):
			class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		

		m=re.findall("[ATCG][AT]ATATTTATA[ATCG][AT]", sequences[ele+1].upper())
                #AT-TA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]ATATTTATT[ATCG][AT]", sequences[ele+1].upper())
                #AT-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]TAATTTAAT[ATCG][AT]", sequences[ele+1].upper())
                #TA-AT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]TAATTTATA[ATCG][AT]", sequences[ele+1].upper())
                #TA-TA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]TAATTTATT[ATCG][AT]", sequences[ele+1].upper())
                #TA-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]TTATTTAAT[ATCG][AT]", sequences[ele+1].upper())
                #TT-AT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                


		m=re.findall("[ATCG][AT]TTATTTATA[ATCG][AT]", sequences[ele+1].upper())
                #TT-TA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]TTATTTAAA[ATCG][AT]", sequences[ele+1].upper())
                #TT-AA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                

		m=re.findall("[ATCG][AT]TTATTTATT[ATCG][AT]", sequences[ele+1].upper())
                #TT-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]AAATTTATT[ATCG][AT]", sequences[ele+1].upper())
                #AA-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

        	m=re.findall("[ATCG][AT]ATATTTAAT[AT][ATCG]", sequences[ele+1].upper())
		#AT-AT, mismatch in back and front
		if m and "ATTTATTTA" not in str(m):
			class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))			
		elif m and "ATTTATTTA" in str(m):
			class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		

		m=re.findall("[ATCG][AT]ATATTTATA[AT][ATCG]", sequences[ele+1].upper())
                #AT-TA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]ATATTTATT[AT][ATCG]", sequences[ele+1].upper())
                #AT-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]TAATTTAAT[AT][ATCG]", sequences[ele+1].upper())
                #TA-AT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]TAATTTATA[AT][ATCG]", sequences[ele+1].upper())
                #TA-TA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]TAATTTATT[AT][ATCG]", sequences[ele+1].upper())
                #TA-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]TTATTTAAT[AT][ATCG]", sequences[ele+1].upper())
                #TT-AT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                


		m=re.findall("[ATCG][AT]TTATTTATA[AT][ATCG]", sequences[ele+1].upper())
                #TT-TA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]TTATTTAAA[AT][ATCG]", sequences[ele+1].upper())
                #TT-AA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                

		m=re.findall("[ATCG][AT]TTATTTATT[AT][ATCG]", sequences[ele+1].upper())
                #TT-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[ATCG][AT]AAATTTATT[AT][ATCG]", sequences[ele+1].upper())
                #AA-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

        	m=re.findall("[AT][ATCG]ATATTTAAT[ATCG][AT]", sequences[ele+1].upper())
		#AT-AT, mismatch in back and front;
		if m and "ATTTATTTA" not in str(m):
			class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))			
		elif m and "ATTTATTTA" in str(m):
			class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		

		m=re.findall("[AT][ATCG]ATATTTATA[ATCG][AT]", sequences[ele+1].upper())
                #AT-TA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]ATATTTATT[ATCG][AT]", sequences[ele+1].upper())
                #AT-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]TAATTTAAT[ATCG][AT]", sequences[ele+1].upper())
                #TA-AT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]TAATTTATA[ATCG][AT]", sequences[ele+1].upper())
                #TA-TA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]TAATTTATT[ATCG][AT]", sequences[ele+1].upper())
                #TA-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]TTATTTAAT[ATCG][AT]", sequences[ele+1].upper())
                #TT-AT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                


		m=re.findall("[AT][ATCG]TTATTTATA[ATCG][AT]", sequences[ele+1].upper())
                #TT-TA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]TTATTTAAA[ATCG][AT]", sequences[ele+1].upper())
                #TT-AA, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                

		m=re.findall("[AT][ATCG]TTATTTATT[ATCG][AT]", sequences[ele+1].upper())
                #TT-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]AAATTTATT[ATCG][AT]", sequences[ele+1].upper())
                #AA-TT, mismatch in back and front;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

        	m=re.findall("[AT][ATCG]ATATTTAAT[AT][ATCG]", sequences[ele+1].upper())
		#AT-AT, mismatch in back and front;
		if m and "ATTTATTTA" not in str(m):
			class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))			
		elif m and "ATTTATTTA" in str(m):
			class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		

		m=re.findall("[AT][ATCG]ATATTTATA[AT][ATCG]", sequences[ele+1].upper())
                #AT-TA, mismatch in the front and back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]ATATTTATT[AT][ATCG]", sequences[ele+1].upper())
                #AT-TT, mismatch in the front and back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]TAATTTAAT[AT][ATCG]", sequences[ele+1].upper())
                #TA-AT, mismatch in the front and back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]TAATTTATA[AT][ATCG]", sequences[ele+1].upper())
                #TA-TA, mismatch in the front and back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]TAATTTATT[AT][ATCG]", sequences[ele+1].upper())
                #TA-TT, mismatch in the front and back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]TTATTTAAT[AT][ATCG]", sequences[ele+1].upper())
                #TT-AT, mismatch in the front and back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                


		m=re.findall("[AT][ATCG]TTATTTATA[AT][ATCG]", sequences[ele+1].upper())
                #TT-TA, mismatch in the front and back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]TTATTTAAA[AT][ATCG]", sequences[ele+1].upper())
                #TT-AA, mismatch in the front and back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                

		m=re.findall("[AT][ATCG]TTATTTATT[AT][ATCG]", sequences[ele+1].upper())
                #TT-TT, mismatch in the front and back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))


		m=re.findall("[AT][ATCG]AAATTTATT[AT][ATCG]", sequences[ele+1].upper())
                #AA-TT, mismatch in the front and back;
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		#Include definitions from AREsite2:
		#WWTTTWW;WWWTTTWWW;WWWWTTTWWWW: put in class1
		#WWTTTWW
		m=re.findall("[AT][AT]TTT[AT][AT]", sequences[ele+1].upper())
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
		
		#WWWTTTWWW:
		m=re.findall("[AT][AT][AT]TTT[AT][AT][AT]", sequences[ele+1].upper())
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

		#WWWWTTTWWWW
		m=re.findall("[AT][AT][AT][AT]TTT[AT][AT][AT][AT]", sequences[ele+1].upper())
                if m and "ATTTATTTA" not in str(m):
                        class1_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))
                elif m and "ATTTATTTA" in str(m):
                        class2_set.add(sequences[ele+1].upper()+" "+str(tempname)+" "+str(m).replace("'","").replace(", ","and"))

#outputs three types of AREs:

for things in class1_set:
	output_f.write(things.replace('[\'>','\t').replace('\', \'','\t').replace(' ','\t').replace(']','').replace("'","").replace("[","").replace('\t\t','\t').replace(':','\t').replace('>','').replace("(-)","\t-\t").replace("(+)","\t+\t")+'\t'+'Class_one'+'\t'+'\n')

for things in class2_set:
	output_f.write(things.replace('[\'>','\t').replace('\', \'','\t').replace(' ','\t').replace(']','').replace("'","").replace("[","").replace('\t\t','\t').replace(':','\t').replace('>','').replace("(-)","\t-\t").replace("(+)","\t+\t")+'\t'+'Class_two'+'\t'+'\n')

for things in class3_set:
	output_f.write(things.replace('[\'>','\t').replace('\', \'','\t').replace(' ','\t').replace(']','').replace("'","").replace("[","").replace('\t\t','\t').replace(':','\t').replace('>','').replace("(-)","\t-\t").replace("(+)","\t+\t")+'\t'+'Class_three'+'\t'+'\n')

output_f.close()
