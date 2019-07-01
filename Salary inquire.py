def file_test():
  with open("info.txt",'r',encoding="utf-8") as f:
    file = list(f)
    return file
def server():
  for i in range(1):
    print("1.查询员工工资\n2.修改员工工资\n3.增加新员工记录\n4.退出")
    return i
loginSucces = False
while True:
    i = server()
    serial_number = input("请选择你的服务>>:")
    if serial_number.isdigit():
      serial_number = int(serial_number)
      file = file_test()
      if serial_number < 5 and serial_number >= 0:
        if serial_number == 1:
          name = input("请输入要查询的员工姓名:").strip()
          for i in file:
            file = i.strip().split()
            if name in file:
              break
          for i in file:
            if name in file:
              name_sum = file[1]
              print("%s的工资是：%s\n"%(name,name_sum,))
              break
          else:
            print("没有此用户！\n")
        elif serial_number == 2:
          name_old = input("请输入要修改的员工姓名:").strip()
          for ii in file:
            file = ii.strip().split()
            if name_old in file:
              print(file)
              sum_old = file[1]
              name_alter,sum_alter = input("请输入修改的新员工工号和姓名和工资，用空格分割:").strip().split()
              with open("info.txt","r",encoding="utf-8") as f:
                lines = f.readlines()
              with open("info.txt","w",encoding="utf-8") as f_a:
                for line in lines:
                  if name_old in line:
                    line = line.replace(name_old,name_alter)
                  f_a.write(line)
                f_a.close()
                with open("info.txt", "r", encoding="utf-8") as f:
                  lines = f.readlines()
                with open("info.txt", "w", encoding="utf-8") as f_b:
                  for line in lines:
                    if name_alter in line:
                      line = line.replace(sum_old,sum_alter)
                    f_b.write(line)
                  f_b.close()
                  print("修改成功")
                  break
                  if loginSucces == True: break
          else:
            print("没有此用户！\n")
        elif serial_number == 3:
          try:
            name_new, sum_new = input("请输入要增加的员工姓名和工资，用空格分割:").strip().split()
          except ValueError:
            print("输入的参数不够！\n")
          else:
            if name_new.isalpha() and sum_new.isdigit():
              for ii in file:
                file = ii.strip().split()
                if name_new not in file:
                  with open("info.txt", "a+", encoding="utf-8") as f_c:
                    f_c.write("\n%s %s"%(name_new,sum_new))
                  print("增加成功")
                  break
                  if loginSucces == True: break
            else:
              print("参数类型不对！\n")
        elif serial_number == 4:
          print("谢谢使用，下次再见！")
          exit()
      else:
        print("请输入正确的序号！")
    else:
      print("输入的不是整数！\n")