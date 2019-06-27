import random

class GuessNum(object):
    def __init__(self):
        print("产生一个1-100的随机数：")
        self.num = random.randint(0,101)
        self.guess()
    def guess(self):
        i = 0
        while True:
            print("猜这个随机数：")
            strNum = input("请输入你猜的数字：")
            i += 1
            try:
                print("****************")
                if int(strNum) < self.num:
                    print("你猜的太小了")
                    continue
                elif int(strNum) > self.num:
                    print("你猜的太大了")
                    continue
                else:
                    print("猜对了")
                    print("你总共猜了%d次" %i)
                    break
            except ValueError:
                print("请输入数字")
                continue

if __name__ == '__main__':
    gn = GuessNum()
