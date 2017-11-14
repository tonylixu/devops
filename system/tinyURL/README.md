## Problem definition
TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

## Solution analysis
First of all, I think we need to understand this question a little bit better. We should at least trying to undertand why the hell do we need to shorten the URL, what kind of benefit does that give you?

### What is TinyURL?
TinyURL is a URL shortening web service, which provides short aliases for redirection of long URLs. It takes long URLs and shrink them into much smaller ones, then when you enter the shortened URL into web browser, they gets converted back to the original length. One of the advantage of shorten URL is easy to remember, written down and post.

### Technical background
The URL shortening problem 
