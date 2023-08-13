from typing import List

import requests


def create_post_url_from_dict(vk_url: dict) -> List[str]:
    posts = []

    for item in vk_url:
        posts.append(f"https://vk.com/wall{item[3:]}")
    return posts


def create_wall_url(vk_community_id: int, offset: int) -> str:
    return f"https://vk.com/wall-{vk_community_id}?offset={offset}"


def get_html_from_url(vk_url: str) -> str:
    req = requests.get(vk_url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 YaBrowser/23.7.1.1140 Yowser/2.5 Safari/537.36"
    })
    return req.text
