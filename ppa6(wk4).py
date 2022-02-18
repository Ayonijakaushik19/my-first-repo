temp_words=list(map(str,input().split(",")))
temp_words.reverse()
for word in temp_words:
    if word!=temp_words[-1]:
        print(word,end=",")
    else:
        print(word)
