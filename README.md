# 批量文件处理, batchfile
1. #### 程序说明
程序说明|程序名称
--|:--:|
批处理合并配置文件|batchfile.yaml
批处理合并主程序|batchfile.py
批处理合并DEMO|merge_tbspacn0.py
生成测试数据|gen_test_data.py
工具函数|utility.py

2. #### 程序用法
```
usage: batchfile.py [-h] --config INPUTFILE [--section SECTION] [--workdir WORKDIR]
                    [--yyyymmdd YYYYMMDD]

根据配置文件，加工明细数据

optional arguments:
  -h, --help            show this help message and exit
  --config INPUTFILE, -c INPUTFILE
                        input config file
  --section SECTION, -s SECTION
                        input section
  --workdir WORKDIR, -w WORKDIR
                        input workdir
  --yyyymmdd YYYYMMDD, -d YYYYMMDD
                        input year month day[20200815]
```