#first: find the several types of rG4 sites:
python 0_ARE/0_code_to_identify_AREs.py $1
sh 0_ARE/further_process.sh middle_result > middle_result2
rm middle_result

#then process to get the middle file 3:
python 0_ARE/1_code_to_process_output.py middle_result2 | sort | uniq | sed 's/ /\t/g' > middle_result3
rm middle_result2

#check whether the AREs in middle_result3 is overlapping:
bedtools intersect -a middle_result3 -b middle_result3 -wao | perl -lane 'print if $F[-1] != 0' | sort | uniq > first_part

#select the longer one in the overlapped sites:
python 0_ARE/2_further_process_AREs.py first_part | sort | uniq >selected_1
rm first_part

#then the non overlapping ones were merged together with selected_1:
grep -F -v -f region_overlapping middle_result3 | sort | uniq | cat  - selected_1 > selected_2
rm selected_1
rm region_overlapping
rm middle_result3

#finally for selected_2, the near AREs in class3 and class1 are merged together:
grep three selected_2 | bedtools sort -i - | bedtools merge -i - -s -d 5 -c 4,6 -o distinct,distinct | awk '{print $0,"Class_three"}' | sed 's/ /\t/g' | cut -f1-3,5,6,7 > fin_3
grep one selected_2 | bedtools sort -i - | bedtools merge -i - -s -d 5 -c 4,6 -o distinct,distinct | awk '{print $0,"Class_one"}' | sed 's/ /\t/g' |cut -f1-3,5,6,7 > fin_1

#finally merge fin_3, fin_1 and selected_2 results:
less selected_2 | grep two |cut -f1-4,6,7 | cat - fin_1 fin_3  |awk '{print $1,$2,$3,$4,0,$5,$6}' |sed 's/ /\t/g' > final_AREs.bed
rm selected_2
rm fin_3
rm fin_1


