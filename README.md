# LiuNengAI Bug Report Builder · 报错求助整理器

A free Chinese-language form that turns environment details, reproduction steps, errors and expected results into a Markdown bug report.

[Use the live tool](https://liunenglabs.xyz/guides/debug-report/) · [查看全部免费工具与指南](https://liunenglabs.xyz/guides/?utm_source=github)

## 下载与离线使用

[下载 v1.0.0 单文件版](https://github.com/a941249849/liunengai-debug-report/releases/tag/v1.0.0)：在 Assets 中选择 `debug-help-builder.html`，保存后用浏览器打开。无需安装或联网；导航链接需在线访问。发行页同时提供 SHA-256 校验文件、固定版本的代码和中英文使用说明。

[Download the offline release](https://github.com/a941249849/liunengai-debug-report/releases/tag/v1.0.0). Save the HTML asset and open it in a browser. The interface is Chinese.

## 使用

1. 打开 `index.html`，或直接访问在线工具。
2. 填写目标、运行环境、最小代码、复现步骤、实际结果、预期结果和已尝试的方法。也可先用内置演示了解格式。
3. 核对生成的 Markdown，复制或下载，再发给同学、助教、项目维护者或自己选择的 AI。
4. 从网页保存单个 HTML 文件后，可以离线使用。

## Privacy and scope

- No account, backend or dependencies required for the tool.
- Report inputs are processed locally in your browser; this tool page contains no analytics script.
- No AI calls, automatic diagnosis or code execution. It formats the information you provide.
- Do not include passwords, Session tokens, verification codes, real customer information or unredacted private logs in a report you share.
- Navigation links lead to external pages when clicked; those pages may have different policies.

## Self-host

Serve `index.html` from any static host, or open it directly in a browser. All application HTML, CSS and JavaScript are in that file.

## 准备把报告交给 AI 时

本工具只整理问题，不提供 AI 模型、订阅或 API 额度。你可以把核对后的报告交给同学、维护者，或自己选择的 AI；使用本工具不需要购买任何服务。

- [ChatGPT 订阅与 API 有什么区别？](https://liunenglabs.xyz/guides/chatgpt-subscription-vs-api/?utm_source=github)：先分清在聊天界面使用，还是在程序中调用，避免买错服务。
- [Codex 提示验证电话号码怎么办？](https://liunenglabs.xyz/guides/codex-phone-verification/?utm_source=github)：区分短信验证、MFA 和订阅额度；一次接码不提供会员或 API 余额，也不保证通过验证。

以上是 LiuNengAI 运营方整理的说明，相关页面会介绍本站另行收费的服务，非 OpenAI 官方说明。不要向他人发送账号密码、验证码或登录 Session。

## 可运行案例：CSV 报错与结果核验

想练习怎样把问题说清楚，可以从 [research-csv 示例](examples/research-csv/) 开始：用自制数据复现缺测标记报错，运行完整修复，并核对排除记录、样本数和均值。附 Python 脚本、Notebook 和向 AI 描述最小复现问题的模板；无需 AI 账号或购买。安装 Python 依赖需联网；该案例的依赖与运行要求独立于上方免安装的 HTML 工具。

[无需登录预览及下载完整包](https://liunenglabs.xyz/guides/research-csv-debug/)。这是一般数据清理练习，不代替真实研究的分析方案或统计推断。

## License and operator

MIT © 2026 LiuNeng AI. See [LICENSE](LICENSE).

This is published by 刘能AI / LiuNengAI. Our website also operates a separate paid service for ChatGPT subscription recharge on customers' own accounts. We are an independent operator, not OpenAI's official website. The free tool does not require a purchase; this repository is not an official OpenAI project.
