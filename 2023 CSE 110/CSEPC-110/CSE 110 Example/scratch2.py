# with open("books.txt") as books_file:
#     for line in books_file:
#         clean_line = line.split(",")
#         print(clean_line[0])
#         # print(line)

def fullname(w1,w2):
  return w1 + ' ' + w2

f=fullname(w2='faith',w1='charity')
print(f)