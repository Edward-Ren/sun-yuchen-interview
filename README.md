# 播客精读计划 · Podcast Digest CN

> **听得长，读得清。** 用有依据的中文精读，重新整理值得花时间的长访谈。

[📖 在线阅读（部署 GitHub Pages 后）](#在线阅读) · [📄 本期完整精读](./episodes/001-sun-alan/精华精读.md) · [🧭 证据索引](./episodes/001-sun-alan/证据索引.md) · [🔎 审校记录](./episodes/001-sun-alan/审校说明.md)

## Episode 001 · 孙宇晨 × 邵艾伦

**4 小时 22 分的对话，真正值得思考的 12 个讨论。**

话题包括 AI、学习与机会、重大决策、财富与自由、创造与体验。不是拼凑“成功学金句”，而是保留**谁说的、在回答什么、举了什么例子，以及有什么边界**。

- 🎥 [原始访谈（YouTube）](https://www.youtube.com/watch?v=0Z-vhBvBmUY)
- 📖 [阅读完整文章](./episodes/001-sun-alan/精华精读.md)
- 🕒 [每一节的来源和时间戳](./episodes/001-sun-alan/证据索引.md)
- 📝 [哪些地方还没有音频听校？](./episodes/001-sun-alan/审校说明.md)

### 三段可以先回看

| 感兴趣的话题 | 回看片段 |
| --- | --- |
| 决策前先扩大选择范围 | [00:40:06](https://www.youtube.com/watch?v=0Z-vhBvBmUY&t=2406s) |
| 财富与自由是什么关系 | [02:43:27](https://www.youtube.com/watch?v=0Z-vhBvBmUY&t=9807s) |
| 创造与消费如何平衡 | [04:12:27](https://www.youtube.com/watch?v=0Z-vhBvBmUY&t=15147s) |

## 这份内容如何保证可信？

1. 所有重要观点均应有对应的原视频时间戳及转录章节。
2. **编辑标题不是嘉宾原话**；不以引号冒充没有听校的逐字引述。
3. 把「嘉宾的个人主张」和「已查证的外部事实」分开。
4. **目前是公开转录对照的发布候选稿，尚未逐段听原音核对**。欢迎就具体时间码纠错。

转录参考：[LeoLee0812 分章节转录](https://github.com/LeoLee0812/sunyuchen-alan-interview)；[AayuBal 辅助整理](https://github.com/AayuBal/shaoailun-sunyuchen-podcast)。原视频与转录的权益属于各自权利人；仓库未收录其完整音频或逐字稿。

## 在线阅读

本仓库根目录已经包含 `index.html` 和 `assets/style.css`，可直接双击 `index.html` 预览，无须安装网页框架。

GitHub Pages 发布方法：**Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save**。部署后链接一般是 `https://你的用户名.github.io/podcast-digest-cn/`（以 GitHub 实际显示为准）。

## 从零开始开发

- [打开 START_HERE.md](./START_HERE.md)：解压、VS Code、Copilot Student、上传 GitHub 的步骤。
- [COPILOT_PROMPT.txt](./COPILOT_PROMPT.txt)：可直接粘贴给 Copilot 的第一条任务。
- [`prompts/`](./prompts/)：内容审核、网站优化、质量检查、后续扩展的分阶段 Prompt。
- [AGENTS.md](./AGENTS.md)：任何代码 Agent 都应遵守的内容真实性红线。

### 本地运行和检查

```bash
# 只浏览网页，无需 Python 依赖，直接打开 index.html 即可
python -m unittest discover -s tests -v

# 改了精华精读.md，需重建静态页面：
python -m pip install -r requirements.txt
python scripts/build_site.py
```

## 路线

**现在：** 做好这一篇、核对证据、完善阅读体验。  
**之后：** 做第二篇、第三篇，确定稳定的编辑风格。  
**最后：** 才考虑转录自动化、批量整理、主题索引与多 Agent。

## 版权与贡献

- 代码：MIT，见 [LICENSE](./LICENSE)。
- 本仓库原创编辑文字：见 [CONTENT-LICENSE.md](./CONTENT-LICENSE.md)。原访谈视频、人物言论和第三方逐字稿不在本仓库许可范围内。
- [贡献指南](./CONTRIBUTING.md)：请提交带原视频时间戳的纠错，不要只提交“AI 说应该是这样”。

> 独立整理项目，不代表视频发布方、嘉宾或转录仓库作者；本文不构成投资、法律、医疗建议。
