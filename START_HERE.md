# 从零上手：上传 GitHub + 用 Copilot Student 继续做

## 你已经有什么？

仓库已经包含 `README.md`、第一期精读、时间戳证据索引、审校记录、静态网页、审查脚本以及 Copilot Prompt 文件。

## A. 在 Windows 打开项目

1. 将仓库完整下载并解压到例如 `D:\Projects\podcast-digest-cn`（不要只上传 ZIP 文件）。
2. 双击解压目录中的 `index.html`，先看文章页面。
3. 打开 **VS Code** → `File` → `Open Folder...` → 选择 `podcast-digest-cn` 这一层文件夹。
4. 安装 GitHub 官方的 **GitHub Copilot** 扩展并登录已经激活 Student 的 GitHub 账号。
5. 打开 Copilot Chat，粘贴根目录 `COPILOT_PROMPT.txt` 的全部内容。
6. 先让它审计，不要让它在第一步擅自重写访谈原文。

> 如果你使用截图中的 **GitHub Copilot 桌面 App**：点 Sessions 旁的 `+`，选择 **Open local folder**，选本项目目录；先用 **Plan**，权限用需要确认的模式。底部若显示 `No models available`，先处理账户权益/登录问题；也可以改用 VS Code Copilot Chat。

## B. 使用 Copilot Student 前的检查

1. 打开 https://github.com/settings/education/benefits ，确认学生权益与 Copilot Student 已激活（学生认证批准后还可能需要单独激活 Copilot）。
2. 打开 https://github.com/settings/copilot 看账户设置。
3. 在 VS Code 退出再登录正确 GitHub 账号，并确认 GitHub Copilot 扩展处于启用状态。
4. Student 的模型是自动选择，不必手工购买模型，也不应随便填写 API Key。使用额度可能有限。
5. 如果 App 仍显示无模型，而 VS Code Copilot Chat 能正常用，先用 VS Code 做项目即可。

## C. 最容易的方法：直接上传到 GitHub（不用命令）

1. GitHub 登录后，右上角 `+` → `New repository`。
2. Repository name 建议 `podcast-digest-cn`，Description 可写：`Source-grounded Chinese podcast digests. Read less, understand more.`
3. 选择 **Public**（想暂时审查，可先选 Private 后来再公开）。**不要勾选**初始化 README、.gitignore 或 license，因为包里已经有。
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
