# 网络爬虫学习项目

## 项目目标
这是一个学习Python网络爬虫的项目，主要用于获取和解析网页数据。

## 当前功能
- 爬取新浪财经股票机构持股数据
- 使用BeautifulSoup解析HTML内容
- 处理中文编码问题
- 将数据转换为pandas DataFrame格式
- 自动处理表头和数据列数不匹配的问题
- 过滤空的证券代码记录

## 依赖库
- requests: 用于发送HTTP请求
- beautifulsoup4: 用于解析HTML内容
- pandas: 用于数据处理和分析

## 安装依赖
```bash
pip install requests beautifulsoup4 pandas
```

## 使用方法
直接运行主程序：
```bash
python main.py
```

## 文件说明
- `main.py`: 主程序文件，包含爬虫逻辑

## 注意事项
- 网页编码使用GBK格式
- URL包含中文字符，已进行解码处理 