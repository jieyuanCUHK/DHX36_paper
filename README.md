Code for the manuscript "mRNA translation control by Dhx36 binding to 5'UTR G4 structures is essential for skeletal muscle stem cell regenerative functions"
===
All the code here are tested in Python2.7.15 and CentOS7.3.1611.
## 1. rG4 site identification
Please prepare the fasta file as input (e.g. example_fasta.fa), and run the commmand_for_rG4.sh:
```Bash
sh command_for_rG4.sh example_fasta.fa #Bash
```
The file final_rG4_sites.bed will be generated, with the following format:

| 栏目1 | 栏目2 |
| ----- | ----- |
| 内容1 | 内容2 |

| Chromosome | Begin | End | rG4_sequence | color | strand | rG4_type |
| ---------- | ----------- | ---------- | ----------- | ---------- | ----------- |
| chr10 | 114752403 | 114752426 | GGGCGGCGGGGTAGCGGCGGCGGG | 0 | - | Bulge |


## 2. AU-rich element (ARE) identification
Please prepare the fasta file as input (e.g. example_fasta.fa), and run the commmand_for_ARE.sh:
```Bash
sh command_for_ARE.sh example_fasta.fa #Bash
```
A bed-format file final_AREs.bed will be generated.
