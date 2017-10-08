class FileC(object):
    def __init__(self):
        pass

    def getAllfile(self, path):
        import os
        fo = os.listdir(path)
        file_list = []
        for f in fo:
            if not os.path.isdir(f):
                file_list.append(f)
        return file_list

    def processSon_file(self,fn,labels,data,dict_data):
        for la in labels:
            file_name = fn.split('.')[0] + '_c' + str(la) + '_' + str(dict_data[la][1])+'.'+fn.split('.')[1]
            son_file = open(file_name, 'a+')
            for son_num in dict_data[la][0]:
                son_file.write(data[son_num])
            son_file.close()