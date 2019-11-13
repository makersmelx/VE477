# LAB 5

<center>Wu Jiayao 517370910257
</center>

## Compare the efficiency of Bellman-Ford and Dijkstra in terms of (i) complexity and (ii) running time

### (i) Complexity

With the use of  Fibonacci heap, the complexity of Dijkstra is $\mathcal{O}(|E|+V\log|V|)$ for Graph<V,E>

The complexity of Bellman-Ford is $\mathcal{O}(|V||E|)$  for Graph<V,E>

### (ii) Running time

Here is a test case **case.txt** with 3734 edges, downloaded from Coursera course, attached with the report.

~~~shell
 time python3 Dijkstra.py < case.txt
 time python3 BellmanFord.py < case.txt
~~~

Output:

~~~shell
['0', '79', '18', '186']

real    0m0.079s
user    0m0.047s
sys     0m0.016s
['0', '79', '18', '186']

real    0m0.428s
user    0m0.406s
sys     0m0.031s
~~~

### Conclusion

In graphs that has no negative cycles (the assumption), Dijkstra does better than Bellman - Ford both in theoretical complexity and practical running time.