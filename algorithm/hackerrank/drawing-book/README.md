### Problem definition
Brie’s Drawing teacher asks her class to open their -page book to page number 1. Brie can either start turning pages from the front of the book (i.e., page number 1) or from the back of the book (i.e., page number n), and she always turns pages one-by-one (as opposed to skipping through multiple pages at once). When she opens the book, page 1 is always on the right side:
[0 | 1]

Each page in the book has two sides, front and back, except for the last page which may only have a front side depending on the total number of pages of the book.

Given `n` and `p`, find and print the minimum number of pages Brie must turn in order to arrive at page `p`.

Input Format:
* The first line contains an integer n, denoting the number of pages in the book. 
* The second line contains an integer p, denoting the page that Brie's teacher wants her to turn to.

Output Format:
* Print an integer denoting the minimum number of pages Brie must turn to get to page `p`.


Constraints:
* 1 <= n <= 10^5
* 1 <= p <= n

Sample Input:
* Input: (6,2), output: 1
* Input: (5,4), output: 0 (You don't need to turn the page)

### Problem analysis
* Obvisouly this problem can be abstract to an array problem, you know the length of the array and you need to find the shortest distance between a given point to the head and tail of the array.
* The solution is easy, you calculate the distance from the head to the given point, and you calculate the distance from the tail to the given point, then return the smaller one.
* Since each page is double sided, each flip of page means two moves in the array, so if you are at page #5, you need 2 (5/2) page flips [0|1, 2|3, 4|5] from the begining of the page; if you are at page #7, you need 3 page flips [0|1, 2|3, 4|5], 6|7]. You can calculte this number of flips by (7/2).
* You can apply the same idea from the tail, give a 7 pages book [0|1, 2|3, 4|5], 6|7], to get to page #2 from the back, you need (7-2)/2 flips ((The total number of steps from page #0 to #7) - (the number of steps from page #0 to page #p).
* From page #1 to page #n, you need n/2 number of flips.

### Solution
See `solution1.py`. Both time complexity and space complexity on `solution1.py` is constant.

### Optimization
There is not much you can do on the time and space complxity, but you can probably do something to the edge cases. If you put edge cases in the main solution, the main solution actually covers the edge cases. So to optimize, we don't need to conisder edge cases. See `solution2.py`

