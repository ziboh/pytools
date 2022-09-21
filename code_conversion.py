import chardet
import sys
import tkinter.messagebox as messagebox

def code2code(soure_file, code_int="gbk", code_put="utf-8"):
    try:
        with open(soure_file, "rb+") as f:
            date = f.read()
            result = chardet.detect(date)
            print(f'This language is {result["language"]}')
            print(f'This result is {result}')
            if result["encoding"] != 'utf-8':
                tmp = b''
                while date:
                    tmp += date
                    date = f.read(1024)
                try:
                    content = tmp.decode("GB18030")
                    print(f'This content is {content}')
                except Exception as e:
                    return 0
                tmp = content.encode("utf-8")
                f.seek(0)
                f.truncate()
                f.write(tmp)
                return 2
            else:
                return 1
    except Exception as e:
        return 3


def gui(title, content, showflag="success"): 
    if showflag == "success":
        messagebox.showinfo(title, content)
    elif showflag == "error":
        messagebox.showerror(title, content)
    elif showflag == "warning":
        messagebox.showwarning(title, content)
    else:
        messagebox.showerror(title, "程序错误")


def main():
    argv_count = len(sys.argv)
    if argv_count == 2:
        result = code2code(sys.argv[1])
        if result == 0:
            gui("error", "编码不为中文", "error")
        elif result == 1:
            gui("warning", "文件已经为utf-8", "warning")
        elif result == 2:
            # gui("success", "转换完成", "success")
            pass
        elif result == 3:
            gui("success", "文件打开异常", "error")
        else:
            gui("ereor", "未知错误", "error")


if __name__ == "__main__":
    main()