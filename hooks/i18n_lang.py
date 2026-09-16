"""Set the static <html lang> attribute per page language.

Material derives <html lang> from the global theme language, which cannot differ
between the Chinese pages and the docs/en/ English pages in a single build.
This MkDocs hook (core feature, no plugin) rewrites the attribute at build time
so crawlers see a correct static lang attribute on both language trees.
"""

import re

_HTML_LANG = re.compile(r'(<html[^>]*?\blang=")[^"]*(")', re.I)


def on_post_page(output: str, page, config) -> str:
    try:
        url = (getattr(page, "url", "") or "")
    except Exception:
        return output
    if url.startswith("en/"):
        return _HTML_LANG.sub(r"\1en\2", output, count=1)
    return output
