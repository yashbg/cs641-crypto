file=open('bash_output.txt', mode = 'r', encoding = 'utf-8-sig')
line=file.readlines()
text=[]
for i in line:
    i=i.strip()
    text.append(i)
file.close()
file = open("outputs.txt","w+")
for i in range(1024):
    if i!=0 and i%128==0:
        file.write("\n")
    file.write(text[i])
    file.write(" ")
file.close()