import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time


def url():
    return input("Please type competition name: ")


def title_script(url_name):
    options = Options()
    # ヘッドレスモードで実行する場合
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url_name)
    # 簡易的にJSが評価されるまで秒数で待つ
    time.sleep(3)

    html = driver.page_source.encode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find_all("h1", attrs={"class": "competition-header__title"})

    if len(str(title)) == 2:
        print("ERROR")
        title_script(url())

    title = str(title).split('>')[1].split("<")[0].replace(" ", "_")
    print("Directory name: ", title.replace(" ", "_"))
    os.mkdir("Competition/" + title)
    os.mkdir("Competition/" + title + "/data")
    os.mkdir("Competition/" + title + "/model")
    os.mkdir("Competition/" + title + "/notebook")
    os.mkdir("Competition/" + title + "/Log")
    print("Done")
    print("Kaggle精進しろ")


if __name__ == "__main__":
    title_script(url())
