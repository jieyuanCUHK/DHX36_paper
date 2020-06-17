#first: find the several types of rG4 sites:
python 1_rG4/0_code_to_identify.py $1 
sh 1_rG4/further_process.sh middle_result > middle_result2
rm middle_result

#then process to get the final file
python 1_rG4/1_code_to_process_output.py middle_result2 | sort | uniq |grep -v "\[" | sed 's/ /\t/g' > final_rG4_sites.bed
rm middle_result2

