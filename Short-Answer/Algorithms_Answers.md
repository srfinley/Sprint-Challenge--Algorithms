#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Normally it would be easy to say this is O(n^3), but the fact that a increments by the square of n gives me pause. I tested this by hand with small values, then implemented a modified version (that counts the number of loops executed) with large values, and found that both tests resulted in a number of loops equal to n. I believe this is because n^3 (the runtime of a conventionally-incrementing loop) divided by n^2 (the actual increments) is equal to n. Therefore, **O(n)**.


b)


c) Although this is a recursive function, it only calls itself once per call; one could imagine it seamlessly rewritten as a for loop over n. Each marginal bunny only results in one extra call. I believe its runtime is **O(n)**.

## Exercise II


