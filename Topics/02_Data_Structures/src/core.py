"""

   An first example of a sequence type, tuples.

   >>> numbers = (1, 30, 500, 70, 9)
   >>> len(numbers)
   5
   >>> numbers[2]
   500

   Example of list, mutable data type

   >>> numbers = [1, 30, 500, 70, 9]
   >>> numbers[2] = 0
   >>> numbers
   [1, 30, 0, 70, 9]

   Heterogenous data structure

   >>> employee_record = ("George", "lecturer", 4, 1.73)

   Perils of mutability:

   >>> L = [10, 20]
   >>> KL = [L, L]
   >>> KL
   [[10, 20], [10, 20]]
   >>> L[0] = 30
   >>> KL
   [[30, 20], [30, 20]]

   For loop

   >>> L = [10, 20, 30]
   >>> total = 0
   >>> for x in L:
   ...   total += x
   >>> total
   60


"""