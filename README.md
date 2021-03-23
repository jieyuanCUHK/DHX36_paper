Code for the manuscript "mRNA translation control by Dhx36 binding to 5’UTR G-quadruplex structures is essential for skeletal muscle stem cell regenerative functions"
===
All the code here are tested in Python2.7.15, CentOS7.3.1611 and Matlab R2014b.
## 1. rG4 site identification
Please prepare the fasta file as input (e.g. example_fasta.fa), and run the command_for_rG4.sh:
```Bash
sh command_for_rG4.sh example_fasta.fa #Bash
```
The file final_rG4_sites.bed will be generated, with the following format:

| Chromosome | Begin | End | rG4_sequence | color | strand | rG4_type |
|:----- |:----- |:----- |:----- |:----- |:----- |:----- |
| chr10 | 114752403 | 114752426 | GGGCGGCGGGGTAGCGGCGGCGGG | 0 | - | Bulge |


## 2. AU-rich element (ARE) identification
Please prepare the fasta file as input (e.g. example_fasta.fa), and run the command_for_ARE.sh:
```Bash
sh command_for_ARE.sh example_fasta.fa #Bash
```
The file final_AREs.bed will be generated, with the following format:

| Chromosome | Begin | End | ARE_sequence | color | strand | ARE_class |
|:----- |:----- |:----- |:----- |:----- |:----- |:----- |
| chr15 | 27396407 | 27396420 | GGTTATTTATTTA | 0 | - | Class_two |

## 3. Cell-level G4 intensity quantification
Please first mask individual cells with green mask (example image below), and change the directory in 2_Image_processing/code.m for quantification. 
After running the code in Matlab, cell-level quantifications will be generated (stored in result variable).

![KO-4_b0t0z0c0-2x0-1024y0-1024](https://user-images.githubusercontent.com/40020029/112088866-858a7e00-8bcb-11eb-896c-faafb126cad0.jpg)
