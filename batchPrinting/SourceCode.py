import os
import xlwings as xw
file_path=r'./WaitingForPrint' #给出文件所在的路径文件夹名称
file_list=os.listdir(file_path)  #列出路径下所有文件和文件夹的名称
app=xw.App(visible=False)
#sheet_name='Invoice'
for i in file_list:
    if i.startswith('~$'):
        continue
    file_paths=os.path.join(file_path,i)
    workbook=app.books.open(file_paths)
    worksheet=workbook.sheets[1]
    #worksheet.api.PageSetup.Orientation = xlLandscape # 横向模式
    worksheet.api.PageSetup.Zoom = False
    worksheet.api.PageSetup.FitToPagesTall = 1 #对页高进行缩放
    worksheet.api.PageSetup.FitToPagesWide = 1 #对页宽进行缩放
    worksheet.api.PrintOut()
app.quit()

