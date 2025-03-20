import requests as r
import re


html = r.get("https://emsam-nt.ru/menu/goryachie_rolly").text

rTitle = re.findall(r"<div class=\"catalog-item-text\">.*>(.*)\s*</a>", html)
rSubTitle = re.findall(r"<div class=\"catalog-item-desc\"><p>(.+)\s*</p>", html)
rPrice = re.findall(r"<div class=\"catalog-item-price\">(.+?)</div>", html)

rMenu = re.findall(
    r"<div class=\"catalog-item-text\">.*>(.+)\s*</a> <div class=\"catalog-item-desc\"><p>(.+)\s*</p>.*?<div class=\"catalog-item-price\">(.+?)</div>",
    html,
)

with open("Emsam.txt", "w", encoding="utf-8") as f:
    # for i in range(len(rTitle)):
    #     f.write(f"Title: {rTitle[i]}\nSub-title: {rSubTitle[i]}\nPrice: {rPrice[i]}\n")
    #     f.write("\n")
    n = 1
    for i in rMenu:
        f.write(f"{n}. ")
        f.write(f"Название: {i[0]}\nСостав: {i[1]}\nЦена: {i[2]}\n")
        f.write("\n")
        n += 1
