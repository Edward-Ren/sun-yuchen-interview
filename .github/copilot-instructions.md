本项目是面向公众的中文长播客精读/摘要发布仓库。请先阅读仓库根目录的 `AGENTS.md`、`README.md` 和 `episodes/001-sun-alan/审校说明.md`。

最高优先级：不编造访谈发言和时间戳，不把二手转录当成听音核实的原话，不将人物主张当作事实，不擅自改动内容核验状态。优先做可读性、样式、来源链接、结构化质量检查。任何新增观点都必须指出证据来源并待人工审阅。

技术栈保持最小化：Python + 静态 HTML/CSS；无需 React、Next.js、数据库、登录、API Key、Agent 框架。第一期内容由 Markdown 生成网页。修改 Markdown 后运行 `python scripts/build_site.py`，并运行 `python -m unittest discover -s tests -v`。
