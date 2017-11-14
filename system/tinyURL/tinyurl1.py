class Codec:

    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        # We simply calculate the length of the urls array
        # Then use the (length - 1) number as the shortened url
        return 'http://tinyurl.com/' + str(len(self.urls)-1)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        # Decode is simple, we just need to retrive the
        # last number after the '/'
        # Remeber index starts from 0
        return self.urls[int(shortUrl.split('/')[-1])]

if __name__ == '__main__':
    url = 'https://leetcode.com/problems/design-tinyurl'
    codec = Codec()
    print codec.encode(url)
    print codec.decode(codec.encode(url))