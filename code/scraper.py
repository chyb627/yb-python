from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self):
        self.__url = "https://www.yes24.com/Product/Category/BestSeller?"
        self.__params = {
            "categoryNumber": "001",
        }
        self.__headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        }

    def do(self):
        response = requests.get(self.__url, params=self.__params, headers=self.__headers)
        # print(response.status_code)
        # print(response.text)

        soup = BeautifulSoup(response.text, "html.parser")
        list_box = soup.find("ul", class_="sGLi tp_book tp_chkG tp_best tp_list")
        # print(list_box)
        item_boxes = list_box.find_all("div", class_="itemUnit")
        # item_boxes = list_box.find_all("a", class_="gd_name")
        # print(item_boxes)

        result = []
        for item_box in item_boxes:
            # 출판사 가져오기
            item_title = item_box.find("span", class_="authPub info_pub")
            # print(item_title.text)
            brand = item_title.text

            # 책 이름, URL 가져오기
            item_link = item_box.find("a", class_="gd_name")
            # print(item_link.text.strip())
            name = item_link.text.strip()
            url = "https://www.yes24.com" + item_link["href"]

            # 책 글쓴이 가져오기
            item_writer = item_box.find("span", class_="authPub info_auth")
            # print(item_writer.text.strip())
            writer = item_writer.text.strip()

            # 책 가격 가져오기
            item_price = item_box.find("strong", class_="txt_num")
            # print(item_price.text.strip())
            price = item_price.text.strip()

            item = {
                "book_brand": brand,
                "book_name": name,
                "book_writer": writer,
                "book_price": price,
                "book_url": url
            }
            # print(item)
            result.append(item)
        return result
                

if __name__ == "__main__":
    scraper = Scraper()
    items = scraper.do()
    print(items)