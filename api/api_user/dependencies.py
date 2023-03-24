import requests
from fake_useragent import UserAgent

header = {
    "User-Agent": UserAgent().chrome,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US",
    # "Connection": "keep-alive",
}