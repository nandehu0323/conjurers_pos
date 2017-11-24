import time
import pickle
from datetime import datetime

sell_data = []
base_price = int(input("価格を設定してください:"))

with open('data.dump', 'rb') as f:
    sell_data = pickle.load(f)

while True:
    total_amount = 0
    total_price = 0
    data_dict = {
        "amount": 0,
        "date": None,
        "price": base_price
        }
    amount = input("個数:")
    if amount == "change":
        base_price = int(input("価格を設定してください:"))
        continue
    elif amount == "history":
        for i in sell_data:
            print("日時:" + str(i["date"]) + "  売上価格:" + str(i["price"]) + "  個数:" + str(i["amount"]) + )
        continue
    data_dict = {
        "amount": int(amount),
        "date": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        "price": base_price
        }
    sell_data.append(data_dict)

    for i in sell_data:
        total_amount += i["amount"]
        total_price += i["amount"] * i["price"]

    print("合計売上:" + str(total_price) + "  合計売上個数:" + str(total_amount) + "  個数:" + str(data_dict["amount"]) + "  日時:" + str(data_dict["date"]))

    with open('data.dump', 'wb') as f:
        pickle.dump(sell_data, f)
