"""Python-Markdown extension: `[@ 漢字 かな]` -> <ruby>漢字<rt>かな</rt></ruby>.

Port of the mkdocs-ja-ruby plugin, so the syntax works under Zensical
(which does not run MkDocs plugins).
"""
import re

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

RUBY = re.compile(r"\[@ ([^\]]+) ([^\]]+)\]")
HTML = r"<ruby>\1<rp>(</rp><rt>\2</rt><rp>)</rp></ruby>"


class RubyPreprocessor(Preprocessor):
    def run(self, lines):
        return RUBY.sub(HTML, "\n".join(lines)).split("\n")


class JaRubyExtension(Extension):
    def extendMarkdown(self, md):
        # before Python-Markdown's own preprocessors, same as the MkDocs plugin hook
        md.preprocessors.register(RubyPreprocessor(md), "ja_ruby", 100)


def makeExtension(**kwargs):
    return JaRubyExtension(**kwargs)
