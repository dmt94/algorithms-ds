### Big O

Big O notation only concerns itself with general categories of algorithm steps

Big O notation doesn't care about the number of steps an algorithm takes. It cares about the long-term trajectory of the algorithm's steps AS THE DATA INCREASES.

While Big O is helpful for contrasting algorithms that fall under different classifications of Big O, when two algorithms fall under the same classification, further analysis is required to determine which algorithm is faster.


O(N) tells the story of linear growth, steps increase in a straight line according to some proportion of the data, regardless of the magnitude O(100N) or O(1000N), etc. O(N^2) tells of exponential growth.


Big O Notation only takes into account the highest order of N when we have multiple orders added together.

```
N^2 + (2N - 2)

N^2 + N

N^2 - the highest order of N
```


Best- and worst-case scenarios happen relatively infrequently. In the real world, average scenarios are what occur most of the time.

