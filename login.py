import mechanize
import requests
from requests_ntlm import HttpNtlmAuth
from bs4 import BeautifulSoup

result=requests.get("http://10.140.202.115/Citrix/Monitor/OData/v3/Data/Applications",auth=HttpNtlmAuth('XEN\\david','@xi@ns2020'))
print(result.content)