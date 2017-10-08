from RowData import *
import re
class DataF(object):
    def __init__(self):
        pass

    def getData(self,filename):
        fo = open(filename)
        data = fo.readlines()
        fo.close()
        return data

    def transDataToList(self,data): #分离数据并保存到一个列表
        data_list=[]
        for line in data:
            line_new=re.split('\t|,| ',line.strip('\n'))
            data_list.append(line_new)
        return data_list

    def getColumn(self,data_list): #得到数据维数（列数）
        column_list = []
        for line in data_list:
            column_list.append(len(line))
        return max(column_list, key=column_list.count) - 1

    def getRow(self,data_list): #得到数据行数
        i = 0
        for row in data_list:
            i += 1
        return i


    def creatDictData(self,labels):  # 创建一个以类标签为键的字典
        dict_data = {}
        for key in labels:
            dict_data[key] = [[], 0]
        return dict_data

    def processData(self,data_list, row, dict_data, label_column,column):
        d_column = []
        d_type = []
        row_data=RowData()
        for i in range(row):
            if (row_data.isNone(data_list[i])):
                continue
            if (not (row_data.isColumn(data_list[i], column))):
                d_column.append(i+1)
            if (not (row_data.isNumber(data_list[i], label_column))):
                d_type.append(i+1)
            dict_data[data_list[i][label_column]][0].append(i)
            dict_data[data_list[i][label_column]][1] += 1
        return (d_column,d_type,dict_data)