import os
import sys
import argparse
# 线程安全队列实现
from queue import Queue
# 线程
from threading import Thread
# 高级文件，文件夹，压缩包处理模块
from shutil import copyfile


def copyFile(src, dst, num):
    # 使用num个线程复制src目录下的文件到dst目录中
    # 源文件必须存在
    assert os.path.isdir(src), src+'must be an existing directory.'
    # 如果目标文件夹不存在，创建一个
    if not os.path.isdir(dst):
        os.makedirs(dst)
    # 最多容纳10个元素的队列
    q = Queue(10)

    def add(src):
        for f in os.listdir(src):
            f = os.path.join(src, f)
            if os.path.isfile(f):
                q.put(f)
            elif os.path.isdir(f):
                q.put(f)
                # 递归
                add(f)
        # 用来通知工作线程在没有文件需要复制了
        for _ in range(num):
            q.put(None)
    # 创建并启动往队列中存放元素的线程
    t_add = Thread(target=add, args=(src,))
    t_add.start()

    def copy(name):
        # 工作线程函数
        while True:
            srcItem = q.get()
            if srcItem == None:
                print(name, 'quit...')
                break
            # 替换字符串，生成目标路径
            dstItem = srcItem.replace(src, dst)
            print('{0}:{1}==>{2}'.format(name, srcItem, dstItem))

            # 复制文件
            if os.path.isfile(srcItem):
                # 根据需要创建目标文件夹
                dstDir = os.path.split(dstItem)[0]
                if not os.path.isdir(dstDir):
                    try:
                        os.makedirs(dstDir)
                    except FileExistsError as e:
                        pass
                copyfile(srcItem, dstItem)
            elif os.path.isdir(srcItem):
                # 创建目标文件夹
                try:
                    os.makedirs(dstItem)
                except FileExistsError as e:
                    pass
    for _ in range(num):
        t = Thread(target=copy, args=('Tread'+str(_),))
        t.start()


if __name__ == '__main__':
    # 解系命令行参数
    parser = argparse.ArgumentParser(description='copy files from src to dst')
    parser.add_argument('-s', '--src')
    parser.add_argument('-n', '--num', default='5')
    args = parser.parse_args()

    if args.src != None and args.dst != None:
        copyFile(args.src, args.dst, int(args.num))
    else:
        print('Please use the following command to see how to use:')
        print(' '+sys.argv[0]+' -h')
