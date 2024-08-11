import json
from common.excel_util import *
import requests

from common.text_util import *
def request_utl(method,url,headers,payloads,params=None,expect=None,run_result_txt=None,resultWriteExcel=None,resultWriteSheet=None):
    if method=='get':
        res=requests.get(url=url,headers=headers,params=params)
        assertion=expect in res.text
        if assertion:
            assert assertion
            #将运行结果写入txt
            write_text(text_file=run_result_txt,data=res.text+"__pass|")
            # 根据sheet名返回执行结果写入excel
            ExcelUtil(resultWriteExcel=resultWriteExcel).write_excel(resultWriteSheet=resultWriteSheet)
        else:
            write_text(text_file=run_result_txt,data=res.text+"__fail|")
    elif method=='post':
        payloads=json.loads(payloads)
        res=requests.post(url=url,data=payloads,headers=headers)
        print(res.text)
        assertion =expect in res.text
        if assertion:
            assert assertion
            # 将运行结果写入txt
            write_text(text_file=run_result_txt, data=res.text + "__pass|")
            #根据sheet名返回执行结果写入excel
            ExcelUtil(resultWriteExcel=resultWriteExcel).write_excel(resultWriteSheet=resultWriteSheet)
        else:
            write_text(text_file=run_result_txt, data=res.text + "__fail|")
            # 根据sheet名返回执行结果写入excel
            ExcelUtil(excel_path=resultWriteExcel).write_excel(resultWriteSheet=resultWriteSheet)


