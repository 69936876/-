print("1、计算利息")
print("2、程序版本")
print("3、关于本程序")
choice = input("输入你的选择(1/4):")

if choice =="1":
    x=int(input("请输入金额："))
    y = x * 2.5 / 200
    print("利息是：", y)
    print("（程序已结束运行）")

elif choice == "2":
     print("版本：2.0")
     print("（程序已结束运行）")

elif choice == "3":
     print("使用本程序可以计算1年的利息，数值来源于互联网")
     print("(本程序仅供参考，请以各大银行官网和柜台公布的利息为准)如有问题，请咨询银行客服")
     import time
     localtime = time.asctime(time.localtime(time.time()))
     print("截止到本地时间为 :", localtime)
     print("（程序已结束运行）")

            
