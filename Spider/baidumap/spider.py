import xlrd
from xlutils import copy
import os
import requests
import json
import time


def WriteExcel():
    sSaveName = r'C:\Users\pqxuan\Desktop\公司地址核对.xls'
    oBook = xlrd.open_workbook(r'C:\Users\pqxuan\Desktop\addr.xls')
    oNewBook = copy.copy(oBook)
    oSheet = oBook.sheet_by_name('Sheet1')
    oNewSheet = oNewBook.get_sheet(0)
    for i in range(oSheet.nrows):
        lLine = oSheet.row_values(i)
        if len(lLine) < 3:
            continue
        if lLine[1] in ('公司名称', ''):
            continue
        lAddress = GetAddress(lLine[1])
        for y in range(len(lAddress)):
            oNewSheet.write(i, y + 2, lAddress[y])
        time.sleep(0.001)
        print(lLine[1], lAddress)
    os.remove(sSaveName)
    oNewBook.save(sSaveName)


def GetAddress(sCompany):
    query = r'newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&' \
            'wd={keyword}&c=75&src=0&wd2=&pn=0&sug=0&l=13&b=(11557560.82,3561099.48;11619000.82,' \
            '3573899.48)&from=webmap&biz_forward={%22scaler%22:1,' \
            '%22styles%22:%22pl%22}&sug_forward=&auth=yHMaUwxXg5cLAZKG3bcPBR25O9xvaUxfuxLEzRHLzHxtA' \
            '%3Dk6Amkbz8yvYgP1PcGCgYvjPuVtvYgPMGvgWv%40uxtw8055yS8v7uvYgP%40vYZcvWPCuVtvYgP' \
            '%40ZPcPPuVtvYgPhPPyheuVtvhgMuxVVty1uVtCGYuVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuVtPYIuVtPYIUvhgMZSguxzBEHLNRTVtlEeLZNz1G8DjKal3hJYyuVt%40ZPuVtc3CuVteuVtegvcguxLEzRHLzHxtosSSEb1rZZWuV&seckey=WEu2p0m8dt6xRATlm8ps7uKhIeqQrzZIBjlqdnHxLlY%3D%2C8pFMXw-4VsHjuhlGDY3wtlF4BnzLzh-uDiewZpsppwl3fbjIQcZaov_nmNEHDC_no7YmfzfbEvker0GVQLbbjwZ3IAdiqg6r5CiExlUPMeP9EB4txkFZd3-3nRDIf78fmKUZ7kLCvuUjYWJjmgH8YcvneETsaWkhL4RwSp3te9wd_7sHKx_OmYAKAYQZxflA&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12635092,2633917&ie=utf-8&t=1642856262456&newfrom=zhuzhan_webmap'

    query = query.replace('{keyword}', sCompany)

    sBaseUrl = 'https://map.baidu.com/?%s' % query

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36',
    }

    r = requests.get(sBaseUrl, headers)
    jText = json.loads(r.text)
    content = jText.get('content', [])
    if not content:
        return []
    lRes = []
    for dNote in content:
        lNote = []
        for s in ('addr', ):
            lNote.append(dNote.get(s, 'none'))
        lRes.append(' '.join(lNote))
    return lRes


if __name__ == '__main__':
    WriteExcel()
    # print(GetAddress('z'))
