import pytest
from common.text_util import *
from common.yaml_util import *
from common.request_util import *
import json
@pytest.mark.parametrize('args',read_yaml('%s/data/data_yaml/1.登录.yaml' % base_dir)['cases'])
def test_login(args):
    print(str(args))
    """登录接口，获取token"""
    url=args['url']
    headers=eval(args['head'])
    payloads=json.dumps(eval(args['body']))
    params=eval(args['body'])
    method=args['method']
    run_result_txt='%s/data/run_result.txt' % base_dir
    expect=args['expect']
    res=request_utl(method=method,url=url,headers=headers,payloads=payloads,params=params,expect=expect,run_result_txt=run_result_txt,
                    resultWriteExcel='%s/data/case_excel/MCC自动化测试表格.xlsx' % base_dir,resultWriteSheet='1.登录')

