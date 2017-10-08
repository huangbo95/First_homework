import re
class Label(object):
    def __init__(self):
        pass

    def getLabel(self,data_list, label_column): #得到标签数据集
        label_list = []
        for line in data_list:
            label_list.append(line[int(label_column)])
        return list(set(label_list))

    def getlabelColumn(self,filename): #得到标签所在列
        label_column=re.findall('At(\d+)\D',filename)
        if(label_column):
            return int(label_column[0])
        return 0
