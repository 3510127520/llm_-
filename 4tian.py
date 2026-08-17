  #让用户输入文件夹路径
folder_path= input("请输入文件夹需要扫描路径")
from pathlib import Path

stats ={} #空字典

folder =Path(folder_path) #找遍文件夹下所有文件（不包括子文件夹）
for file_path in folder.iterdir():#for  in  循环拿取 older.iterdir() 启动了扫描仪
    if file_path.is_file():#判断这个东西是文件吗
        print(file_path.name)  #只打印名字
#获取扩展名
        extension = file_path.suffix #比如".txt"
# 如果扩展名为空，则是说明没有扩展名的文件
        stats[extension] =stats.get(extension,0) + 1
#用字典统计


#打印报告
print("文件类型统计报告")
print('-' * 30)
for exe, count in stats.items():
    ext_display = exe if exe else "无扩展名"
    print(f"{ext_display}:{count}个")

#保存到文件
with open("report.txt","w",encoding="utf-8") as f:
    f.write("文件类型统计报告\n")
    f.write('-' * 30 + "\n")
    for exe, count in stats.items():
       ext_display = exe if exe else "无扩展名"
       f.write(f'{ext_display}:{count}个\n')

print("\n报告已保存到 report.txt")
            
