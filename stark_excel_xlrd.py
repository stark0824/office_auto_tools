# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/5/10
# +----------------------------------------------------------------------
# | Desc: 运行环境 Python 3.10.4
# |      .xlsx pip install xlrd==1.2.0
# |      .xls pip install xlrd 最新版本不支持.xlsx pip uninstall xlrd
# +----------------------------------------------------------------------
import xlrd
from pathlib import Path, PurePath


def get_log_contents(path):
    p = Path(path)
    files = [x for x in p.iterdir() if PurePath(x).match('*.xlsx')]
    contents = []
    for file in files:
        data = xlrd.open_workbook(file)
        table = data.sheets()[0]
        for i in range(5, 13):
            log = table.cell_value(rowx=i, colx=2)
            if len(log) != 0:
                contents.append(log)

    return contents


src_path = "/Users/stark/Desktop/cp_logs/2022"
contents = get_log_contents(src_path)
print(contents)

# 输出结果:
# excel里指定的内容....
