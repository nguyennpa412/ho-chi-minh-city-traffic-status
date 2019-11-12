import scrapy
import pathlib
import os
from crawlD1Status.items import FileData


class crawlD1StatusMapFiles(scrapy.Spider):
  name = "statusD1Map"

  def __init__(self, t=None, *args, **kwargs):
    super(crawlD1StatusMapFiles, self).__init__(*args, **kwargs)
    self.start_urls = [
        'http://giaothong.hochiminhcity.gov.vn/'
    ]
    self.t = t

  def parse(self, response):
    statusD1MapDir = str(pathlib.PurePath(
        __file__).parent.parent.parent) + '/statusMapImg/full'
    for f in os.listdir(statusD1MapDir):
      os.remove(os.path.join(statusD1MapDir, f))
    for i in [26092, 26093, 26094, 26095, 26096, 26097, 26098]:
      for j in [15395, 15396, 15397, 15398, 15399]:
        yield FileData(file_urls=['http://giaothong.hochiminhcity.gov.vn:8000/Render/RenderHandler.ashx?level=15&x=%s&y=%s&server=192.168.10.12:8008&maps=HTDP_LINKS_ALL&t=%s' % (i, j, self.t)])
