import subprocess
import hashlib
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from scrapy.utils.python import to_bytes
app = Flask(__name__, template_folder='./', static_folder='./')


def urlToImg(t):
  mapArray = []
  for i in [1629, 1630, 1631, 1632]:
    mapArray.append([])
    for j in [961, 962, 963]:
      mapArray[i-1629].append([])
      mapArray[i-1629][j-961].append(str(i) + '_' + str(j))
      mapArray[i-1629][j-961].append('./crawlStatusMap/statusMapImg/full/' + str(hashlib.sha1(to_bytes(
          'http://giaothong.hochiminhcity.gov.vn:8000/Render/RenderHandler.ashx?level=11&x=%s&y=%s&server=192.168.10.12:8008&maps=HTDP_LINKS_ALL&t=%s' % (i, j, t))).hexdigest()))
  return mapArray


def urlToImgD1(t):
  d1MapArray = []
  for i in [26092, 26093, 26094, 26095, 26096, 26097, 26098]:
    d1MapArray.append([])
    for j in [15395, 15396, 15397, 15398, 15399]:
      d1MapArray[i-26092].append([])
      d1MapArray[i-26092][j-15395].append(str(i) + '_' + str(j))
      d1MapArray[i-26092][j-15395].append('./crawlD1Status/statusMapImg/full/' + str(hashlib.sha1(to_bytes(
          'http://giaothong.hochiminhcity.gov.vn:8000/Render/RenderHandler.ashx?level=15&x=%s&y=%s&server=192.168.10.12:8008&maps=HTDP_LINKS_ALL&t=%s' % (i, j, t))).hexdigest()))
  return d1MapArray


def urlToImgBK(t):
  bkMapArray = []
  for i in [52182, 52183, 52184, 52185, 52186]:
    bkMapArray.append([])
    for j in [30793, 30794, 30795, 30796]:
      bkMapArray[i-52182].append([])
      bkMapArray[i-52182][j-30793].append(str(i) + '_' + str(j))
      bkMapArray[i-52182][j-30793].append('./crawlBKStatus/statusMapImg/full/' + str(hashlib.sha1(to_bytes(
          'http://giaothong.hochiminhcity.gov.vn:8000/Render/RenderHandler.ashx?level=16&x=%s&y=%s&server=192.168.10.12:8008&maps=HTDP_LINKS_ALL&t=%s' % (i, j, t))).hexdigest()))
  return bkMapArray


@app.route("/")
def main():
  return render_template('index.html')


@app.route('/updateStatus', methods=['POST'])
def updateStatus():
  t = int(datetime.timestamp(datetime.now()))*1000
  subprocess.check_call(['scrapy', 'crawl', 'statusMap',
                         '-a', 't=%s' % t], cwd='./crawlStatusMap')
  return jsonify(res=urlToImg(t))


@app.route('/updateD1Status', methods=['POST'])
def updateD1Status():
  t = int(datetime.timestamp(datetime.now()))*1000
  subprocess.check_call(['scrapy', 'crawl', 'statusD1Map',
                         '-a', 't=%s' % t], cwd='./crawlD1Status')
  return jsonify(res=urlToImgD1(t))


@app.route('/updateBKStatus', methods=['POST'])
def updateBKStatus():
  t = int(datetime.timestamp(datetime.now()))*1000
  subprocess.check_call(['scrapy', 'crawl', 'statusBKMap',
                         '-a', 't=%s' % t], cwd='./crawlBKStatus')
  return jsonify(res=urlToImgBK(t))


if __name__ == "__main__":
  app.run()
