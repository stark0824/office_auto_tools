# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/5/11
# +----------------------------------------------------------------------
# | Desc: 运行环境 Python 3.10.4 统计文件字数 写入内容
# +----------------------------------------------------------------------

from pathlib import Path,PurePath

src_path = "/Users/stark/Desktop/long_pic";

p = Path(src_path);
dict = {}
con = {}
files = [ x for x in p.iterdir() if PurePath(x).match("*.txt") ]
for fileObj in files :
    with open(fileObj,encoding='utf-8') as f :
        files_name = fileObj.name;
        print(files_name);
        contents = f.read()
    words = contents.rstrip()
    number = len(words)
    dict[files_name] = number;
    con[files_name] = contents;

print(dict);
print(con);

# 想追加写入内容,结尾加\n
desc = "把这段文字写入文件\n";
desc2 = "把这段文字写入文件dsads\n"
p = "/Users/stark/Desktop/long_pic/test.txt"
with open(p,"w") as f :
    f.write(desc)
    f.write(desc2)