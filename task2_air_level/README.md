# Task2 - 空气质量数据爬虫

## 项目概述
爬取air-level.com网站的城市空气质量数据，支持北京、上海、广州、深圳四个城市的数据获取。

## 功能特性
- 交互式城市选择（beijing、shanghai、guangzhou、shenzhen）
- 自动爬取指定城市的空气质量历史数据
- 使用BeautifulSoup解析HTML表格数据
- 自动处理表头和数据提取
- 数据自动保存为CSV格式
- 包含用户输入验证和错误提示

## 技术栈
- **Python 3.x** - 主要编程语言
- **requests** - HTTP请求库
- **BeautifulSoup4** - HTML解析库
- **pandas** - 数据处理和CSV导出
- **User-Agent伪装** - 模拟浏览器访问

## 依赖安装
```bash
pip install requests beautifulsoup4 pandas
```

## 使用方法

### 基本使用
1. 运行程序：
```bash
python main.py
```

2. 根据提示输入城市名称：
   - beijing（北京）
   - shanghai（上海）
   - guangzhou（广州）
   - shenzhen（深圳）

3. 程序会自动：
   - 发送HTTP请求获取数据
   - 解析HTML表格
   - 提取表头和数据行
   - 保存为 `air_level_{城市名}.csv` 文件

### 输出文件
- `air_level_beijing.csv` - 北京空气质量数据
- `air_level_shenzhen.csv` - 深圳空气质量数据
- 其他城市对应的CSV文件

## 数据字段说明
根据网站表格结构，包含以下字段：
- 日期时间
- AQI指数
- 空气质量等级
- PM2.5浓度
- PM10浓度
- 其他空气质量指标

## 代码结构
```
task2_air_level/
├── main.py              # 主程序文件
├── README.md            # 项目说明文档
├── air_level_*.csv      # 输出的数据文件
└── .gitignore          # Git忽略文件配置
```

## 注意事项
1. **网络连接**：需要稳定的网络连接访问air-level.com
2. **User-Agent**：程序使用Chrome浏览器User-Agent避免反爬
3. **输入验证**：只支持指定的四个城市名称
4. **文件覆盖**：重复运行会覆盖同名CSV文件

## 开发说明
- 程序使用UTF-8编码处理中文内容
- 包含调试信息输出，便于问题排查
- 采用表格解析方式提取结构化数据
- 支持动态URL构建适配不同城市

## 改进建议
- [ ] 添加更多城市支持
- [ ] 增加数据可视化功能
- [ ] 添加定时爬取功能
- [ ] 支持数据去重和增量更新
- [ ] 添加异常处理和重试机制 