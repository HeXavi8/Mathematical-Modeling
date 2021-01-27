#The situation and possibility of translation are showed in MC.jpg

n = 5  # Calculate the situation after 5 minutes or hours or days or months or years
v = (1, 0, 0, 0)  # the situation at 0 minutes or hours or days or months or years
i = 0  # Our calculation begin at i minutes or hours or days or months or years

print('the possibility of each state:(state0,state1,state2,state3)')
while i < n:
    v = (
        0.5 * v[1] + 0.5 * v[2],#for state0
        0.5 * v[0],#for state1
        0.5 * v[0],#for state2
        0.5 * v[1] + 0.5 * v[2] + v[3]#for state3
    )
    i = i + 1
    print('v' + str(i) + ': ' + str(v))
