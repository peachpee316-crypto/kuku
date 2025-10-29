"""
〇九九アプリ
1×1から9×9までランダムに出題してユーザーに答えを入力してもらう。try except
10問制、20問制、間違えるまで……などルールを自分で考えてみよう。
-------------------kuku.csv作成-------------------------------
import csv

with open('kuku.csv', 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(1, 10):
        for j in range(1, 10):
            expression = f"{i}×{j}"
            answer = i * j
            writer.writerow([expression, answer])
---------------------------------------------------------------
"""
import random as r
kuku_dic={}
with open("kuku.csv","r",encoding="UTF-8")as fp:
    for val in fp:
        temp=val.strip().split(",")
        kuku_dic[temp[0]]=temp[1]
        # print(kuku_dic) #出力OK


max_q=input("何回チャレンジしますか？(数字を入力)：")

q_count=0 #問題回数
c_count=0 #正解数
try:      #チャレンジ回数max_qのValueError
    while q_count<int(max_q):
        q_count += 1
        print(f"★★---question {q_count}/{max_q}---★★")

        q=r.choice(list(kuku_dic.keys())) #九九問題
        ans=input(f"{q}=？:  (終了はeを入力)")
        if ans == "e":
            print("終了します。")
            break
        try:    #九九回答ansのValueError
            if int(ans) == int(kuku_dic[q]):
                print("正解！")
                c_count += 1
            else:
                print(f"不正解。答えは【{int(kuku_dic[q])}】")
        except ValueError:
            print("無効な入力です。数字を入力してください。")
            q_count -= 1
except ValueError:
    print("無効な入力です。数字を入力してください。")


if q_count >0:  #1問でも有効な回答があった場合正解率を計算
    # print(f"★★★---{c_count}/{q_count}Correct!---★★★")
    print(f"★★★---{round(c_count/q_count*100,1)}%Correct!---★★★")
else:
    print("有効な質問は回答されませんでした。")