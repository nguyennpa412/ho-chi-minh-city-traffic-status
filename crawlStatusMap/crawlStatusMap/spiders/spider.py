import scrapy
from crawlStatusMap.items import FileData


class crawlStatusMapFiles(scrapy.Spider):
  name = "statusMap"
  start_urls = [
      'http://giaothong.hochiminhcity.gov.vn/'
  ]

  def parse(self, response):
    for i in [1629, 1630, 1631, 1632, 1633]:
      for j in [961, 962, 963, 964]:
        yield FileData(file_urls=['http://giaothong.hochiminhcity.gov.vn:8000/Render/RenderHandler.ashx?level=11&x=%s&y=%s&server=192.168.10.12:8008&maps=HTDP_LINKS_ALL' % (i, j)])
