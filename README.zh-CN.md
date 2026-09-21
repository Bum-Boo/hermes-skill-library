# Hermes Skill Library

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | **中文**

这是面向 Hermes Agent 类助手的精选可复用技能库。它不是单一用途的软件包；您可以安装整个库，也可以只安装一个按用途划分的集合。

## 技能集合

| 集合 | 用途 |
|---|---|
| [`gstack-safe`](collections/gstack-safe/) | 证据优先的规范、审查与调查 |
| [`agent-engineering`](collections/agent-engineering/) | 向编码代理 CLI 委派有明确范围的任务 |
| [`research-workflows`](collections/research-workflows/) | 来源收集、监控、ML 实验与评估证据 |
| [`comfyui-image-workflows`](collections/comfyui-image-workflows/) | ComfyUI 生成、批处理、验证与故障排除 |
| [`wsl-operator`](collections/wsl-operator/) | Windows/WSL 路径与 GUI 启动器 |
| [`oauth-browser-handoff`](collections/oauth-browser-handoff/) | 在无头、WSL 或远程环境中由用户完成 OAuth 浏览器流程 |
| [`profile-context-diet`](collections/profile-context-diet/) | 清理陈旧或过量的 Hermes 配置文件上下文 |
| [`hermes-profile-operations`](collections/hermes-profile-operations/) | 多配置文件设置、存储与上下文维护 |
| [`local-development-safety`](collections/local-development-safety/) | 范围明确的本地变更与最新完成证据 |
| [`github-publishing`](collections/github-publishing/) | 面向 WSL 的发布与远程状态验证 |
| [`telegram-operator`](collections/telegram-operator/) | 简洁、真实的 Telegram 进度与结果报告 |
| [`computer-use-safety`](collections/computer-use-safety/) | 后台优先的桌面控制与安全升级路径 |
| [`web-interface-verification`](collections/web-interface-verification/) | 响应式、触控、悬停与平板宽度验证 |
| [`repository-maintenance`](collections/repository-maintenance/) | 审计分叉、镜像、供应商快照与下游代码库 |
| [`artifact-recovery`](collections/artifact-recovery/) | 基于证据恢复并安全交付难以辨认的既有本地文件 |

各集合页面列出了所含技能和使用说明，机器可读清单位于 [`catalog.json`](catalog.json)。

## 安装全部技能

```bash
git clone https://github.com/Bum-Boo/hermes-skill-library.git
cd hermes-skill-library
./scripts/install.sh
hermes skills list
```

```bash
# Install for one profile
./scripts/install.sh ~/.hermes/profiles/<profile>/skills
hermes --profile <profile> skills list
```

默认目标为 `~/.hermes/skills`。如果 Hermes CLI 的 `skills list` 不支持 `--profile`，请使用该配置文件开始对话，并要求助手列出或加载已安装技能。

> 安装程序会把库复制到目标位置，并可能替换同路径文件。运行前请审查源码并确认目标正确。

## 只安装一个集合

```bash
./scripts/install-collection.sh <collection-name>
./scripts/install-collection.sh comfyui-image-workflows ~/.hermes/profiles/<profile>/skills
```

请使用上表中的集合名。[`scripts/install-collection.sh`](scripts/install-collection.sh) 未实现的名称会以错误退出。

## 仓库结构

```text
skills/<category>/<skill-name>/SKILL.md  可安装技能
collections/<collection>/README.md      按用途编写的集合说明
scripts/install.sh                      安装全部技能
scripts/install-collection.sh           安装一个集合
catalog.json                            集合清单
SECURITY.md                             安全政策
LICENSE                                 MIT 许可证
```

## 安全贡献

请将带有有效 Hermes frontmatter 的技能放在 `skills/<category>/<skill-name>/SKILL.md`，并更新集合文档和 `catalog.json`。分享变更前，请在临时目录测试安装，并检查是否包含凭据、私人路径、账户标识、浏览器配置文件或客户数据。切勿提交真实秘密值。请参阅 [`SECURITY.md`](SECURITY.md)。

## 署名请求

如果您分享本技能库或发布衍生作品，烦请在方便时提及 **@Bum-Boo** 和[原始仓库](https://github.com/Bum-Boo/hermes-skill-library)。这是致谢请求，并非附加或修改许可证条件。

## 许可证

MIT。请参阅 [`LICENSE`](LICENSE)。
