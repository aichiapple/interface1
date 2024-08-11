import re
from common.text_util import *
from common.yaml_util import *
from pathlib import Path

base_dir = Path(__file__).parent.parent

def extract_util(case_file,extract_yamefile="%s/data/data_drivern_yaml/extract.yaml" % base_dir,default_yamlfile="%s/data/data_driven_yaml/default_variable.yaml" % base_dir):
    """
    数据关联的公共方法
    运行用例前，检查用例yaml中是否有${}
    有，则检查${}中的变量是否存在与extract.yaml中
    有，则替换，无则不变，或者设置默认值
    内存中覆盖yaml中读取的值
    在进行数据驱动
    :param case_file:
    :param extract_yamefile:
    :param default_yamlfile:
    :return:
    """
    #运行用例
    text_file='%s/data/extract_replace.txt' % base_dir
    #运行前先清空extract.txt
    truncate_text(text_file)
    #返回全部匹配到的结果，且去重
    value_cases=str(read_yaml(case_file))
    write_text(text_file='%s/data/extract_replace.txt' % base_dir,data=value_cases)
    p=r'\$\{(.*?)\}'
    match_list=list(set(re.findall(p,value_cases)))

    #2、提取字段的key列表（关联变量和用户默认变量，将他们合并）
    global value_extract_keys,value_extract
    if read_yaml(extract_yamefile):
        value_extract=read_yaml(extract_yamefile)
        print(value_extract)
        value_default_variable=read_yaml(default_yamlfile)
        value_extract.update(value_default_variable)
        value_extract_keys=list(value_extract.keys())
        print(value_extract_keys)
    else:
        print("extract.yaml文件中没有存储的变量")
        if read_yaml(default_yamlfile):
            value_default_variable=read_yaml(default_yamlfile)
            value_extract_keys=list(value_default_variable.keys())
            print(value_extract_keys)

    #3 动态替换${}
    for m in match_list:
        if m in value_extract_keys:
            p1=r'\${%s}' % m
            replace=re.sub(p1,value_extract[m],read_text(text_file))
            write_text(text_file=text_file,data=replace)
        else:
            print("关联数据中，没有该key:%s" % m)
        return eval(read_text(text_file))['cases']

def save_variable(key,value):
    """保存变量到extract.yaml文件，需要模块运行前先进行清空"""
    #1\数据按格式追加写入extract_save.txt文件
    file='%s/data/extract_save.txt' % base_dir
    extract_yamlfile="%s/data/data_dirven_yaml/extract.yaml" % base_dir
    write_text(file,'"%s":"%s",' % (key,value))
    variable=eval("{%s}" % read_text(file)[0:-1])
    write_yaml(data=variable,yaml_file=extract_yamlfile)






