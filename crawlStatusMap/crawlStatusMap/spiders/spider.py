import scrapy
import pathlib
import os
from crawlStatusMap.items import FileData


class crawlStatusMapFiles(scrapy.Spider):
  name = "statusMap"

  def __init__(self, t=None, *args, **kwargs):
    super(crawlStatusMapFiles, self).__init__(*args, **kwargs)
    self.start_urls = [
        'http://giaothong.hochiminhcity.gov.vn/'
    ]
    self.t = t

  def parse(self, response):
    statusMapDir = str(pathlib.PurePath(
        __file__).parent.parent.parent) + '/statusMapImg/full'
    for f in os.listdir(statusMapDir):
      os.remove(os.path.join(statusMapDir, f))
    for i in [1629, 1630, 1631, 1632]:
      for j in [961, 962, 963]:
        yield FileData(file_urls=['http://giaothong.hochiminhcity.gov.vn:8000/Render/RenderHandler.ashx?level=11&x=%s&y=%s&server=192.168.10.12:8008&maps=HTDP_LINKS_ALL&t=%s' % (i, j, self.t)])
