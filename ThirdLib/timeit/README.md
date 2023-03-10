# `timeit`程序执行计时

## `timeit.timeit`
```text
The module function timeit.timeit(stmt, setup, timer, number) accepts four arguments: 
1. stmt which is the statement you want to measure; it defaults to ‘pass’.
2. setup which is the code that you run before running the stmt; it defaults to ‘pass’. 
We generally use this to import the required modules for our code.
3. timer which is a timeit.Timer object; it usually has a sensible default value so you don’t have to worry about it.
4. number which is the number of executions you’d like to run the stmt.
The output of above program will be the execution time(in seconds) for 10000 iterations of the code snippet passed to timeit.timeit() function.
```

## 参考链接
* 1 [`timeit.timeit`的示例](https://www.geeksforgeeks.org/timeit-python-examples/)