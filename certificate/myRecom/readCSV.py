import pandas as pd

df = pd.read_csv('datas/jongmok.csv',encoding='utf-8')
# df = pd.read_csv('datas/jickmu.csv',encoding='utf-8')
# li = []
# for idx,d in enumerate(range(len(df))):
#     sample = {}
    # sample.append(df.loc[idx][0])
    # sample.append(df.loc[idx][3])
#     if idx % 2 == 0:
#         sample.setdefault("label", int(idx/2))
#         sample.setdefault("value", df.loc[idx][0])
#         li.append(sample)
#
# print(len(li))
# print(li)




# l1 = pd.read_csv('datas/gisa.csv',encoding='utf-8')
# l1 = pd.read_csv('datas/ginungsa.csv',encoding='utf-8')
# l1 = pd.read_csv('datas/samu.csv',encoding='utf-8')
# l1 = pd.read_csv('datas/sanupgisa.csv',encoding='utf-8')

print(df)