from openpyxl import Workbook

from app.vk import (
    create_post_url_from_dict,
    create_wall_url,
    get_html_from_url,
    get_post_id,
    get_text_from_post,
    get_phone_number,
    get_post_author
)

# ТОЛЬКО НОМЕРА ВК СООБЩЕСТВ
VK_COMMUNITY_IDS = [
    178644285,  # Недвижимость Кирова Сдам Сниму Продам Квартиры
    20638317,   # НЕДВИЖИМОСТЬ КВАРТИРЫ КИРОВ
    53252559,   # Недвижимость Киров | Продажа | Аренда
]
MAX_POST_COUNT = 10000
POST_STEP = 20
FILE_PATH = r"./data.xlsx"

wb = Workbook()

ws = wb.active

ws.title = "База номеров"

for community in VK_COMMUNITY_IDS:
    for step in range(0, MAX_POST_COUNT + POST_STEP, POST_STEP):
        c_url = create_wall_url(community, offset=step)
        c_html = get_html_from_url(c_url)
        c_urls = get_post_id(c_html)
        posts = create_post_url_from_dict(c_urls)

        for post_id in posts:
            post_html = get_html_from_url(post_id)
            text, from_post = get_text_from_post(post_html)
            author = get_post_author(post_html)
            phone_number = get_phone_number(post_html)
            if phone_number == "ПИЗДА" or not text:
                print("Пусто...")
            else:
                ws.append([
                    post_id,
                    phone_number,
                    author,
                    from_post,
                    text
                ])

# Просто чтобы мазни не было
ws.column_dimensions["A"].width = 36
ws.column_dimensions["B"].width = 13
ws.column_dimensions["C"].width = 51
ws.column_dimensions["D"].width = 51
ws.column_dimensions["E"].width = 200

wb.save(FILE_PATH)
