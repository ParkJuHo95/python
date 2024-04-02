from day06_graph.daoStock_my import DaoStock

class Datas():

    def __init__(self):
        self.ds = DaoStock();
        
    def selectDatas(self,s_name):
        s_list = self.ds.selectList(s_name)
        result = []
        for i in s_list:
            start = s_list[0]['price']
            dif = start - i['price']
            percent = dif/start * 100
            result.append(percent)
            result.append(i['ymd'])
        return result
    
    def points(self,k,s_name):
        name_list = self.selectDatas(s_name)
        x = []
        y = []
        z = []
        for idx, i in enumerate(name_list):
            if idx%2 == 0:
                z.append(i)
                x.append(k)
            if idx%2 == 1:
                date = i.replace("_","")
                num = int(date[8:])
                y.append(num)
        return x,y,z    
        
        
if __name__ == '__main__':
    Datas().selectDatas("삼성전자")