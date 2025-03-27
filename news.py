import requests as r
import re


html = r.get("https://www.roscosmos.ru/102/").text

rTitle = re.findall(r"<span class=\"name\">(.+)</span>", html)
rDate = re.findall(r"<span class=\"date\">(\d\d)\.(\d\d)\.(\d{4})</span>", html)
rSubTitle = re.findall(r"<span class=\"anons\">(.+)</span>", html)
rSrc = re.findall(r"<a class=\"link\" href=\"(.*)\">", html)
with open("news.txt", "w", encoding="utf-8") as f:
    for i in range(len(rTitle)):
        f.write(
            f"Date: {".".join(rDate[i])}\nTitle: {rTitle[i]}\nsrc: {rSrc[i]}\nsub-title: {rSubTitle[i]}\n"
        )
        f.write("\n")
