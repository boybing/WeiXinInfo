import requests


def getWeiXinInfo():
    appid='wxa976cd396e03cb0e'
    Sc='4829eb8814ee18f83744175cce1a2a15'
    bk='nywshl.herokuapp.com'
    urlString='https://open.weixin.qq.com/connect/oauth2/authorize?appid='+appid+'&redirect_uri='+bk+'&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect'
    requests.get(url=urlString)

getWeiXinInfo()