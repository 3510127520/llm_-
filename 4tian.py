  #让用户输入文件夹路径
folder_path= input("请输入文件夹需要扫描路径")
import logging
from pathlib import Path

#配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s -%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),#输出到屏幕
        logging.FileHandler('app.log',encoding='utf-8')#输出到文件
    ]
)

#第一个函数：负责扫描循环拿文件
def scan_folder(folder_path,filter_ext=None,search_key=None):
    """扫描文件及，统计文件类型，支持过滤扩展名"""
    folder =Path(folder_path)
    if not folder.exists():#检查路径是否存在，如果不存在主动抛出个错误
        raise ValueError(f"路径不存在:{folder_path}")#raise是抛出错误信息的作用

    #检查路径是不是文件夹
    if not folder.is_dir():
        raise ValueError(f"不是文件夹:{folder_path}")
    stats ={} #空字典
    for file_path in folder.iterdir():#for  in  循环拿取 older.iterdir() 启动了扫描仪
        if file_path.is_file():#判断这个东西是文件吗
           if search_key and search_key.lower() not in file_path.name.lower():#加一个搜索功能，这个是判断是不是这个搜索的关键词
               continue
           extension = file_path.suffix #比如".txt"
# 如果扩展名为空，则是说明没有扩展名的文件
           if filter_ext and extension !=filter_ext:#设置过滤，跳过不匹配的文件，filter_ext用来接受用户想过滤的扩展名
               continue #作用跳过这个文件继续下一个
           stats[extension] =stats.get(extension,0) + 1
#用字典统计
    return stats

#第二个函数；负责生成要打印的文字
def generate_report(stats,folder_path):#生成Markdown格式（让打印的文字更好看，有大有小有加粗）的统计报告
   lines =[]  #准备一个空列表，用来装报告这行 
   #标题
   lines.append(f"#文件类型报告文件")
   lines.append(f"")
   lines.append(f"**扫描路径**:'{folder_path}'")
   lines.append(f"**扫描时间:{__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
   lines.append(f"")
   lines.append(f"##统计结果")
   lines.append(f"")
   lines.append(f"|文件类型|数量|")
   lines.append(f"| :--- | :--- |")
   for exe, count in stats.items():
     ext_display = exe if exe else "无扩展名"
     lines.append(f"|{ext_display}:{count}|")
#总计
   total = sum(stats.values())
   lines.append(f"")
   lines.append(f"**总计**: {total}个文件")
   return "\n".join(lines)#把列表拼成一段完整的文字

#第三个函数：负责把文字存进文件
def sava_report(content, filename="report.md"):
   #保存报告到Markdown文件
   with open(filename,"w",encoding="utf-8") as f:
          f.write(content)


#总指挥：把上面三个函数组合起来使用
def main():
    #1,问地址
    folder_path = input("请输入文件夹需要扫描路径；")
#询问是否要过滤的扩展名字
    filter_input = input("请输入要过滤的扩展名字（如.txt，直接回车不过滤）；").strip()
    filter_ext = filter_input if filter_input else None

    search_input = input("请输入文件关键词（直接回车跳过）；").split()
    search_key = search_input if search_input else None
#使用try/except 包裹可能出错的代码，如果try出错了会跳到excpet，excpet放出错执行的内容
    try:
    #调用1，拿到统计结果
     stats = scan_folder(folder_path,filter_ext,search_key)
    #调用2，生成报告文字
     report = generate_report(stats,folder_path)
    #打印到屏幕
     print(report)
    #调用3，保存文件
     sava_report(report)
     logging.info("\n报告已经保存到report.txt")
    except ValueError as e:#把错误内容存到变量e里面
        #用户输入错误路径时，显示友好提示
        logging.error(f"错误：{e}")#有变量的时候打印就需要加f，他可以把变量里的内容显示出来，而不是打印变量本身这个e
        logging.info("请检查路径是否正确，然后重新运行程序。")
    except Exception as e:
        #其他未知错误
        logging.error(f"发生未知错误：{e}")
        logging.info("请截图这个错误信息，联系ai")

#这句话是告诉python：只有当我主动运行这个文件时，才执行总指挥
if __name__ == "__main__":
    main()   
        
