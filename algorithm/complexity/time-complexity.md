## How to Analyze Time Complexity
* Input - Rate of growth of time, let's define the following model machine with conditions:
  * Single processor
  * 32 bit machine
  * Sequential of execution
  * 1 unit time for arithmetical and logical operations
  * 1 unit of time for assignment and return
  * Exmaple:
  ```bash
      def sum(a, b):
          return a + b
      Using the model machine, we have Tsum = 2 units, 1 unit for add op, 1 unit for return

      This example is a constant time algorithm.

      def sum_of_list(array, size_of_array):
          total = 0
          for i in range(size_of_array):
              total = total + array[i]
          return total
     Using the model machine, we have:
         1 unit + 2(n+1) units + 2n units + 1 unit = 4n + 4
         T(n) = Cn + C'
  ```
* Asymptotic notations
  * Algorithm1: T(n) = 5n^2 + 7
  * Algorithm2: T(n) = 17n^2 + 6n + 8
  * Both are running on our model machine.
  * when n -> oo, constant can be ignored
  * "Big-oh": Upper bound of the rate growth of time
  ```bash
  f(n) = 5n^2 + 2n + 2 = O(n^2)
  g(n) = n^2
  ```
  * Omega notation: lower bound of the growth of time
  ```bash
  f(n) = 5n^2 + 2n + 2 = O(n^2)
  g(n) = n^2
  for c = 5, n = 0
  5n^2 <= f(n), n >= 0
  ```
  * Theta notation: tight bount
  ```bash
  f(n) = 5n^2 + 2n + 2 = O(n^2)
  g(n) = n^2
  for c = 5, n = 0
  5n^2 <= f(n), n >= 0
  ```