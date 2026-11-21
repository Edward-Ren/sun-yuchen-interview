import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from check_content import validate, sections, evidence_rows, time_to_seconds

class ContentTests(unittest.TestCase):
    def test_structure(self):
        self.assertEqual(validate(), [])

    def test_all_twelve_items(self):
        self.assertEqual(len(sections()), 12)
        self.assertEqual(len(evidence_rows()), 12)

    def test_multiple_evidence_timestamps(self):
        row = next(item for item in evidence_rows() if item['id'] == '11')
        self.assertEqual([item['time'] for item in row['times']],
                         ['03:49:45', '03:50:25', '03:52:24'])

    def test_timestamps(self):
        self.assertEqual(time_to_seconds('04:12:27'), 15147)
        for bad in ['04:77:01', '00:02:99', '2:3:1']:
            with self.assertRaises(ValueError):
                time_to_seconds(bad)

    def test_generated_pages_exist(self):
        for page in ('index.html', 'evidence.html', 'review.html'):
            self.assertTrue((ROOT/page).is_file())
        html = (ROOT/'index.html').read_text(encoding='utf-8')
        import hashlib
        content = (ROOT/'episodes/001-sun-alan/精华精读.md').read_bytes()
        self.assertIn('source-sha256:'+hashlib.sha256(content).hexdigest(), html)
        for md_name, page_name in (
            ('证据索引.md', 'evidence.html'),
            ('审校说明.md', 'review.html'),
        ):
            source = (ROOT/'episodes/001-sun-alan'/md_name).read_bytes()
            generated = (ROOT/page_name).read_text(encoding='utf-8')
            self.assertIn('source-sha256:'+hashlib.sha256(source).hexdigest(), generated)
        self.assertIn('<nav class="chapter-nav" aria-label="章节目录" tabindex="0">', html)
        evidence = (ROOT/'evidence.html').read_text(encoding='utf-8')
        self.assertIn('class="table-scroll" role="region"', evidence)
        self.assertIn('tabindex="0"', evidence)
        self.assertIn('<title>播客精读｜中文长访谈精读</title>', html)
        self.assertIn('孙宇晨 × 邵艾伦：<br><em>4 小时访谈里，值得读的 12 个讨论</em>', html)

    def test_article_and_evidence_ids_match(self):
        article_ids = {x[0] for x in sections()}
        evidence_ids = {x['id'] for x in evidence_rows()}
        self.assertEqual(article_ids, evidence_ids)

    def test_source_and_review_present(self):
        self.assertTrue((ROOT/'episodes/001-sun-alan/审校说明.md').is_file())
        self.assertIn('未听校', (ROOT/'episodes/001-sun-alan/证据索引.md').read_text(encoding='utf-8'))

if __name__ == '__main__':
    unittest.main()
