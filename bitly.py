from bitlyshortener import Shortener

# Tokens de cuentas
# email:t96ohi.wcaifvf34@khig.site  # username:tohig  # pass:bitly*1234
TOKENS_BITLY = [
    'c66911a01f1f8f8aa8d183c4fd12d9f5c5f7a7bb'
    ]

bitly = Shortener(tokens=TOKENS_BITLY, max_cache_size=100)

# cache bitly
def cache_bitly():
    cache = bitly.cache_info
    return cache

# porciento usado
def uso_bitly():
    uso = round(bitly.usage()*50)
    return str(uso)+"/50"

def acortar(long_url):
    try:
        array = [1]
        array[0] = long_url
        url_bitly = bitly.shorten_urls(array)
        return url_bitly[0]
    except:
        return "Url incorrecta"