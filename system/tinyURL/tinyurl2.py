import string
import random

class Codec:

    string_base = string.ascii_letters + string.digits
    
    def __init__(self):
        self.encoded_urls = {}
        self.decoded_urls = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # If this is a new longUrl
        while longUrl not in self.encoded_urls:
            encoded_str = ''.join(random.choice(Codec.string_base) for _ in range(6))
            # If this is a new encoded url, we do not want to use same encoded urls for
            # different longUrls
            if encoded_str not in self.decoded_urls:
                self.encoded_urls[longUrl] = encoded_str
                self.decoded_urls[encoded_str] = longUrl
        return 'http://tinyurl.com/' + self.encoded_urls[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        # Retrieve the last 6 digits
        encoded_str = shortUrl[-6:]
        return self.decoded_urls[encoded_str]

if __name__ == '__main__':
    url = 'https://leetcode.com/problems/design-tinyurl'
    codec = Codec()
    print codec.encode(url)
    print codec.decode(codec.encode(url))