import requests

cookies = {
    'PHPSESSID': 'Вставить сюда',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=nbpahmh62v964avqnmb8gp1gb7; _ym_uid=1692850126258532426; _ym_d=1692850126; _ym_isad=1; _ym_visorc=w',
    'Referer': 'http://sevtransport-online.ru/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

response = requests.get(
    'http://sevtransport-online.ru/php/getVehiclesMarkers.php?rids=131-0,335-0,1-1,2-1,119-0,120-0,133-0,132-0,128-0,129-0,360-0,359-0,366-0,365-0,330-0,332-0,121-0,136-0,137-0,115-0,116-0,113-0,114-0,138-0,139-0,140-0,141-0,333-0,331-0,107-0,108-0,126-0,127-0,251-0,252-0,124-0,125-0,162-0,163-0&lat0=0&lng0=0&lat1=90&lng1=180&curk=0&city=sevastopol&info=12345&_=1692854146534',
    cookies=cookies,
    headers=headers,
    verify=False,
)

laz = list(map(str, range(1047, 1056))) + list(map(str, range(2032, 2039)))
mega0 = list(map(str, range(1056, 1070))) + ["1071"] + list(map(str, range(2039, 2047)))
mega2 = list(map(str, range(1072, 1095))) + ["1115"] + list(map(str, range(1123, 1165))) + list(map(str, range(2050, 2071))) + list(map(str, range(2085, 2108)))
mega3 = list(map(str, range(1095, 1123))) + list(map(str, range(2071, 2085)))
mega5 = ["2049"]
avangard = list(map(str, range(3000, 3200)))
umz = list(map(str, range(1030, 1047)))
ziu = list(map(str, range(1003, 1030))) + list(map(str, range(2000, 2032)))
optima = ["1070", "2047", "2048"]
models = [["Лаз", laz], ["Мегаполис.00", mega0], ["Мегаполис.02", mega2], ["Мегаполис.03", mega3],
          ["Мегаполис.05", mega5], ["Авангард", avangard], ["ЮМЗ", umz], ["ЗИУ", ziu], ["Оптима", optima]]
trolls = []
for troll in response.json()["anims"]:
    trolls.append([int("".join(c for c in troll["rnum"] if c.isdigit())), troll["rnum"], "".join(c for c in troll["gos_num"] if c.isdigit()), str(troll["lat"]), str(troll['lon'])])
trolls.sort()
for troll in trolls:
    if troll[1] != "К1":
        print(*troll[1:3], end=' ')
        for model in models:
            if str(troll[2]) in model[1]:
                print(model[0], end='   ')
        lat = troll[3][:2]+'.'+troll[3][2:]
        lon = troll[4][:2]+'.'+troll[4][2:]
        print(lat, lon, "http://www.google.com/maps/place/"+lat+","+lon)