fread = open("output_final.txt", "r")
input=fread.read();
list=input.rstrip('x').split('x');
print len(list)
duplicatedict={}
def countDuplicates():
    for i,item in enumerate(list):
    #     print i,item
        if item in duplicatedict.items():
            duplicatedict[item]=duplicatedict[item]+1
        else:
            duplicatedict[item]=1            
countDuplicates()
unique=0            
for key, count in duplicatedict.items():
    print (key,count)
    if count == 1:
        unique=unique+1
print "unique count: ",unique