import os
import xlwings as xw
file_path=r'C:\Users\m4800\Desktop\excel' #给出文件所在的路径文件夹名称
file_list=os.listdir(file_path)  #列出路径下所有文件和文件夹的名称
app=xw.App(visible=False)
sheet_name='Invoice'
for i in file_list:
    if i.startswith('~$'):
        continue
    file_paths=os.path.join(file_path,i)
    workbook=app.books.open(file_paths)
    for term in workbook.sheets:
        if term.name==sheet_name:
            term.api.PrintOut()
            break        
app.quit()