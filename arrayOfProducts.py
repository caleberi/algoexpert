def arrayOfProducts(array):
    if len(array) == 0 or len(array) == 1:
        return array
    result = []
    for i in range(0, len(array)):
        stepBackward = i-1
        stepForward = i+1
        product = 1
        while stepBackward >= 0:
            product *= array[stepBackward]
            stepBackward -= 1
        while stepForward < len(array):
            product *= array[stepForward]
            stepForward += 1
        result.append(product)

    return result


def arrayOfProductsV2(array):
    if len(array) == 0:
        return array
    if len(array) == 1:
        return []
    result = []
    for i in range(0, len(array)):
        product = 1
        if i == 0:
            product *= getProduct(array[i+1:])
        elif i == len(array)-1:
            product *= getProduct(array[:i])
        else:
            newProductArray = array[i+1:]+array[:i]
            product *= getProduct(newProductArray)

        result.append(product)
    return result


def getProduct(array, accumulator=1):
    for i in range(len(array)):
        accumulator *= array[i]
    return accumulator


def arrayOfProductsV3(array):
    if len(array) == 0:
        return array
    if len(array) == 1:
        return []
    products = [1 for _ in range(len(array))]
    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
        products[i] = runningProduct
    return products


def arrayOfProductsV4(array):
    if len(array) == 0:
        return array
    if len(array) == 1:
        return []
    products = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]

    runningLeftProduct = 1
    for i in range(len(array)):
        leftProducts[i] = runningLeftProduct
        runningLeftProduct *= array[i]
    runningRightProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = runningRightProduct
        runningRightProduct *= array[i]

    for i in range(len(array)):
        products[i] = leftProducts[i]*rightProducts[i]
    return products



def arrayOfProductsV5(array):
    if len(array) == 0:
        return array
    if len(array) == 1:
        return []
    products = [1 for _ in range(len(array))]

    runningLeftProduct = 1
    for i in range(len(array)):
        products[i] = runningLeftProduct
        runningLeftProduct *= array[i]
    runningRightProduct = 1
    for i in reversed(range(len(array))):
        products[i] *=runningRightProduct
        runningRightProduct *= array[i]

    return products

print(arrayOfProducts([5, 1, 4, 2]))
print(arrayOfProductsV2([5, 1, 4, 2]))
print(arrayOfProductsV3([5, 1, 2, 4]))
print(arrayOfProductsV4([5, 1, 2, 4]))
print(arrayOfProductsV5([5, 1, 2, 4]))