sed '{
N
s/\(.*\)\n\(\t.*\)/\1\2/
t merge
P
D}
:merge 
p
d' $1
