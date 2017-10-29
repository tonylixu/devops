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
  ```
* 