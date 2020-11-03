import sys
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

def make_file():
    with open('template.html', 'r') as file:
        html = file.read()
        
    # ファイルが存在しない場合のみ書き込みする
    today = datetime.today()
    d_file = datetime.strftime(today, '%y%m%d')
    d_today = datetime.strftime(today, '%Y/%m/%d')
    new_file = d_file + '.html'

    try:
        with open(new_file, mode='x') as f:
            # 日付
            today = datetime.today()
            yesterday = today - timedelta(days=1)
            tomorrow = today + timedelta(days=1)
            one_month_ago = today - relativedelta(months=1)
            one_month_after = today + relativedelta(months=1)
            # 6桁
            d_today = datetime.strftime(today, '%Y/%m/%d')
            d_yesterday = datetime.strftime(yesterday, '%y%m%d')
            d_tomorrow = datetime.strftime(tomorrow, '%y%m%d')
            d_one_month_ago = datetime.strftime(one_month_ago, '%y%m%d')
            d_one_month_after = datetime.strftime(one_month_after, '%y%m%d')
            # 置換
            tar_1 = d_today
            tar_2 = d_one_month_ago + '.html'
            tar_3 = d_yesterday + '.html'
            tar_4 = d_tomorrow + '.html'
            tar_5 = d_one_month_after + '.html'
            html = html.replace('target_1', tar_1)
            html = html.replace('target_2', tar_2)
            html = html.replace('target_3', tar_3)
            html = html.replace('target_4', tar_4)
            html = html.replace('target_5', tar_5)
            f.write(html)
    except FileExistsError:
        pass


def main():
    try:
        # day = sys.argv[1]
        make_file()
    except IndexError:
        pass

if __name__ == "__main__":
    main()