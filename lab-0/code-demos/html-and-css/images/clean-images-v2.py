import glob
import os
list1=glob.glob('*.png')
# print(list1)

# COLLECT FILE LIST
list2=glob.glob('../*.ipynb')
list3=glob.glob('../*.qmd')
list2=list2+list3
# print(list2)

# COLLECT ALL RELEVANT TEXT
text=''
for filename in list2: 
    with open(filename, 'r') as file:
        input_text = file.read()
    text += " "   
    text += input_text

# REMOVE
for filename in list1: 
    if filename not in text:
        print("not found (removing)", filename)
        os. remove(filename)
    # else:
    #     print("found",filename)
