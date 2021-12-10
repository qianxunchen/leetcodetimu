import json
import time
import requests
from bs4 import BeautifulSoup
from tencentcloud.common import credential
from tencentcloud.sms.v20210111 import sms_client, models
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException


def push_code(phone_number, data_list):
    SecretId = 'AKID1rQijTw95j6C2cvykFTQ6VdT2KL4XjdG'
    SecretKey = 'NUKuFK8futc4F9mOjnb8NL2SbT4ORDiw'
    try:
        cred = credential.Credential(SecretId, SecretKey)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "sms.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = sms_client.SmsClient(cred, "ap-guangzhou", clientProfile)

        req = models.SendSmsRequest()
        params = {
            "PhoneNumberSet": [phone_number],
            "SmsSdkAppId": "1400607510",
            "SignName": "植花集公众号",
            "TemplateId": "1234898",
            "TemplateParamSet": data_list
        }
        req.from_json_string(json.dumps(params))

        resp = client.SendSms(req)
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)

def weather_get(city_num):

      url = 'http://www.weather.com.cn/weather1d/%s.shtml#input' % city_num
      headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
      data = requests.get(url=url,headers=headers)
      data.encoding='utf-8'
      if data.status_code == 200:
            data = data.text
            soup = BeautifulSoup(data, 'lxml', from_encoding='utf-8')
            data2 = soup.select('ul[class="clearfix"]')[0]
      # 天气
            tianqi1 = data2.find_all('p', class_=['wea'])[0].text
            tianqi2 = data2.find_all('p', class_=['wea'])[1].text

            if tianqi1 != tianqi2:
                  tianqi = tianqi1+"转"+tianqi2
            else:
                  tianqi = tianqi1
      # 温度
            ssd = "°C"
            qiwen1 = data2.find_all('p', class_=['tem'])[0]
            qiwen1 = qiwen1.find_all('span')[0].text
            qiwen2 = data2.find_all('p', class_=['tem'])[1]
            qiwen2 = qiwen2.find_all('span')[0].text
            if qiwen1 != qiwen2:
                  qiwen = qiwen1+"-"+qiwen2+ssd
            else:
                  qiwen = qiwen1+ssd
      # 时间
      year = time.strftime("%Y", time.localtime())
      month = time.strftime("%m", time.localtime())
      day = time.strftime("%d", time.localtime())
      Time = year+"年"+month+'月'+day+"日"

      # 城市
      citys = {
                  101300907: "玉州区",
                  101300908: '福绵区',
                  101300111: '江南区',
                  101300102: '兴宁区'
      }
      city = citys.get(city_num)
      return [Time, city, tianqi, qiwen]


if __name__ == '__main__':
    '''
    玉州区：101300907
    福绵区：101300908
    江南区: 101300111
    兴宁区：101300102
    '''
    # 服务器运行
    for _ in range(1000):
        data = weather_get(101300907)
        phone_numer = "+8615777589710"
        push_code(phone_numer, data)
        time.sleep(86400)

    # 本地测试
    # data = weather_get(101300907)
    # phone_numer = "+8615777589710"
    # push_code(phone_numer, data)
