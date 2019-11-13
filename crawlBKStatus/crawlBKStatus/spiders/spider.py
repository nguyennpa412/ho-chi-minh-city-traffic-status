import scrapy
import pathlib
import os
from crawlBKStatus.items import FileData


class crawlBKStatusMapFiles(scrapy.Spider):
  name = "statusBKMap"

  def __init__(self, t=None, *args, **kwargs):
    super(crawlBKStatusMapFiles, self).__init__(*args, **kwargs)
    self.start_urls = [
        'http://giaothong.hochiminhcity.gov.vn/'
    ]
    self.t = t

  def parse(self, response):
    statusBKMapDir = str(pathlib.PurePath(
        __file__).parent.parent.parent) + '/statusMapImg/full'
    for f in os.listdir(statusBKMapDir):
      os.remove(os.path.join(statusBKMapDir, f))
    for i in [52182, 52183, 52184, 52185, 52186]:
      for j in [30793, 30794, 30795, 30796]:
        yield FileData(file_urls=['http://giaothong.hochiminhcity.gov.vn:8000/Render/RenderHandler.ashx?level=16&x=%s&y=%s&server=192.168.10.12:8008&maps=HTDP_LINKS_ALL&t=%s' % (i, j, self.t)])
