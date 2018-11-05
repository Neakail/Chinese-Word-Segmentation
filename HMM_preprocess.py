import codecs
import re


fin=codecs.open("199801.txt","r","utf-8")
strl=fin.read()
strl = re.sub("\[","",strl)
strl = re.sub("]nt","",strl)
strl = re.sub("]ns","",strl)
strl = re.sub("]nz","",strl)
strl = re.sub("]l","",strl)
strl = re.sub("]i","",strl)
strl = re.sub("\n", "@", strl)
strl = re.sub("\s+"," ", strl)
strl = re.sub("@","\n",strl)
strl = re.sub(" \n","\n",strl)
strl = re.sub(" ","@",strl)
strl = re.sub("\s+","\n",strl)
strl = re.sub("@"," ",strl)
s=strl.encode("utf-8")
fout=open("199801_1.txt","w")
fout.write(s)
fout.close()
fin.close()