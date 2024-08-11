import yaml

from common.excel_util import ExcelUtil
from pathlib import Path
base_dir=Path(__file__).parent.parent

def read_yaml(yaml_file):
    """读取yaml"""
    with open(yaml_file,encoding='utf-8') as f:
        value = yaml.load(stream=f.read(),Loader=yaml.FullLoader)
        return value

def write_yaml(yaml_file,data):
    """写yaml"""
    with open(yaml_file,mode='w',encoding='utf-8') as f:
        yaml.dump(data=data,stream=f,allow_unicode=True)
def truncate_yaml(yaml_file):
    """清空yaml"""
    with open(yaml_file,"w") as f:
        f.truncate()
def handler():
    """根据读取excel数据，生成yaml的测试用例数据"""
    file='%s/data/case_excel/MCC自动化测试表格.xlsx' % base_dir
    value=ExcelUtil(file).wb.sheetnames
    sheet_names=ExcelUtil(file).wb.sheetnames
    n=0
    for sheet in sheet_names:
        data=value[n]
        file='%s/data/data_yaml/%s.yaml' % (base_dir,sheet)
        write_yaml(data=data, yaml_file=file)
        n+=1




