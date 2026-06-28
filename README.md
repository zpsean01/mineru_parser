# mineru_parser

基于 [MinerU 精准解析 API](https://mineru.net/apiManage/docs) 的 PDF 文档解析工具，支持通过 URL 解析单个文件以及批量上传本地文件解析。

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 Token

编辑 `.env` 文件，填入在 [MinerU API 管理](https://mineru.net/apiManage) 创建的 Token：

```
MINERU_TOKEN=你的Token
```

### 3. 使用

**解析单个远程文件：**

```bash
python main.py single https://cdn-mineru.openxlab.org.cn/demo/example.pdf
```

**批量上传本地文件：**

```bash
python main.py batch report1.pdf report2.pdf
```

### 常用选项

| 参数 | 说明 |
|------|------|
| `--model-version` | 模型版本：`pipeline` / `vlm`(默认) / `MinerU-HTML` |
| `--language` | 文档语言：`ch` / `en` / `auto` |
| `--output-dir` | 结果保存目录（默认 `./output`） |
| `--no-extract` | 不自动解压结果 ZIP |
| `--poll-interval` | 轮询间隔秒数（默认 5） |
| `--poll-timeout` | 轮询超时秒数（默认 1800） |

```bash
# 示例：指定模型与语言
python main.py single https://example.com/doc.pdf --model-version pipeline --language en

# 示例：自定义输出目录
python main.py single https://example.com/doc.pdf --output-dir ./my_results --no-extract
```

## 项目结构

```
mineru_parser/
├── main.py                # CLI 入口
├── .env                   # 配置文件
├── requirements.txt       # 依赖
└── modules/
    ├── api_client.py      # API 客户端基类
    ├── config.py          # 配置管理
    ├── single_parser.py   # 单文件 URL 解析
    ├── batch_parser.py    # 批量上传解析
    └── utils.py           # 下载/解压等工具
```

## 说明

- 单 URL 解析：提交任务 → 轮询结果 → 下载 ZIP → 自动解压，返回 Markdown 等解析结果
- 批量上传：申请上传链接 → 上传文件 → 系统自动提交解析任务
- 单个文件不超过 200MB / 200 页，批量单次不超过 50 个文件
- 更多 API 详情见 [官方文档](https://mineru.net/apiManage/docs)
