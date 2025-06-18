# Datawhale网络爬虫课程项目

这是Datawhale网络爬虫课程的学习项目，包含多个实战任务，从基础爬虫到高级应用。

## 项目结构
```
learn_spider_202506/
├── task1_sina_stock_spider/    # 任务1：新浪股票数据爬虫
├── task2_air_level/           # 任务2：空气质量数据爬虫
└── README.md                  # 项目总说明
```

## Task1 - 新浪股票信息爬虫

### 功能特性
- 🚀 爬取新浪财经股票机构持股数据
- 📊 支持多页数据自动获取
- 🔧 智能处理表头和数据列对齐
- 💾 自动保存为CSV格式
- 🛡️ 完善的错误处理和调试信息
- 🧹 自动过滤无效数据记录

### 技术亮点
- BeautifulSoup4 HTML解析
- Pandas 数据处理和分析
- 中文编码处理（GBK）
- 动态分页爬取
- 数据验证和清洗

### 数据输出
- `stock_data.csv` - 包含股票代码、简称、机构数等信息
- 支持获取数百条机构持股记录

---

## Task2 - 空气质量数据爬虫

### 功能特性
- 🌍 支持4个主要城市空气质量数据爬取
- 💬 交互式城市选择界面
- 📋 自动解析HTML表格数据
- 📁 按城市分别保存CSV文件
- 🛡️ User-Agent伪装防反爬
- ✅ 输入验证和错误提示

### 支持城市
- 北京 (beijing)
- 上海 (shanghai) 
- 广州 (guangzhou)
- 深圳 (shenzhen)

### 数据字段
- 日期时间、AQI指数、空气质量等级
- PM2.5、PM10浓度等详细指标

---

## 环境要求

### Python版本
- Python 3.7+

### 依赖库
```bash
pip install requests beautifulsoup4 pandas
```

## 快速开始

### 运行Task1（股票爬虫）
```bash
cd task1_sina_stock_spider
python main.py
```

### 运行Task2（空气质量爬虫）
```bash
cd task2_air_level
python main.py
```

## 学习目标

通过这些项目，你将学到：
- 网络爬虫基本原理和实现
- HTML解析和数据提取技巧
- 反爬虫策略和应对方法
- 数据处理和存储最佳实践
- 错误处理和调试技巧
- 代码结构设计和可维护性

## 注意事项

⚠️ **使用声明**
- 本项目仅用于学习目的
- 请遵守网站robots.txt规则
- 注意控制爬取频率，避免对服务器造成压力
- 尊重网站版权和用户协议

## 贡献指南

欢迎提交Issue和Pull Request来改进项目！

## 许可证

MIT License
