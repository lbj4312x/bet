import random
class Game():
    def __init__(self,print_test,money):
        self.print_test=print_test
        self.money=money
        self.show=""
    def game(self,l,num):
        beilv=[2,2,2,2,4,4,4,6,6,8,10]
        if self.money<num:
            if self.print_test:
                print("你的钱不够!")
            return False
        if l<5 or num<10:
            return False
        self.money=self.money-num
        if num<=25:
            beilv.append(2)
        elif 25<num<=50:
            beilv.append(4)
            beilv.append(6)
        elif 50<num<=100:
            for i in range(5):
                beilv.append(8)
        else:
            for i in range(6):
                beilv.append(10)
        beilv=random.choice(beilv)
        if self.print_test:
            print("倍率:",beilv)
        if beilv==2:
            times=4
        elif beilv==4:
            times=3
        elif beilv==6:
            times=2
        else:
            times=1
        jinru=[]
        for i in range(times):
            a=random.randint(1,l)
            while a in jinru:
                a=random.randint(1,l)
            jinru.append(a)
        if self.print_test:
            print("可以进的情况:")
        for k in jinru:
            if self.print_test:
                print(k)
            b=1
        for j in range(l):
            b=b+random.randint(0,1)
            if self.print_test:
                print("第{0}层,{1}号口".format(j+1,b))
        if b in jinru:
            if self.print_test:
                print("成功")
            self.money=self.money+num*beilv
            return num*beilv
        else:
            if self.print_test:
                print("失败")
            return 0
    def emlpd(self):
        em=0
        you=0
        for i in range(1,4):
            em_xie=5
            you_xie=5
            print("------------第{}局------------".format(i))
            zd=[True,False]*5
            print("有5个实弹，5个空弹，每人有5滴血")
            for j in range(3):
                x=random.choice(zd)
                dj=random.choice(["放大镜","锯子"])
                print("你有道具",dj)
                b=input("是否使用道具")
                if b=="是" or b=="Y" or b=="y" or b=="yes":
                    if dj=="放大镜":
                        print("子弹是",x)
                    else:
                        x=int(x)*2
                a=input("打谁?")
                if a=="自己":
                    you_xie=you_xie-int(x)
                    if int(x)==1 or int(x)==0:
                        zd.remove(x)
                    else:
                        zd.remove(True)
                    if x:
                        print("是实弹,你减了血")
                    else:
                        print("恭喜你，是空弹")
                else:
                    em_xie=em_xie-int(x)
                    if int(x)==1 or int(x)==0:
                        zd.remove(x)
                    else:
                        zd.remove(True)
                    if x:
                        print("是实弹,他减了血")
                    else:
                        print("很可惜，是空弹")
                x=random.choice(zd)
                if random.choice([1,2])==1:
                    print("他选择打你")
                    you_xie=you_xie-int(x)
                    zd.remove(x)
                    if x:
                        print("是实弹,你减了一滴血")
                    else:
                        print("恭喜你，是空弹")
                else:
                    print("他选择打自己")
                    em_xie=em_xie-int(x)
                    zd.remove(x)
                    if x:
                        print("是实弹,他减了一滴血")
                    else:
                        print("很可惜，是空弹")
                if you_xie<=0:
                    em=em+1
                    print("你输了这一局")
                    break
                elif em_xie<=0:
                    print("你赢了这一局")
                    you=you+1
                    break
        if em>you:
            print("你亖了")
        else:
            print("你赢了")
        
    def lhj(self,num):
        if num<10 or self.money<num:
            return False
        self.money=self.money-num
        same=1
        self.show=[]
        shape=["春","夏","秋","冬","金","木","水","火","土"]
        for i in range(5):
            a=random.choice(shape)
            if a in self.show:
                same=same+1
            self.show.append(a)
        self.show=sorted(self.show)
        a=""
        for i in self.show:
            a=a+i+" "
        self.show=a
        if same>1:
            self.money=self.money+num+num*len(shape)*same*0.05
            return num+num*len(shape)*same*0.05
        else:
            return 0

        



