from hashlib import md5
#ascii_letters是生成所有字母，digits是生成所有数字
from string import ascii_letters,digits
#创建一个迭代器，返回iterable中所有长度为r的项目序列，如果省略了r，那么序列的长度与iterable中的项目数量相同： 返回p中任意取r个元素做排列的元组的迭代器
from itertools import permutations
from time import time

all_letters = ascii_letters + digits + '.,;' #候选字符集
def decrypt_md5(md5_value):
    if len(md5_value) != 32:
        print('error')
        return
    md5_value = md5_value.lower() #转化成小写
    for k in range(5,10):
        for item in permutations(all_letters,k):                                #暴力测试
            item = ''.join(item)
            print('.',end='')#显示进度
            if md5(item.encode()).hexdigest() == md5_value:
                return item
md5_value = 'b932ae9220e9a413b39d9782605fee8f'
start = time()
result = decrypt_md5(md5_value)
if result:
    print('\nSuccess: '+md5_value+'==>'+result)
print('Time used:',time()-start)