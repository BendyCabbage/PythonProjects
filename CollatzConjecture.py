#This is currently inaccurate for values that have more than 1000 steps, for example 9780657630, as they exceed the maximum recursion depth 
def main(value, steps, peak):
    if value == 1:
        return [steps, peak]
    else:
        if value % 2 == 0:
            newValue = int(value/2)
            #print(f"{steps}. {newValue}")
            return main(newValue, steps + 1, peak)
        else:
            newValue = int(3*value + 1)
            if newValue > peak:
                peak = newValue
            #print(f"{steps}. {int(3*value + 1)}")
            return main(3*value + 1, steps + 1, peak)

peaks = []
steps = []

for n in range(1, 73):
    output = main(n, 0, n)
    peaks.append(output[1])
    steps.append(output[0])
    #print(f"{n}. Steps: {output[0]}. Peak: {output[1]}")

print(main(63728127,0,63728127))
