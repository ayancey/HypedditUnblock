import requests
import lxml.html

s = requests.session()
s.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"
})


def get_download_file(url):
    r = s.get(url)
    root = lxml.html.fromstring(r.text)

    unique_id = root.xpath("//input[@id='current_download_file_listner']/@value")
    title = root.xpath("//title/text()")

    if unique_id:
        return {
            "file_name_suggestion": title[0].split("|")[0].strip(),
            "url": "https://hypeddit-gates-prod.s3.amazonaws.com/" + unique_id[0] + "_main"
        }


if __name__ == "__main__":
    print(get_download_file("https://hypeddit.com/ominousbeatsseason1/morhiphopfreedownloadroyaltyfree"))
