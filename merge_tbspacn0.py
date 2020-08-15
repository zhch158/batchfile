
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用
import os,sys
import time

def merge_tbspacn0(main_file, main_begin, main_length, temp_file, temp_begin, temp_length, o_file):
    left_row_count=right_row_count=1
    left_row=right_row=None
    outfile=open(o_file, 'w', encoding='utf-8')
    with open(main_file, 'r', encoding='utf-8') as f1, open(temp_file, 'r', encoding='utf-8') as f2:
        left_row = f1.readline()
        right_row = f2.readline()
        while left_row != None and len(left_row)>0:
            if(left_row_count%1000000==0):
                print("[%s], left have read[%d], right have read[%d]" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), left_row_count, right_row_count))
            if(right_row == None or len(right_row)==0):
                #左文件有数据，右文件没有数据
                outfile.write(left_row)
                left_row = f1.readline()
                left_row_count+=1
                continue
            elif(left_row[main_begin-1:main_length] == right_row[temp_begin-1:temp_length]):
                outfile.write(right_row)
                left_row = f1.readline()
                left_row_count+=1
                right_row = f2.readline()
                if(right_row == None or len(right_row)==0):
                    if(left_row!=None and len(left_row)>0):
                        outfile.write('\n')
                else:
                    right_row_count+=1
                continue
            elif(left_row[main_begin-1:main_length] < right_row[temp_begin-1:temp_length]):
                outfile.write(left_row)
                left_row = f1.readline()
                left_row_count+=1
                continue
            else:
                right_row = f2.readline()
                if(right_row != None and len(right_row)>0):
                    right_row_count+=1

    outfile.close()
    print("[%s], left have read[%d], right have read[%d]" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), left_row_count-1, right_row_count))
    return 0
