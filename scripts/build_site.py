# Generate a static, source-grounded reading page from the reviewed Markdown.
# Requires mistune; commit generated index.html for no-build GitHub Pages.
from pathlib import Path
from html import escape
from urllib.parse import quote
import hashlib
import re
import mistune

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT/'episodes/001-sun-alan/精华精读.md'
SOURCE = ARTICLE.read_text(encoding='utf-8')
SOURCE_HASH = hashlib.sha256(SOURCE.encode('utf-8')).hexdigest()

class EditorialRenderer(mistune.HTMLRenderer):
    def __init__(self):
        super().__init__(escape=True)
        self.h2_idx = 0
        self.h3_idx = 0
    def heading(self, text, level, **attrs):
        if level == 1:
            return ''  # hero supplies the title
        if level == 2:
            self.h2_idx += 1
            ident = f'part-{self.h2_idx}'
        elif level == 3:
            self.h3_idx += 1
            ident = f'topic-{self.h3_idx:02d}'
        else:
            ident = f'heading-{self.h2_idx}-{self.h3_idx}-{level}'
        return f'<h{level} id="{ident}">{text}</h{level}>\n'

md = mistune.create_markdown(renderer=EditorialRenderer(), plugins=['table', 'strikethrough'])
content = md(SOURCE)
def add_keyboard_scroll_regions(markup):
    return re.sub(
        r'<table>(.*?)</table>',
        r'<div class="table-scroll" role="region" aria-label="可横向滚动的表格" tabindex="0"><table>\1</table></div>',
        markup,
        flags=re.S,
    )

content = add_keyboard_scroll_regions(content)
# In the source, links to evidence/review are adjacent to article, so rewrite just these
# two Markdown link destinations for the site, where index.html resides at repo root.
for target, out in [('证据索引.md', 'evidence.html'), ('审校说明.md', 'review.html')]:
    content = content.replace(f'href="./{quote(target)}"', f'href="./{out}"')
    content = content.replace(f'href="./{target}"', f'href="./{out}"')

parts = re.findall(r'^## (.+)$', SOURCE, re.M)
# First five '第...部分' are main reading sections.
main_parts = [p for p in parts if p.startswith(('第一部分','第二部分','第三部分','第四部分','第五部分'))]
# Article has 1 intro H2 before the five parts, so IDs run part-2...part-6.
nav = '\n'.join(f'<a href="#part-{i+2}"><span>{i+1:02d}</span>{escape(p.split("：",1)[-1])}</a>' for i,p in enumerate(main_parts))

html = f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f7f5f0">
  <meta name="description" content="孙宇晨、邵艾伦访谈精读：围绕 AI、财富自由、商业机会与人生选择，精选12个核心讨论并保留原片时间戳。">
  <meta name="keywords" content="孙宇晨,邵艾伦,访谈精读,财富自由,AI,人生选择">
  <meta property="og:title" content="孙宇晨、邵艾伦访谈精读｜AI、财富自由与人生选择">
  <meta property="og:description" content="4小时22分钟访谈精读，精选12个核心讨论，保留真实案例和原片时间戳。">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="zh_CN">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="孙宇晨、邵艾伦访谈精读｜AI、财富自由与人生选择">
  <meta name="twitter:description" content="4小时22分钟访谈精读，精选12个核心讨论，保留真实案例和原片时间戳。">
  <title>播客精读｜中文长访谈精读</title>
  <link rel="stylesheet" href="./assets/style.css">
</head>
<body>
<!-- source-sha256:{SOURCE_HASH} -->
<a class="skip" href="#reading">跳转到正文</a>
<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="#top" aria-label="播客精读首页"><span class="brandmark">·</span> 播客精读</a>
    <nav class="topnav" aria-label="页面导航">
      <a href="#reading">阅读正文</a>
      <a href="./evidence.html">证据索引</a>
      <a class="toplink" href="https://www.youtube.com/watch?v=0Z-vhBvBmUY" target="_blank" rel="noopener noreferrer">原视频 ↗</a>
    </nav>
  </div>
</header>
<main id="top">
  <section class="hero">
    <div class="hero-text">
      <p class="eyebrow">播客精读 · 第一期</p>
      <h1>孙宇晨 × 邵艾伦：<br><em>4 小时访谈里，值得读的 12 个讨论</em></h1>
      <p class="intro">从 AI 时代的机会与决策，到财富、自由、创造与人生选择，精读本期 12 个核心讨论。</p>
      <div class="meta"><span>4 小时 22 分</span><span>12 个讨论</span><span>5 条阅读主线</span></div>
    </div>
    <aside class="hero-note" aria-label="本期阅读重点">
      <p class="note-kicker">先听三段</p>
      <a href="https://www.youtube.com/watch?v=0Z-vhBvBmUY&t=2406s" target="_blank" rel="noopener noreferrer"><time>00:40:06</time><span>决定之前，把地图打开 ↗</span></a>
      <a href="https://www.youtube.com/watch?v=0Z-vhBvBmUY&t=9807s" target="_blank" rel="noopener noreferrer"><time>02:43:27</time><span>自由与财富的关系 ↗</span></a>
      <a href="https://www.youtube.com/watch?v=0Z-vhBvBmUY&t=15147s" target="_blank" rel="noopener noreferrer"><time>04:12:27</time><span>创造与消费的平衡 ↗</span></a>
      <div class="note-foot">跳转时间是话题入口，不一定是每句话的精确起点。</div>
    </aside>
  </section>
  <div class="disclosure" role="note"><strong>核验状态</strong> · 本文基于公开转录对照整理，<strong>尚未完成逐段听原音校对</strong>。编辑标题不代表嘉宾逐字原话，涉及技术、健康和投资的观点也不代表已被独立证实。</div>
  <div class="reading-layout" id="reading">
    <aside class="sidebar">
      <div class="sticky">
        <p class="sidebar-title">阅读目录 / CONTENTS</p>
        <nav class="chapter-nav" aria-label="章节目录" tabindex="0">
          {nav}
        </nav>
        <div class="sidebar-extra"><a href="./evidence.html">证据索引 ↘</a></div>
      </div>
    </aside>
    <article class="prose" aria-label="播客精读正文">
      {content}
    </article>
  </div>
  <section id="sources" class="sources">
    <p class="eyebrow">来源与说明</p>
    <p>本文依据公开分章节转录整理，保留原片时间入口；尚未完成逐段原音听校，不构成投资、医疗或法律建议。</p>
    <div class="source-grid">
      <a href="https://www.youtube.com/watch?v=0Z-vhBvBmUY" target="_blank" rel="noopener noreferrer"><span>原始访谈</span><strong>邵艾伦 × 孙宇晨 ↗</strong></a>
      <a href="./evidence.html"><span>查证位置</span><strong>12 项证据索引 ↗</strong></a>
    </div>
  </section>
</main>
<footer><span>播客精读 · 第一期</span><span>听得长，读得清。</span></footer>
</body>
</html>
'''
(ROOT/'index.html').write_text(html, encoding='utf-8')
print('Built:', ROOT/'index.html')

# Render evidence and review to human-readable HTML pages, not raw .md URLs.
secondary_md = mistune.create_markdown(plugins=['table'])
for infile, outfile, page_title in [
    ('证据索引.md', 'evidence.html', '证据索引'),
    ('审校说明.md', 'review.html', '审校说明')
]:
    source_path = ROOT/'episodes/001-sun-alan'/infile
    raw = source_path.read_text(encoding='utf-8')
    source_hash = hashlib.sha256(raw.encode('utf-8')).hexdigest()
    rendered = add_keyboard_scroll_regions(secondary_md(raw))
    page = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{page_title} · 播客精读计划</title><link rel="stylesheet" href="./assets/style.css"></head>
<body><!-- source-sha256:{source_hash} --><header class="topbar"><div class="topbar-inner"><a class="brand" href="./index.html"><span class="brandmark">·</span> 播客精读计划</a><nav class="topnav"><a href="./index.html">← 返回精读</a><a class="toplink" href="https://www.youtube.com/watch?v=0Z-vhBvBmUY" target="_blank" rel="noopener noreferrer">原视频 ↗</a></nav></div></header>
<main class="appendix prose">{rendered}</main><footer><span>播客精读计划 · Episode 001</span><span>证据、限度和可更正的记录。</span></footer></body></html>'''
    (ROOT/outfile).write_text(page, encoding='utf-8')
    print('Built:', ROOT/outfile)
