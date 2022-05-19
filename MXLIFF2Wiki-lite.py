from lxml import etree
import sys
import codecs 

nentrada=sys.argv[1]
nsortida=sys.argv[2]

root = etree.parse(nentrada)
sortida=codecs.open(nsortida,"w",encoding="utf-8")

#for element in root.iter():
#    print(element.tag)

tus=root.findall('.//{urn:oasis:names:tc:xliff:document:1.2}trans-unit')

for tu in tus:
    paras=[]
    targets=tu.findall('{urn:oasis:names:tc:xliff:document:1.2}target')
    for target in targets:
        mks=target.findall('{urn:oasis:names:tc:xliff:document:1.2}mrk')
        if len(mks)>0:
            for mk in mks:
                paras.append(mk.text)
        else:
            paras.append(target.text)
    para="".join(paras)
    sortida.write(para+"\n\n")
