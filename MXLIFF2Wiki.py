from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from lxml import etree
import sys
import codecs

def open_mxliff():
    source_file = askopenfilename(initialdir = ".", filetypes = (("All files", "*"),("xliff files","*.xlf")))
    entry.delete(0,END)
    entry.insert(0,source_file)
    return
	
def export():
    nentrada=entry.get()
    nsortida=nentrada+".out.txt"
    root = etree.parse(nentrada)
    sortida=codecs.open(nsortida,"w",encoding="utf-8")

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

main_window = Tk()
main_window.title("MXLIFF2Wiki")
s = ttk.Style()
themes=s.theme_names()
if "winnative" in themes:
    s.theme_use("winnative")
else:
    s.theme_use("default")
main_window.clipboard_clear()

#FILES
selectButton=Button(main_window, text = str("Select MXLIFF"), command=open_mxliff,width=15)
selectButton.grid(row=0,column=0)
entry = Entry(main_window,  width=50)
entry.grid(row=0,column=1)

goButton=Button(main_window, text = str("Export"), command=export,width=15)
goButton.grid(sticky="E",row=1,column=1)



main_window.mainloop()