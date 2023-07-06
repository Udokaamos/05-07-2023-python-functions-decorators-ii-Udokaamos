# Function decorators II

## Description

In this exercise, we will keep practicing on decorators.

*In each function created throughout these exercises the body of the function must contain a **dosctring** (a first line with a string explaining what the function does).*

##

## Tasks

###

### Task 1

Create a decorator named `validate_numeric` to validate if the input arguments of a function are numeric (types `int` or `float`).

If any of the arguments passed to the function are not numeric, it should return a message `The input arguments must be numeric` and stop execution. Otherwise, it should execute the decorated function normally.

Use the following test case:

```
@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(1, "2"))
print(sum(a=1, b="a"))
print(sum(a=1, b=3.4))
```

- Your result should look like this:

```
3
The input arguments must be numeric
The input arguments must be numeric
4.4
```

###

### Task 2

Keep the previous code and now create an additional decorator named `debug`. This will let us get some information on the execution of the function without having to add `print` all over the body of the function.

This decorator should simply output information about the input and output arguments. It should indicate both the positional and keyword arguments passed to the function and the output before returning it.

Use the following test cases:

```
@debug
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

sum(1, 2)
sum(a=1, b=2)
sum(1, "a")
```

- Your result should look like this:

```
**********
Positional arguments: 1,2
There are no keyword arguments
Result: 3
**********
There are no positional arguments
Keyword arguments: a=1,b=2
Result: 3
**********
Positional arguments: 1,a
There are no keyword arguments
Result: The input arguments must be numeric
```

###

### Task 3

Now you will create a decorator named `cache` that will store in memory the output of every particular call to a function. This way, if we call the function twice with the same input parameters, the function will not be called the second time and the result will be fetched from the cache instead.

The function will also print `Calculating` when it is the first time we use a particular call and `Using the cache` in any other case.

> To do so, you can create a global variable to store the output of the calls, but try to think a way to do it without any global variable.

The variable that will store the cache may be a dictionary whose keys are the actual function used and the value another dictionary with the input arguments list as key and the output as value. Example:

```
{
    <function sum at 0x7fcd34ced840>: {
        (1, 2): 3,
        (3, 2): 5
    }
}
```

Use the following test cases:

```
@cache
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(1, 2))
print(sum(3, 2))
print(sum(3, 2))
print(sum(2, 1))
```

- Your result should look like this:

```
Calculating
3
Using the cache
3
Calculating
5
Using the cache
5
Calculating
3
```
