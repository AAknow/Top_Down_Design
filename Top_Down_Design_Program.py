def main():
    # Instructions
    print("Consider a cannonball shot straight up into the air. " \
          + "Input the initial height \nof the cannon and the velocity of " \
          + "the cannonball. Both must be positive integers\nwith or" \
          + " without decimals\n")
    # Get calculations
    initialValues = getInput()
    maxHeight = calculateMaximumHeight(initialValues[0], initialValues[1])
    totalTime = timeToHitGround(initialValues[0], initialValues[1])
    # Display results
    print("\nThe maximum height of the cannonball is {:,}".format(maxHeight) \
          + " feet")
    print("The ball will hit the ground after approximately " \
          + "{:,}".format(totalTime) + " seconds")
    
def getInput():
    numCheck = 0
    while numCheck == 0:
        h0 = input("What is the initial height of the cannon in feet?\n")
        v0 = input("What is the initial velocity of the cannonball in feet " \
                   + " per second?\n")
        # Check if inputs are non-negative numbers
        try:
            float(h0)
            float(v0)
            if float(h0) >= 0 and float(v0) >= 0:
                numCheck = 1
            else:
                print("Please input valid numbers.\n")
        except ValueError:
            print("Please input valid numbers.\n")
    return float(h0), float(v0)

def heightOfBall(h0, v0, t):
    calculation = round(h0 + (v0 * t) - (16 * (t ** 2)), 2)
    return calculation

def calculateMaximumHeight(h0, v0):
    t = v0/32
    maxHeight = heightOfBall(h0, v0, t)
    return maxHeight

def timeToHitGround(h0, v0):
    t = 0
    while heightOfBall(h0, v0, t) >= 0:
        t = round(t + .1, 1)
    return t

main()
