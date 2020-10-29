import sys

def make_file(day: str):
    with open('template.html', 'r') as file:
        html = file.read()
        
    # ファイルが存在しない場合のみ書き込みする
    new_file = day + '.html'

    try:
        with open(new_file, mode='x') as f:
            # 置換
            tar_1 = '20' + day[0:2] + '/' + day[2:4] + '/' + day[4:6]
            tar_2 = str(int(day) - 1) + '.html'
            tar_3 = str(int(day) + 1) + '.html'
            html = html.replace('target_1', tar_1)
            html = html.replace('target_2', tar_2)
            html = html.replace('target_3', tar_3)
            f.write(html)
    except FileExistsError:
        pass


def main():
    try:
        day = sys.argv[1]
        make_file(day)
    except IndexError:
        pass

if __name__ == "__main__":
    main()