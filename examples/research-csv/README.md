# 科研 Python 排错小示例

适用：会运行 Python、刚开始处理 CSV 的研究生。内容只有一个案例，不涉及论文代写、实际科研数据或模型接口。

## 使用

1. 将压缩包完整解压，保持所有文件在同一目录。
2. 使用 Python 3.9 或更高版本。在自己的虚拟环境安装：`python -m pip install -r requirements.txt`。
3. 用 Jupyter 打开 `csv-debug.ipynb`，选择该环境内核，依次运行全部单元格。Notebook 的工作目录应为本文件所在目录。
4. 不使用 Notebook 时，在此目录运行 `python run_demo.py`。输出 result.png、summary.csv、excluded.csv；重跑会覆盖这三个输出，不修改 example.csv。

## 先看结果

8 行输入，6 行纳入，2 行缺测排除。control：n=3，均值11；treatment：n=3，均值16。图中展示全部有效观测值和均值，不作显著性推断。

## 常见问题

- 找不到 example.csv：切换到解压后的目录再运行。
- 缺少 pandas / matplotlib：在当前 Notebook 使用的环境中安装依赖。
- 图中文字为英文：为避免中文字体依赖；中文说明在 Notebook 中。
- 出现未知组名、重复样本号或意外文本：先核对数据，不用自动填补绕过错误。

作者：刘能 / LiuNengAI（https://liunenglabs.xyz/）。本站独立运营，提供 AI 订阅相关商业服务，非 OpenAI 官方。本练习免费使用，不要求购买；材料在本地运行，无统计代码，不会调用模型或上传数据。环境安装需要联网下载依赖。

授权：本包代码、说明和自制数据以 MIT License 提供。
