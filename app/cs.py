import pandas as pd

data = pd.read_csv('CSV/nama.csv')
print(data)

card_data = pd.read_csv('CSV/card_list.csv', header=None)
nameja = card_data.iloc[:, 1].to_list()
print(nameja)
card_name = card_data.iloc[:, 0].to_list()

for (i, n) in zip(nameja, card_name):
    locals()[i] = data[data["name"] == n]
    if locals()[i].empty:
        locals()[i] = i
    else:
        pass


def card_min(mm):
    y = mm[mm["price"] == mm["price"].min()]
    print(y)


card_min(母)




#熱烈歓迎了法寺
if type(熱烈歓迎了法寺) == str:
    x = f"{熱烈歓迎了法寺}の在庫はありません"
else:
    x = 熱烈歓迎了法寺["price"].min()
    x = f"熱烈歓迎了法寺の最安値は{x}AMTです"




ryo = [金宇賀様, 聖夜祭, 陸弁天, 捌弁天, 母, 天照大神]
ryb = 0
ryc = []
for r in ryo:
    if type(r) == str:
        ryc.append(r)
    else:
        k = r["price"].min()
        ryb = ryb + k
print(f"熱烈歓迎了法寺の素材の価格は{ryb}AMTです。ただし、{ryc}の在庫はありません")
