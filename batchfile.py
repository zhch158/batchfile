#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用
import os,sys
import argparse
import yaml
from utility import load_from_yaml
from jinja2 import Environment, FileSystemLoader, Template

import merge_tbspacn0
import gen_test_data

if __name__ == "__main__":
    # 测试用
    parser=argparse.ArgumentParser(description='根据配置文件，加工明细数据')
    parser.add_argument('--config', '-c', dest='inputfile', required=True, help='input config file')
    parser.add_argument('--section', '-s', dest='section', required=False, help='input section')
    parser.add_argument('--workdir', '-w', dest='workdir', required=False, help='input workdir')
    parser.add_argument('--yyyymmdd', '-d', dest='yyyymmdd', type=str, required=False, help='input year month day[20200815]')
    # parser.add_argument('--keylength', '-k', dest='key', type=str, required=False, help='input keylength[1:49]')

    # parser.print_help()

    tb_dict=None
    workdir=yyyymmdd=None

    if(len(sys.argv) == 1):
        # parser.print_help()
        # args=parser.parse_args('--config ./batchfile.yaml'.split())
        args=parser.parse_args('--workdir ./ --yyyymmdd 20200815 --config ./batchfile.yaml --section gen_test_tbspacn0'.split())
        # args=parser.parse_args('--workdir ./data --config ./batchfile.yaml --section tbspacn0'.split())
    else:
        args=parser.parse_args()

    configfile = args.inputfile
    workdir=args.workdir
    yyyymmdd=args.yyyymmdd

    config_dic=load_from_yaml(configfile)

    config=config_dic.get("config", None)
    if(workdir==None):
        if(config!=None):
            workdir=config.get("workdir", './')
        else:
            workdir='./'
    config['workdir']=workdir
    if(yyyymmdd!=None):
        config['yyyymmdd']=yyyymmdd
    
    TemplateLoader = FileSystemLoader(searchpath=[os.path.dirname(configfile)])
    env = Environment(loader=TemplateLoader, variable_start_string='${', variable_end_string='}')
    md01 = env.get_template(configfile)
    content = md01.render(config)
    config_dic = yaml.load(content)

    section_name=args.section

    if(section_name==None or section_name=="tbspacn0"):
        tb_dict=config_dic.get("tbspacn0", None)
        if(tb_dict!=None):
            tb_list=tb_dict.get("输入文件", None)
            tb_output=tb_dict.get("输出文件", None)
            tb_func=tb_dict.get("处理方法", None)
            main_file, main_begin, main_length=tb_list[0]
            temp_file, temp_begin, temp_length=tb_list[1]

            print("func=%s, main_file=%s, main_begin=%d, main_length=%d, temp_file=%s, temp_begin=%d, temp_length=%d, o_file=%s)" 
                %(tb_func, main_file, main_begin, main_length, temp_file, temp_begin, temp_length, tb_output))
            func=getattr(merge_tbspacn0, tb_func, None)
            if(func==None):
                print('Func{%s] is not found' %(tb_func))
            else:
                func(main_file, main_begin, main_length, temp_file, temp_begin, temp_length, o_file=tb_output)

    elif(section_name=="gen_test_tbspacn0"):
        tb_dict=config_dic.get("gen_test_tbspacn0", None)
        if(tb_dict!=None):
            tb_list=tb_dict.get("输出文件", None)
            tb_func=tb_dict.get("处理方法", None)
            main_file, main_rows=tb_list[0]
            temp_file, temp_rows=tb_list[1]

            print("func=%s, main_file=%s, main_rows=%d, temp_file=%s, temp_rows=%d)" 
                %(tb_func, main_file, main_rows, temp_file, temp_rows))
            if(temp_rows<=0 or temp_rows>=main_rows/10):
                print("temp_rows must less than main_rows/10")
                exit(1)
            func=getattr(gen_test_data, tb_func, None)
            if(func==None):
                print('Func{%s] is not found' %(tb_func))
            else:
                func(main_file, main_rows, temp_file, temp_rows)
