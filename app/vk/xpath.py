from typing import List

from lxml import html


def get_post_id(doc_html: str) -> List[str]:
    tree = html.fromstring(doc_html)
    urls = tree.xpath("//*[@class='wall_text']/div/@id")
    return urls


def get_text_from_post(doc_html: str) -> tuple[str, str]:
    post_html = html.fromstring(doc_html)
    inner_text = post_html.xpath("//*[@class='wall_post_text']/text()")
    mb_author = post_html.xpath("//*[@class='wall_post_text']/a/text()")
    return ''.join(inner_text), ''.join(mb_author)


def get_post_author(doc_html: str) -> str:
    post_html = html.fromstring(doc_html)
    inner_text = post_html.xpath("//span[@class='PostHeaderTitle__authorName']/text()")
    return ''.join(inner_text)
