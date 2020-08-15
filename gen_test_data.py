
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用
import os,sys
import time
import random

def gen_test_data(o_file, rows=1000000):
    row_count=0
    outfile=open(o_file, 'w', encoding='utf-8')

    while row_count<rows:
        row_count += 1
        num=random.randint(1,10000000)
        out_str='CN00' + 'KEY%042d' %row_count + 'MAIN%0914d' %num
        outfile.write(out_str)
        if(row_count < rows):
            outfile.write('\n')

    outfile.close()
    return 0

if __name__ == "__main__":
    gen_test_data('tbspacn0.20200815.txt', 110)
    # gen_test_data('tbspacn0.20200815.txt', 110)
