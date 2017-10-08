from FileC import *
from Label import *
from DataF import *

if __name__=='__main__':
    file = FileC()
    dataf = DataF()
    lbl = Label()
    row_data = RowData()

    dirpath = input('please input dirpath:\n')   #获取数据文件所在的目录
    file_list = file.getAllfile(dirpath)    #得到该目录下的所有文件名

    for fn in file_list:
        print('文件:' + str(fn))
        label_column=lbl.getlabelColumn(fn)  #获取类标签所在的列

        data = dataf.getData(dirpath+'/'+fn)  # 获取文件数据
        data_list=dataf.transDataToList(data) # 分离文件数据并保存于一个列表

        column = dataf.getColumn(data_list)  # 获取文件数据的维度(列数)
        row = dataf.getRow(data_list)  # 获取文件数据的行数
        print('文件' + str(fn) + ' 的维度是:' + str(column))

        labels = lbl.getLabel(data_list,label_column) # 数据的类标签集

        Dcolumn_error=Dtype_error = []  # 存放列数不等的数据行和数值类型异常的行
        dict_data = dataf.creatDictData(labels) #按照类标签对文件数据进行分类，以字典的方式存放

        (Dcolumn_error,Dtype_error,dict_data)=dataf.processData(data_list,row,dict_data,label_column,column)
        file.processSon_file(fn,labels,data,dict_data)

        row_data.column_except(Dcolumn_error) #输出列数不等的数据行
        row_data.numType_except(Dtype_error)  #输出存在非数值类型的数据行


