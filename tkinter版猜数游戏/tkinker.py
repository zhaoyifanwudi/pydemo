import random
import tkinter
from tkinter.messagebox import showerror, showinfo  # 消息框
from tkinter.simpledialog import askinteger  # 对话框

root = tkinter.Tk()
# 标题
root.title('猜数游戏')
# 窗口初始大小和位置
# 横*纵+离左屏幕边距距离+离上屏幕边距距离
root.geometry('280x80+400+300')
# 不许改表窗口大小
# width height
root.resizable(False, False)
# 用户猜的数
varNumber = tkinter.StringVar(root, value='0')
# 允许猜的总次数
totalTimes = tkinter.IntVar(root, value=0)
# 已猜次数
already = tkinter.IntVar(root, value=0)
# 当前生成的随机数
currentNumber = tkinter.IntVar(root, value=0)
# 玩家玩游戏的总次数
times = tkinter.IntVar(root, value=0)
# 玩家猜对的总次数
right = tkinter.IntVar(root, value=0)

lb = tkinter.Label(root, text='请输入一个整数: ')
# 将label放在（10,10）上
lb.place(x=10, y=10, width=100, height=20)

# 用户猜数并输入的文本框
entryNumber = tkinter.Entry(root, width=140, textvariable=varNumber)
entryNumber.place(x=110, y=10, width=140, height=20)
# 默认禁用，只有开始游戏以后才允许输入
entryNumber['state'] = 'disabled'

# 按钮单机处理函数


def buttonClick():
    if button['text'] == 'Start Game':
        # 每次游戏室允许用户自定义的数值范围
        # 玩家必须输入正确的数
        # 最小数值
        while True:
            try:
                # 输入一个数 initialvalue为默认值 第一个参数为标题 第二个参数是提示
                start = askinteger('允许最小的整数', '最小数（必须大于0）', initialvalue=1)
                if start != None:
                    assert start > 0
                    break
            except:
                pass
        while True:
            try:
                end = askinteger('允许的最大整数', '最大数（必须大于10）', initialvalue=11)
                if end != None:
                    assert end > 10 and end > start
                    break
            except:
                pass
        # 在用户自定义范围内生成要猜的随机数
        currentNumber.set(random.randint(start, end))
        # 用户自定义一共允许猜几次
        # 玩家必须输入正确的整数
        while True:
            try:
                t = askinteger('最多允许猜几次？', '总次数（必须大于0）', initialvalue=3)
                if t != None:
                    assert t > 0
                    totalTimes.set(t)
                    break
            except:
                pass
        # 已猜次数初始化为0
        already.set(0)
        button['text'] = '剩余次数：'+str(t)
        # 把文本框初始化为0
        varNumber.set('0')
        # 启动文本框，允许用户开始输入整数
        entryNumber['state'] = 'normal'
        # 玩游戏的次数加1
        times.set(times.get() + 1)
    else:
        # 以供允许猜几次
        total = totalTimes.get()
        # 本次游戏的正确答案
        current = currentNumber.get()
        # 玩家本次猜的数
        try:
            x = int(varNumber.get())
        except:
            showerror('抱歉', '必须输入整数')
            return
        # 猜对了
        if x == current:
            showinfo('恭喜', '猜对了')
            button['text'] = 'Start Game'
            # 禁用文本框
            entryNumber['state'] = 'disabled'
            # 猜对的次数加1
            right.set(right.get() + 1)
        else:
            # 本次游戏已猜次数加1
            already.set(already.get() + 1)
            if x > current:
                showerror('抱歉', '猜的数太大了')
            else:
                showerror('抱歉', '猜的数太小了')
            # 可猜次数用完了
            if already.get() == total:
                showerror('抱歉', '游戏结束了，正确的数是：' + str(currentNumber.get()))
                button['text'] = 'Start Game'
                # 禁用文本框
                entryNumber['state'] = 'disabled'
            else:
                button['text'] = '剩余次数：' + str(total-already.get())
    # 在窗口上创建按钮，并设置事件处理函数
    button = tkinter.Button(root, text='Start Game', command=buttonClick)
    button.place(x=10, y=40, width=250, height=20)
    # 关闭程序时提示消息

    def closeWindow():
        message = '共玩游戏{0}次，猜对{1}次！\n欢迎下次再玩！'
        message = message.format(times.get(), right.get())
        showinfo('战绩', message)
        root.destroy()
    # WM_DELETE_WINDOW用于定义当用户使用窗口管理器显示关闭窗口时的事件   tkinter协议处理机制 protocol是此协议回调函数（必须是root或者Toplevel组件）
    # 一旦注册处理函数，tkinter将不再自动关闭程序
    root.protocol('WM_DELETE_WINDOW', closeWindow)

    # 启动消息主循环
    root.mainloop()
