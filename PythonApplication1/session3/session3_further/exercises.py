#function with default values


# DOCSTRING 
# doc generator: https://www.sphinx-doc.org/en/master/



def philippsFunction(planet="Earth"):
    """ 
    Greet planet name.
  
    It uses a simple argument and a built-in print function.
  
    Parameters: 
    planet (string): Planet name
  
    Returns: 
  
    """
    print("Hello {}".format(planet))


def functionVariousVar(*planets):
    for planet in planets:
        print("Hello {}".format(planet))


def functionVariousVarDictionary(**planets):
    # print(planets)
    # loop through keys
    # for key in planets:
    #     print("Hello {}".format(   planets[key]   ))

    # # loop thourgh values
    # for planet in planets.values():
    #     print("Hello {}".format(    planet   ))
    # loop thourgh key value pairs
    for key, value in planets.items():
        print("Key: {}, Value: {}".format(    key, value   ))

def richFunction(name, planet, *planets, **kplanets):
    pass


# 4, 6 ==> (4,6)
def functionReturn(a, b):
    a *= 10
    b *= 100

    return a, b
    # return (a, b)


#yield keyword
# generators:
def functionYield(a=[1,2,3,4,5]):
    for item in a:
        yield item


if __name__ == '__main__':
    #pi=philippsfunction
    #pi("Mercury")
    # functionvariousVar("Earth", "Mercury", "Venus", "Jupiter")
    # functionvariousVarDictionary(p1="Earth", p2="Mercury", p3="Venus", p4="Jupiter")

    # x, y = functionReturn(1, 2)
    # (x, y) = functionReturn(1, 2)
    # print("X: {}, Y: {}".format(x,y))



    # import math # https://docs.python.org/3/library/math.html

    # final_sum = sum([1,2,3,5])
    # print(final_sum)

    # f_abs = abs(-10+3)
    # print(f_abs)

    # f_cos = math.cos(45)
    # print(f_cos)

    # yield example:
    # for number in functionYield():
    #     print(number)