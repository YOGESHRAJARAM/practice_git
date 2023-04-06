para=[]
print("Enter a para : ")

while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
print(para)
    
outin="\n".join(para)
print(outin)
