f1 = open('path1','r')  #insert mitra's dictionary here
f2 = open('path2','r')  #insert en-in dictionary here
f3 = open('path3','a')  #insert new blank dictionary here
flag=0

line3 = [line7 for line7 in f2]

f2.close()
f2 = open('path2','r')

wordlist1 = [line1.split(None, 1)[0] for line1 in f2]

wordlist = [line.split(None, 1)[0] for line in f1]

for x in range(0,len(wordlist)-1): 
    for y in range(flag,len(wordlist1)-1):
        if y==len(wordlist1)-1:
            break
        if wordlist[x].lower() == wordlist1[y]:
            f3.write(line3[y])
            break
            flag=y
            
f1.close()
f2.close()
f3.close()
