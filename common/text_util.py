from pathlib import Path
base_dir=Path(__file__).parent.parent

def read_text(text_file):
    """读取text文件"""
    with open(text_file,'r',encoding='utf-8') as f:
        return f.read()


def write_text(text_file,data):
    with open(text_file,'w',encoding='utf-8') as f:
        f.write(data)

def truncate_text(text_file):
    with open(text_file,'w') as f:
        f.truncate()

def read_text_handel(text_file='%s/data/run_result.txt' % base_dir):
    """将保存运行结果的txt文件，处理成想要的数据"""
    value=read_text(text_file=text_file)
    l_reponse=[]
    l_ispass=[]
    for i in value[0:-1].split("|"):
        l_reponse.append(i.split('__')[0])
        l_ispass.append(i.split('__')[1])

    print(l_reponse)
    print(l_ispass)
    return l_reponse,l_ispass


