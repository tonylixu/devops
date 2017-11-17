## Problem definition
TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

## Solution analysis
First of all, I think we need to understand this question a little bit better. We should at least trying to undertand why the hell do we need to shorten the URL, what kind of benefit does that give you?

### What is TinyURL?
TinyURL is a URL shortening web service, which provides short aliases for redirection of long URLs. It takes long URLs and shrink them into much smaller ones, then when you enter the shortened URL into web browser, they gets converted back to the original length. One of the advantage of shorten URL is easy to remember, written down and post.

### Technical background
The URL shortening problem is all about generating a short and unique key (alias) for a given URL and whenever the shorten URL is been requested, they will be redirected to the real URL.

Two shorten solutions:
* Encoding actual URL: Compute a unique hash (MD5 or SHA256) of the given URL. The hash can then be encoded for displaying. The encoding could be based36([a-z,0-9]) or base62([A-Z,a-z,0-9]) and base64 if we add `-` and `.`.
* Generating keys offline: We can have a standalone Key Generation Service(KGS) that generates random six letter strings beforehand and stores them in a database. Whenever we want to shorten a URL, we will just take one of the already generated keys and use it. This approach will make things quite simple and fast since we are not encoding the URL or worrying about duplications or collisions. KGS will make sure all the keys inserted in our keys database are unique.

### Solution1
The easiest and stupid solution :). The main idea is, we define a list to hold all the urls, and for each url, we simplely use the list index number as the string after the '/'.

For example:
```python
url_lists = [
    'https://leetcode.com/problems/design-tinyurl',
    'https://leetcode.com/problems/design-tinyurlaa',
    'https://leetcode.com/problems/design-tinyurlbbb'
]

# The shortened URLs
url_lists_shortened = [
    'http://tinyurl.com/0',
    'http://tinyurl.com/1',
    'http://tinyurl.com/2'
]

# Encoding
return 'http://tinyurl.com/' + str(len(url_lists)-1)

# Decoding
return url_lists[int(url_lists_shortened[i].split('/')[-1])]
```

### Solution2
So solution1 has some disadvantages:
* For the same url, it output different encodings
* It is easy to tell how many urls have been encoded
* The space complexity can go huge easily. 

So instead of using increasing numbers, in our second solution, we use fixed length characters. 
Data structure:
* We will have two dictionaries, encoded_urls and decoded_urls
* For a given encoding:
  * https://leetcode.com/problems/design-tinyurl
  * http://tinyurl.com/KtLa2U
* The mapping will be:
  * encoded_urls[longUrl] = 'http://tinyurl.com/KtLa2U'
  * decoded_urls['KtLa2U'] = longUrl

Steps:
* Randomly generate a 6 character string
* Append the randomly generatly string to 'http://tinyurl.com/'
* Record the mapping between encoded string and original string
* Return the encoded string
* For decode, simply gi