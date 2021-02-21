#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The runtime will be O(n), because only one variable is altered and checked.

b) The runtime will be O(nlogn), because the for loop will only run n number of times, and with the inclusion of the nested while loop we are now doing log(n) n number of times.

c) The runtime will be O(n), becuase only one element is passed in and checked in our recursion function.

## Exercise II

We can use a binary search tree to figure out which floors we can drop the eggs, runtime of O(logn). If we drop the egg in the middle floor and breaks go down a floor, if not then go up a floor and we can repeat this strategy until we find f.
