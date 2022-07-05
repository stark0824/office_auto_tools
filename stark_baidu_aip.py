# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/5/10
# +----------------------------------------------------------------------
# | Desc: 百度云文字识别 baidu-aip
# |       依赖库 pip install chardet pip install baidu-aip
# +----------------------------------------------------------------------

from aip import AipOcr

#  https://ai.baidu.com/ 注册用户,创建应用

APP_ID = 'ID'
API_KEY = 'API_KEY'
SECRET_KEY = 'SECRET_KEY'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

src_path = '/Users/stark/Desktop/cp_logs/pytest/test_aip.png';
image = get_file_content(src_path)
result = client.basicGeneral(image)

info = []
for i in result['words_result']:
    info.append(i['words'])
print(info);
