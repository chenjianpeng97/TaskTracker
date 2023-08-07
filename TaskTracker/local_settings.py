"""
change every settings here
separate develop and testing
"""
LANGUAGE_CODE = 'zh-hans'

# 短信模板,在local_settings中自行更改
# 腾讯云短信应用 app_id https://console.cloud.tencent.com/smsv2/app-manage
TENCENT_SMS_APP_ID = 1400822312
# 腾讯云短信应用的 app_key https://console.cloud.tencent.com/smsv2/app-manage/detail
TENCENT_SMS_APP_KEY = "136ffd16543c8d258d7b50f81e48deee"
# 腾讯云短信签名内容 https://console.cloud.tencent.com/smsv2/csms-sign
TENCENT_SMS_SIGN = "一击格斗公众号	"
# 腾讯云短信模板 https://console.cloud.tencent.com/smsv2/csms-template
TENCENT_SMS_TEMPLATE = {
    'account': 1800161,
    'login': 1800158,
    'reset': 1800132,
}
'''
django-redis配置
'''
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://172.25.12.80:6379',  # redis服务器位置
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                "encoding": 'utf-8',
            },
            # "PASSWORD": ""
        }
    }
}
