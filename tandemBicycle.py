def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    return getMaximumTotalSpeed(redShirtSpeeds, blueShirtSpeeds, fastest)


def getMaximumTotalSpeed(redShirtSpeeds, blueShirtSpeeds, fastest):
    if len(redShirtSpeeds) == 0 and len(blueShirtSpeeds) == 0:
        return 0
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    fastestRedRider = redShirtSpeeds[-1]
    fastestBlueRider = blueShirtSpeeds[-1]
    slowestRedRider = redShirtSpeeds[0]
    slowestBlueRider = blueShirtSpeeds[0]
    if fastest:
        maximumTotalSpeed = 0
        length = len(redShirtSpeeds)
        if fastestRedRider > fastestBlueRider:
            for idx in range(length):
                maximumTotalSpeed += max(
                    redShirtSpeeds[length-1-idx], blueShirtSpeeds[idx])
            return maximumTotalSpeed
        else:
            for idx in range(length):
                maximumTotalSpeed += max(
                    blueShirtSpeeds[length-1-idx], redShirtSpeeds[idx])
            return maximumTotalSpeed
    else:
        minimumTotalSpeed = 0
        length = len(redShirtSpeeds)
        for idx in range(length):
            minimumTotalSpeed += max(redShirtSpeeds[length-1-idx],
                                     blueShirtSpeeds[length-1-idx])
        return minimumTotalSpeed
