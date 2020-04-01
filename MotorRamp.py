from enum import Enum
from Util import *

class MotorRamp:
    mSetpoint = 0.0  # intended speed from -1 to 1 normalized value
    mMax = 0.0  # highest speed
    mMin = 0.0  # lowest speed
    mRampRate = 0.0  # time in seconds

    mDirection = 0  # 0 = Constant, 1 = Ramp up, 2 = Ramp down
    mLastTimestamp = 0.0  # current time in seconds

    def MotorRamp(self, minValue, maxValue, secondsFromZeroToMax):
        self.mMax = maxValue
        self.mMin = minValue

        if Util.epEquals(secondsFromZeroToMax, 0.0):
            self.mRampRate = maxValue * (1.0 / Util.kCycleTime)
        else:
            self.mRampRate = maxValue / secondsFromZeroToMax

        self.setSetpoint(0.0, 0.0)

    # Takes in the current motor speed and the desired setpoint and will set the motor to the desired state
    def setSetpoint(self, setpoint, motorSpeed):
        self.mSetpoint = Util.limit(setpoint, self.mMin, self.mMax)

        if setpoint > motorSpeed:
            self.mDirection = 1
        elif setpoint < motorSpeed:
            self.mDirection = 2
        else:
            self.mDirection = 0

    # Returns the updated output
    # Need to pass in the current speed of the motor and the current timestamp in seconds
    def update(self, motorSpeed, timestamp):
        output = self.mSetpoint
        if self.mDirection == 1:
            increment = (timestamp - self.mLastTimestamp) * self.mRampRate
            if motorSpeed + increment > self.mSetpoint:
                output = self.mSetpoint
            else:
                output = motorSpeed + increment
        elif self.mDirection == 2:
            decrement = -((timestamp - self.mLastTimestamp) * self.mRampRate)
            if motorSpeed + decrement < self.mSetpoint:
                output = self.mRampRate
            else:
                output = self.mSetpoint + decrement
        elif self.mDirection == 0:
            output = self.mSetpoint
        if Util.epEquals(output, self.mSetpoint):
            self.mDirection = 0

        self.mLastTimestamp = timestamp
        return output

    # Resets the params to default for when turning off the motor and other intermediate tasks
    def reset(self, timestamp):
        self.mSetpoint = 0.0
        self.mDirection = 0
        self.mLastTimestamp = timestamp
