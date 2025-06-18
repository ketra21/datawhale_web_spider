import pandas as pd 
# print(url.decode('utf-8'))
# from urllib.parse import unquote
# url_zh = unquote(url)
# print(url_zh)

import requests
from bs4 import BeautifulSoup
def parse_stock_table(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    tables = soup.find_all('table',{'class':'list_table'})
    if not tables:
        print("未找到数据表格")
        return [], []
        
    # 获取表格中的所有行
    rows = tables[0].find_all('tr')
    if not rows:
        print("表格中没有数据行")
        return [], []

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
        
    return headers, data

# 定义基础URL模板
base_url = 'https://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml?symbol=%D6%A4%C8%AF%BC%F2%B3%C6%BB%F2%B4%FA%C2%EB&reportdate={date}&quarter={q}&p={p}'

# 初始化一个空的DataFrame来存储所有数据
all_df = pd.DataFrame()

# 从第1页开始遍历
page = 1
while True:
    if page >6:
        break
    url = base_url.format(date=2024,q=1,p=page)
    headers, data = parse_stock_table(url)

    # 检查数据有效性
    if not headers or not data:
        print(f"第{page}页没有获取到有效数据，停止遍历")
        break
        
    print(f"第{page}页获取到 {len(data)} 行数据")
    
    # 确保列数匹配
    if data and len(headers) != len(data[0]):
        print(f"警告：列数不匹配！表头{len(headers)}列，数据{len(data[0])}列")
        # 如果数据列数更多，截断表头或使用默认列名
        if len(data[0]) > len(headers):
            for i in range(len(headers), len(data[0])):
                headers.append(f'列{i+1}')
    
    # 创建DataFrame
    df = pd.DataFrame(data, columns=headers)
    
    # 尝试删除证券代码为空的记录（如果该列存在）
    if '证券代码' in df.columns:
        df = df[df['证券代码'].str.strip() != '']
    
    # 将当前页数据添加到总DataFrame中
    all_df = pd.concat([all_df, df], ignore_index=True)
    
    print(f"当前已获取总数据量: {len(all_df)}")
    
    # 继续下一页
    page += 1

print("\n最终数据框内容:")
print(all_df.head())
print(f"\n最终数据框形状: {all_df.shape}")
print(f"列名: {list(all_df.columns)}")

# 保存数据到CSV文件
output_file = 'stock_data.csv'
all_df.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"\n数据已保存到文件: {output_file}")





