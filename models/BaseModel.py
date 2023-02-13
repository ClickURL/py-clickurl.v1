# In this file implemented model that do encode and decode to base6
import base64

class BaseModel:
    
    def encode_url(self, url_income: str):
        url_encode_utf8 = url_income.encode("UTF-8")
        url_encode_base64 = base64.b64encode(url_encode_utf8)
        result = url_encode_base64.decode("UTF-8")
        return result
    
    def decode_url(self, url_outcome: str):
        url_encode_utf8 = url_outcome.encode("UTF-8")
        url_decode_base64 = base64.b64decode(url_encode_utf8)
        result = url_decode_base64.decode("UTF-8")
        return result
