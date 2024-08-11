import pytest
from common.text_util import *
from common.excel_util import *

@pytest.fixture(scope='session',autouse=True)
def truncate():
    """执行用例前，先清空data下相关文件"""
    print("\n用例执行前操作：")
    print("1、清空run_result.txt文件")
    truncate_text("%s/data/run_result.txt" % base_dir)
    print("2、清空extract_save.txt文件")
    truncate_text("%s/data/extract_save.txt" % base_dir)
    print("3、清空extract_replace.txt文件")
    truncate_text("%s/data/extract_replace.txt" % base_dir)
    print("4、清空extract.yaml文件")
    truncate_text("%s/data/extract.yaml" % base_dir)
    yield
    print("用例运行完毕")
@pytest.fixture(scope="function")
def login():
    print("用例执行前，先登录")

@pytest.fixture(scope='package',autouse=True)
def handelExcelToYaml():
    ExcelUtil("%s/data/case_excel/MCC自动化测试表格.xlsx" % base_dir).handle_excel()

