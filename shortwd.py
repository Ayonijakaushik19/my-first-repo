"""Accept a sequence of words as input and print the the shortest word in the sequence. 
The input will have n + 1n+1 lines, where nn denotes the number of terms in the sequence.
The i^{th}line in the input will contain the i^{th}
word in the sequence for 1≤i≤n.

The last line of the input will always be the string abcdefghijklmnopqrstuvwxyz. 
This string is not a part of the sequence.
You can assume that each test case corresponds to a non-empty sequence of words. 
If there are multiple words that have the same minimum length, print the first such occurrence."""


last_line="abcdefghijklmnopqrstuvwxyz"
mini=1000
ans=""
a=""
while(a!=last_line):
    a=input()
    if(len(a)<mini):
        mini=len(a)
        ans=a
   
print(ans)
