import os


try:
    REDIS_URL = os.environ['REDIS_URL']
except KeyError:
    REDIS_URL = 'redis://127.0.0.1:6379'


try:
    NEWS_ADMIN = [i for i in os.environ['NEWS_ADMIN'].split(';') if i != ""]
except KeyError:
    NEWS_ADMIN = []

try:
    LOGIN_API_KEY = os.environ['LOGIN_API_KEY']
except KeyError:
    LOGIN_API_KEY = []

try:
    NEWS_ADMIN_ACCOUNT = os.environ['NEWS_ADMIN_ACCOUNT']
    NEWS_ADMIN_PASSWORD = os.environ['NEWS_ADMIN_PASSWORD']
except KeyError:
    NEWS_ADMIN_ACCOUNT = None
    NEWS_ADMIN_PASSWORD = None

JWT_EXPIRE_TIME = 3600
ADMIN_JWT_EXPIRE_TIME = 43200
# crawler zone
WEBAP_LOGIN_TIMEOUT = 5
WEPAP_QUERY_TIMEOUT = 5
LIBRARY_LOGIN_TIMEOUT = 5
LEAVE_LOGIN_TIMEOUT = 4
ACAD_TIMEOUT = 3
#: AP guest account
AP_GUEST_ACCOUNT = "guest"
#: AP guest password
AP_GUEST_PASSWORD = "123"

# cache zone
CACHE_USER_HASH_EXPIRE_TIME = 600
CACHE_WEBAP_COOKIE_EXPIRE_TIME = 600
CACHE_BUS_COOKIE_EXPIRE_TIME = 600
CACHE_LIBRARY_EXPIRE_TIME = 600
CACHE_LIBRARY_USER_INFO_EXPIRE_TIME = 600
CACHE_LEAVE_COOKIE_EXPIRE_TIME = 600
CACHE_WEBAP_QUERY_DEFAULT_EXPIRE_TIME = 600
CACHE_SEMESTERS_EXPIRE_TIME = 3600
CACHE_GRADUTION_EXPIRE_TIME = 3600
CACHE_LEAVE_LIST_EXPIRE_TIME = 3600
CACHE_BUS_USER_RESERVATIONS = 600
CACHE_WEBAP_QUERY_DEFAULT_EXPIRE_TIME = 600
CACHE_BUS_VIOLATION_RECORD_EXPIRE_TIME = 600
CACHE_SEMESTERS_EXPIRE_TIME = 3600
CACHE_GRADUTION_EXPIRE_TIME = 3600
CACHE_BUS_TIMETABLE_EXPIRE_TIME = 60
# why course table expire time so long?
# read parse.py, it's worth it.
CACHE_COURSETABLE_EXPIRE_TIME = 60*60*6  # 6 hours

CACHE_GRADUATE_USER_INFO_EXPIRE_TIME = 3600
CACHE_SERVER_STATUS_EXPITE_TIME = 600
CACHE_ACAD_EXPIRE_TIME = 3600

CACHE_LEAVE_SUBMIT_EXPIRE_TIME = 21600

LEAVE_PROOF_IMAGE_SIZE_LIMIT = 1024*1024*3  # 3MB
