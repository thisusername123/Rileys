class Util:
    kEpsilon = 1e-12
    kCycleTime = 1e-6

    def limitMain(self, v, minValue, maxValue):
        return min(maxValue, max(minValue, v))

    def limit(self, v, maxMagnitude):
        inverseValue = -maxMagnitude
        return self.limitMain(v, inverseValue, maxMagnitude)

    def epsilonEquals(self, a, b, epsilon):
        return (a - epsilon <= b) and (a + epsilon >= b)

    def epEquals(self, a, b):
        return self.epsilonEquals(a, b, self.kEpsilon)