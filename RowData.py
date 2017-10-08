
class RowData(object):
    def __init__(self):
        pass

    def isColumn(self,line, column):
        if (len(line) != int(column)+1):
            return False
        return True

    def isNumber(self,line, label_column):  # 判断是否存在非数值数据
        for i in range(len(line)):
            if (i != label_column):
                try:
                    judge=bool(float(line[i]))
                except ValueError:
                    return False
        return True

    def isNone(self,line):
        if not (line):
            return True
        return False

    def column_except(self,list):
        if(bool(list)):
            print('以下数据行列数不等：')
            print(list)
        pass

    def numType_except(self,list):
        if(bool(list)):
            print('以下数据行存在非数值数据：')
            print(list)
        print('\n')

