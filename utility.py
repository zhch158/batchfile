#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用
# from __future__ import print_function
import json  
import yaml
import os
import time

def dump_dic(target, dic_list):
    f=open(target,"w", encoding="utf-8")
    for dic in dic_list:  
        json.dump(dic, f, ensure_ascii=False)
        f.write("\n")
    f.close()

def load_dic(src, dic_list):
    f=open(src,"r", encoding="utf-8")
    # data=list()
    for line in f:
        l=line.strip()
        if(len(l)==0 or l[0]=="#"):
            continue
        else:
            dic_list.append(json.loads(l))
    # logger.debug(dic_list)
    f.close()

def sub_var_value(src, var_dic):
    target=""
    target=src.format(**var_dic)
    return target

def load_from_yaml(src):
    f = open(src, encoding='utf-8')
    x = yaml.load(f, Loader=yaml.FullLoader)
    f.close()

    return x

def find_config(dic_list, configid, key="ID"):
    for dic in dic_list:
        # if(dic.has_key(key)):
        if(key in dic and dic[key]==configid):
            return dic
        else:
            continue
    return None
