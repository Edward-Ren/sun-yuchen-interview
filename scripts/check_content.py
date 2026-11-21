"""Lightweight *structural* checks; no claim of audio or semantic verification."""
from pathlib import Path
import re
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / 'episodes/001-sun-alan/精华精读.md'
INDEX = ROOT / 'episodes/001-sun-alan/证据索引.md'
VIDEO_ID = '0Z-vhBvBmUY'
MAX_SECONDS = 4 * 3600 + 23 * 60   # allow rough duration of ~4h22m


def sections():
    text = ARTICLE.read_text(encoding='utf-8')
    result = re.findall(r'^###\s+(\d{2})｜(.+?)\s*$', text, re.M)
    return result


def evidence_rows():
    result = []
    for line in INDEX.read_text(encoding='utf-8').splitlines():
        match = re.match(r'^\|\s*(\d{2})\s*\|\s*([^|]+)\|\s*\[([^\]]+)\]\((https?://[^)]+)\)\s*\|', line)
        if match:
            result.append({'id': match.group(1), 'subject': match.group(2).strip(),
                           'time': match.group(3), 'url': match.group(4)})
    return result


def time_to_seconds(hms):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})', hms)
    if not match:
        raise ValueError(f'Invalid time format: {hms}')
    h, m, s = map(int, match.groups())
    if m >= 60 or s >= 60:
        raise ValueError(f'Invalid minute/second: {hms}')
    return h*3600 + m*60 + s


def validate():
    errs = []
    article = ARTICLE.read_text(encoding='utf-8')
    secs = sections(); rows = evidence_rows()
    expected = [f'{i:02d}' for i in range(1, 13)]
    if [x[0] for x in secs] != expected:
        errs.append('文章主题编号必须是 01...12，顺序不可重复')
    if [x['id'] for x in rows] != expected:
        errs.append('证据索引编号必须是 01...12，顺序不可重复')
    row_ids = {row['id'] for row in rows}
    article_ids = {section_id for section_id, _ in secs}
    missing_article_ids = sorted(row_ids - article_ids)
    missing_evidence_ids = sorted(article_ids - row_ids)
    if missing_article_ids:
        errs.append('证据索引存在但正文缺少主题：' + ', '.join(missing_article_ids))
    if missing_evidence_ids:
        errs.append('正文存在但证据索引缺少主题：' + ', '.join(missing_evidence_ids))
    for row in rows:
        try:
            seconds = time_to_seconds(row['time'])
            if seconds >= MAX_SECONDS:
                errs.append(f"{row['id']} 时间超出约 4h22m：{row['time']}")
            parsed = urlparse(row['url']); q = parse_qs(parsed.query)
            if parsed.netloc not in {'www.youtube.com','youtube.com'} or q.get('v') != [VIDEO_ID] or q.get('t') != [f'{seconds}s']:
                errs.append(f"{row['id']} 视频链接与时间戳不一致")
            if f't={seconds}s' not in article:
                errs.append(f"{row['id']} 正文中找不到对应视频时间戳 {seconds}")
        except ValueError as exc:
            errs.append(f"{row['id']}: {exc}")
    for file in [ROOT/'README.md', ARTICLE, INDEX, ROOT/'START_HERE.md']:
        # Checks only local Markdown links; not external network links.
        for dest in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', file.read_text(encoding='utf-8')):
            if dest.startswith(('http:', 'https:', '#', 'mailto:')):
                continue
            base = dest.split('#',1)[0]
            if base and not (file.parent/base).exists():
                errs.append(f'{file.relative_to(ROOT)} → missing {dest}')
    return errs


if __name__ == '__main__':
    errors = validate()
    if errors:
        print('\n'.join('FAIL: '+x for x in errors))
        raise SystemExit(1)
    print('PASS: 12 section/evidence rows, timestamp format, source video IDs, local links.')
    print('WARNING: This checks structure ONLY. It does NOT verify spoken accuracy or factual claims.')
