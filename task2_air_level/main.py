#23：10- 23:25
import pandas as pd
import requests
from bs4 import BeautifulSoup

while True:
    city = input('请输入城市(beijing,shanghai,guangzhou,shenzhen)：')
    city = city.lower()
    if city not in ['beijing', 'shanghai', 'guangzhou', 'shenzhen']:
        print('请输入正确的城市名称')
        continue
    url = f'https://www.air-level.com/air/{city}/'
    if city == 'q' or city == 'quit':
        break
    else:
        print(f'正在爬取{city}的空气质量数据...')  
    break 

# response = requests.get(url.format(city='beijing'))
response = requests.get(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table',{'class':'table text-center'})
print(tables)

rows = tables[0].find_all('tr')

# 提取表头 - 查找th或第一行td
headers = []
header_row = rows[0]
# 先尝试找th标签
header_cells = header_row.find_all('th')
if not header_cells:
    # 如果没有th，使用td
    header_cells = header_row.find_all('td')

for cell in header_cells:
    headers.append(cell.text.strip())

# 调试信息
print(f"表头数量: {len(headers)}")
print(f"表头内容: {headers}")

# 提取数据行
data = []
for row in rows[1:]:  # 跳过表头行
    cols = row.find_all('td')
    if len(cols) > 0:  # 只处理有数据的行
        row_data = []
        for col in cols:
            row_data.append(col.text.strip())
        data.append(row_data)
        # 调试：打印第一行数据的列数
        if len(data) == 1:
            print(f"第一行数据列数: {len(row_data)}")

print(data) 

df = pd.DataFrame(data, columns=headers)

df.to_csv(f'air_level_{city}.csv'.format(city=city), index=False)