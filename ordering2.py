from tkinter import *
import tkinter.messagebox

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        self.label1 = Label(self, text='订单所有单品价格(价格间用逗号分隔)')
        self.label1.pack()
        self.arrInput = Entry(self)
        self.arrInput.pack()

        self.label2 = Label(self, text='优惠金额')
        self.label2.pack()
        self.youhuiInput = Entry(self)
        self.youhuiInput.pack()

        self.label3 = Label(self, text='对方点单单品金额')
        self.label3.pack()
        self.startInput = Entry(self)
        self.startInput.pack()

        self.alertButton = Button(self, text='计算', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        arr = self.arrInput.get() or 'none'
        youhui = self.youhuiInput.get() or 'none'
        start = self.startInput.get() or 'none'

        # 现在价格
        newArr = [float(x) for x in arr.split(',')]
        now = round(sum(newArr), 2)

        # 折扣优惠
        sale = round((now - float(youhui)) / now, 2)

        # 对方点单价格
        other = [float(x) for x in start.split(',')]

        result = round(round(sum(other), 2) * sale, 2)

        print(newArr,now,youhui,sale,other)

        tkinter.messagebox.showinfo('Message', '优惠折扣: %s\n对方点单价格: %s\n需要付款:%s' % (round(sale*10,2), round(sum(other), 2), result))



app = Application()
# 设置窗口标题:
app.master.title('外卖付款计算')
# 主消息循环:
app.mainloop()