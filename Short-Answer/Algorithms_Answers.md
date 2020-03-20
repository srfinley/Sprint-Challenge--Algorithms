#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Normally it would be easy to say this is O(n^3), but the fact that a increments by the square of n gives me pause. I tested this by hand with small values, then implemented a modified version (that counts the number of loops executed) with large values, and found that both tests resulted in a number of loops equal to n. I believe this is because n^3 (the runtime of a conventionally-incrementing loop) divided by n^2 (the actual increments) is equal to n. Therefore, **O(n)**.


b)


c) Although this is a recursive function, it only calls itself once per call; one could imagine it seamlessly rewritten as a for loop over n. Each marginal bunny only results in one extra call. I believe its runtime is **O(n)**.

## Exercise II

We are looking for a value f such that the egg does break when thrown from floor f, but does not when thrown from floor f-1.

(For houses of buildings size and chicken eggs, f = 1. I assume we are dealing with some kind of egg drop contest situation here, or possibly a building for ants or an egg of astonishing durability.)

To minimize the number of eggs tested (I assume this is what is meant by "number of dropped + broken eggs"), a binary search strategy should be implemented. When we have no idea where f might be, binary search allows us to rule out the largest possible number of values per test. No strategy will allow us to determine f if it is greater than n.

First drop an egg from the middle of the building, at n // 2. If it breaks, we know f is less than or equal to this floor number -- n // 2 is our new ceiling value, formerly n. If it doesn't, we know f is greater than that floor number -- n // 2 is our new floor value, formerly 0. Either way, half the floors have been eliminated from consideration. We turn our attention to the floors that have not been eliminated and find the middle value from which to conduct test two.

The number of tests conducted depends on the value of n, but each test narrows the range of possibility such that eventually we will have tested both floor x and x-1 and observed breakage in the former case but not the latter. Once that observation has been made, we will have conclusively proven the value of f = x.

The runtime complexity of this is **O(logn)**.