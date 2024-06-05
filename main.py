from pypdf import PdfReader 
reader = PdfReader(r"C:\Users\ACER PC\Dropbox\My PC (LAPTOP-83BUHU5P)\Downloads\Ayush Sharma - Internship Offer Letter.pdf") 
l = len(reader.pages)
print("length of pdf is :",l)  
page = reader.pages[0] 
s1 = page.extract_text()
print(s1)


print("-----------------------------------------------")
s2 = s1.lower().split(' ')
d = {}
for i in range(len(s2)):
    a = s2[i]
    fw = s2.count(a)
    d[a] = fw
print(d)
len(d)
