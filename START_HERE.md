# 从零上手：阅读项目与可选开发工具

## 你已经有什么？

仓库已经包含 `README.md`、第一期精读、时间戳证据索引、审校记录、静态网页、审查脚本以及 Copilot Prompt 文件。

## A. 在 Windows 打开项目

1. 将仓库完整下载并解压到例如 `D:\Projects\podcast-digest-cn`（不要只上传 ZIP 文件）。
2. 双击解压目录中的 `index.html`，先看文章页面。
3. 打开 **VS Code** → `File` → `Open Folder...` → 选择 `podcast-digest-cn` 这一层文件夹。
4. 可选：安装并登录 GitHub 官方的 **GitHub Copilot** 扩展；Copilot Free 即可用于继续维护，本项目不要求付费计划。
5. 打开 Copilot Chat，粘贴根目录 `COPILOT_PROMPT.txt` 的全部内容。
6. 先让它审计，不要让它在第一步擅自重写访谈原文。

> 如果你使用截图中的 **GitHub Copilot 桌面 App**：点 Sessions 旁的 `+`，选择 **Open local folder**，选本项目目录；先用 **Plan**，权限用需要确认的模式。底部若显示 `No models available`，先处理账户权益/登录问题；也可以改用 VS Code Copilot Chat。

## B. 可选：使用 Copilot Free

1. 如需 AI 辅助，在 VS Code 或 Copilot 桌面 App 登录自己的 GitHub 账号，并确认 Copilot Free 可用。
2. 使用免费计划时，功能和额度以账户当前显示为准；本项目不需要 API Key，也不依赖 Copilot 才能阅读或构建网页。
3. 如果某个客户端暂时无法使用 Copilot，仍可直接打开 `index.html` 阅读，或按下文运行项目检查。

## C. 最容易的方法：直接上传到 GitHub（不用命令）

1. GitHub 登录后，右上角 `+` → `New repository`。
2. Repository name 建议 `podcast-digest-cn`，Description 可写：`Source-grounded Chinese podcast digests. Read less, understand more.`
3. 按分享需要选择 **Public** 或 **Private**。**不要勾选**初始化 README、.gitignore 或 license，因为项目里已经有。
4. 创建后在仓库页面选 `uploading an existing file` / `Add file → Upload files`。
5. 把**解压后文件夹里的全部内容**上传（不是把 ZIP 本身上传）。Web 上传可能不方便保留隐藏的 `.github/` 文件夹，推荐使用下面的 Git 方法以确保全量上传。
6. Commit changes。核查网页能看到 README 和 `episodes/001-sun-alan`。

## D. 更稳妥：用 VS Code 终端推送全部文件

在 GitHub 新建**空仓库**后，在 VS Code 的 Terminal → New Terminal 中逐行运行：

```powershell
git init
git branch -M main
git add .
git commit -m "Initial podcast digest and reading site"
git remote add origin https://github.com/YOUR_USERNAME/podcast-digest-cn.git
git push -u origin main
```

把 `YOUR_USERNAME` 替换成**自己的 GitHub 用户名**，不带尖括号。首次推送可能需要浏览器登录或 Git Credential Manager 授权。如果 `git commit` 提示作者身份缺失，请按 Git 提示配置姓名和邮箱。

## E. 开启 GitHub Pages

仓库 → **Settings** → **Pages** → **Build and deployment** → `Deploy from a branch` → Branch 选 `main`、文件夹选 `/(root)` → Save。

等待 GitHub 显示部署后的网址，然后打开并检查文章排版、证据链接以及手机阅读效果。

## F. 发布前必须人工确认

- [ ] 点开 12 个重点时间戳并复听对应音频，确认 speaker、转录和语境。
- [ ] 检查文章是否把嘉宾主张误写成事实。
- [ ] 检查社交媒体标题没有使用虚假的引号或“他亲口说”但无听校的措辞。
- [ ] 运行 `python -m unittest discover -s tests -v`（此检查**不能**代替听音核对）。
- [ ] 更新 `episodes/001-sun-alan/审校说明.md` 中实际完成的复听记录。

## G. 为什么不直接生成多 Agent 系统？

你现在要做的是**一篇值得传播的高质量文章**。只有在积累第二、第三篇之后，才有足够素材沉淀一致的自动化编辑流程。不要为技术栈牺牲准确性。
