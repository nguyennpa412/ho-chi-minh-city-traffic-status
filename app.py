import subprocess
import hashlib
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from scrapy.utils.python import to_bytes
app = Flask(__name__, template_folder='./', static_folder='./')


def urlToImg(t):
  res = []
  mapArray = []
  for i in [1629, 1630, 1631, 1632]:
    mapArray.append([])
    for j in [961, 962, 963]:
      mapArray[i-1629].append([])
      mapArray[i-1629][j-961].append(str(i) + '_' + str(j))
      mapArray[i-1629][j-961].append('./crawlStatusMap/statusMapImg/full/' + str(hashlib.sha1(to_bytes(
          'http://giaothong.hochiminhcity.gov.vn:8000/Render/RenderHandler.ashx?level=11&x=%s&y=%s&server=192.168.10.12:8008&maps=HTDP_LINKS_ALL&t=%s' % (i, j, t))).hexdigest()))
  res.append(mapArray)
  d1MapArray = []
  for i in [26092, 26093, 26094, 26095, 26096, 26097, 26098]:
    d1MapArray.append([])
    for j in [15395, 15396, 15397, 15398, 15399]:
      d1MapArray[i-26092].append([])
      d1MapArray[i-26092][j-15395].append(str(i) + '_' + str(j))
      d1MapArray[i-26092][j-15395].append('./crawlD1Status/statusMapImg/full/' + str(hashlib.sha1(to_bytes(
          'http://giaothong.hochiminhcity.gov.vn:8000/Render/RenderHandler.ashx?level=15&x=%s&y=%s&server=192.168.10.12:8008&maps=HTDP_LINKS_ALL&t=%s' % (i, j, t))).hexdigest()))
  res.append(d1MapArray)
  return res


@app.route("/")
def main():
  return render_template('index.html')


@app.route('/updateStatus', methods=['POST'])
def updateStatus():
  t = int(datetime.timestamp(datetime.now())*1000)
  subprocess.check_call(['scrapy', 'crawl', 'statusMap',
                         '-a', 't=%s' % t], cwd='./crawlStatusMap')
  subprocess.check_call(['scrapy', 'crawl', 'statusD1Map',
                         '-a', 't=%s' % t], cwd='./crawlD1Status')
  return jsonify(res=urlToImg(t))


if __name__ == "__main__":
  app.run()