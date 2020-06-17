#this is the program used to process the overlaped AU-element results:
import re
import sys

data=open(sys.argv[1])

#format:
#chrM	2910	2923	AATTATTTATAAA	0	+	Class_one	chrM	2910	2923	AATTATTTATAAA Class_one	13

data1=data.readlines()
id_set=set()


for items in data1:
	temp=re.split('[\t]',items.strip())

	if str(temp[0:7])==str(temp[7:14]):
		continue
		#print temp[0:7]
		#id_set.add(str(temp[0:7]))

	else:
		if 'A' not in temp[3] and 'A' not in temp[10]:
			if str(temp[0:7]) not in id_set and str(temp[7:14]) not in id_set:
				if (float(temp[2])-float(temp[1]))>(float(temp[9])-float(temp[8])):
					print str(temp[0:7]).replace("', '","\t").replace("['","").replace("']","")
					id_set.add(str(temp[0:7]))
					id_set.add(str(temp[7:14]))

				else:
					print str(temp[7:14]).replace("', '","\t").replace("['","").replace("']","")
					id_set.add(str(temp[0:7]))
					id_set.add(str(temp[7:14]))

		elif 'A' in temp[3] or 'A' in temp[10]:
			if str(temp[0:7]) not in id_set and str(temp[7:14]) not in id_set:

				if (float(temp[2])-float(temp[1]))>(float(temp[9])-float(temp[8])):
                                	print str(temp[0:7]).replace("', '","\t").replace("['","").replace("']","")
					id_set.add(str(temp[0:7]))
					id_set.add(str(temp[7:14]))

	                        else:
        	                        print str(temp[7:14]).replace("', '","\t").replace("['","").replace("']","")
					id_set.add(str(temp[0:7]))
					id_set.add(str(temp[7:14]))

file=open('region_overlapping','w')
for things in id_set:
	file.write(things.replace("', '","\t").replace("['","").replace("']","")+'\n')

file.close()
