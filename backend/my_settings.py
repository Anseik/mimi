# my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mimi',
        'USER': 'mimi',
        'PASSWORD': 'mimissafy',
        'HOST': 'j4d108.p.ssafy.io',
        'PORT': '3306',
        'OPTIONS' : {                            
            'charset' : 'utf8mb4'
        }
    }
}
T_KEY = "l7xxed8f27d952c0448fbf4b9e4d354f551f"
SECRET_KEY = "$yg2c-8-8cszt%3k$b=3wwc^j1g%gn)wj%yldz)6jd(ez80u-s"
DOMAIN_URL = "j4d108.p.ssafy.io"
EMAIL = {
    'EMAIL_BACKEND'         :'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_USE_TLS'         :True,
    # 'EMAIL_USE_SSL'         :True # 465,
    'EMAIL_PORT'            :587,
    'EMAIL_HOST'            :'smtp.gmail.com',
    'EMAIL_HOST_USER'       :'ehdrjf337@gmail.com',
    'EMAIL_HOST_PASSWORD'   :'tntjd0206@',
    'DEFAULT_FROM_EMAIL'    :'ehdrjf337@gmail.com',
    
}