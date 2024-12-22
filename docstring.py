def add(x: int, y: int) -> int:
    """
    calculate sum of two numbers.
    parameters
    ----------
    x : INT
    y : INT
    Returns
    ----------
    INT (sum of x and y)
    """
    return x+y 
print(add(5, 2))
print(add.__doc__)
print(add.__annotations__)