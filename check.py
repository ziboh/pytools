import chardet
import sys


def code2code(soure_file, code_int="gbk", code_put="utf-8"):
    try:
        with open(soure_file, "rb+") as f:
            date = f.read(4096)
            result = chardet.detect(date)

            if result["encoding"] == 'GB2312' or result["encoding"] == 'GBK' or result["encoding"] == 'GB18030':
                tmp = b''
                while date:
                    tmp += date
                    date = f.read(1024)

                content = tmp.decode(result["encoding"])

                tmp = content.encode("utf-8")

                f.seek(0)
                f.truncate()
                f.write(tmp)
    except Exception as e:
        pass


def main():
    argv_count = len(sys.argv)
    if argv_count == 2:

        code2code(sys.argv[1])


if __name__ == "__main__":
    main()
