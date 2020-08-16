
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用
import os,sys
import time
import random

def gen_test_tbspacn0(main_file, main_rows, temp_file, temp_rows):
    main_row_count=temp_row_count=0
    f1=open(main_file, 'w', encoding='utf-8')
    f2=open(temp_file, 'w', encoding='utf-8')

    temp_row_count += 1
    num=random.randint(1,10000000)
    out_str='CN00' + 'KEY%042d' %main_row_count + 'MAIN%0909d-TAC0' %temp_row_count
    f2.write(out_str)
    f2.write('\n')
    while main_row_count<main_rows:
        main_row_count += 1
        num=random.randint(1,10000000)
        out_str='CN00' + 'KEY%042d' %main_row_count + 'MAIN%0914d' %num
        f1.write(out_str)
        if(main_row_count < main_rows):
            f1.write('\n')

        if(main_row_count == int(temp_row_count*main_rows/temp_rows) and temp_row_count<temp_rows):
            temp_row_count += 1
            out_str='CN00' + 'KEY%042d' %main_row_count + 'MAIN%0909d-TAC0' %temp_row_count
            f2.write(out_str)
            f2.write('\n')
        if(main_row_count%int(main_rows/10)==0):
            print("[%s], have generated tbspacn0[%d], tbsptac0[%d]" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), main_row_count, temp_row_count))

    temp_row_count += 1
    main_row_count += 1
    out_str='CN00' + 'KEY%042d' %main_row_count + 'MAIN%0909d-TAC0' %temp_row_count
    f2.write(out_str)
    print("[%s], have generated tbspacn0[%d], tbsptac0[%d]" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), main_row_count-1, temp_row_count))

    f1.close()
    f2.close()
    return 0

if __name__ == "__main__":
    gen_test_tbspacn0('tbspacn0.20200815.txt', 110, "tbsptac0.20200815.txt", 10)
    # gen_test_data('tbspacn0.20200815.txt', 110)
