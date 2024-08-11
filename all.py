import os
import time
from common.text_util import *
import pytest


def main():
    #运行用例的主入口
    truncate_text("%s/data/run_result.txt" % base_dir)
    pytest.main(['-vs','./testcase/test_login.py'])
    # tempdir_path="output/reports/temp/%stemp" % time.strftime("%y%m%d-%H%M%S")
    # os.system("pytest --alluredir %s" % tempdir_path)
    # os.system("allure generate %s"
    #           "-o output/reports/allure_report --clean" % tempdir_path)



if __name__ == '__main__':
    main()
