import os
import shutil
import time

import pytest

from utils.OsPathUtil import REPORT_DIR, DATA_DIR, CASE_DIR, CONF_DIR, BAK_DIR

# 文件备份
date2display = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
date2display_cut = date2display[:10]
if not os.path.exists(os.path.join(BAK_DIR, f'{date2display_cut}')):
    shutil.copytree(DATA_DIR, os.path.join(BAK_DIR, f'{date2display_cut}'))

pytest_cmd = [CASE_DIR, '-vlsq', '--alluredir', f"{REPORT_DIR}\\.allureTemp", "--clean-alluredir"]
pytest.main(pytest_cmd)
shutil.copyfile(f"{CONF_DIR}\\environment.properties", f"{REPORT_DIR}\\.allureTemp\\environment.properties")
# shutil.copyfile(f"{REPORT_DIR}\\allure\\history", f"{REPORT_DIR}\\.allureTemp\\history")
os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
