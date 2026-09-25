inputs = [1, 2, 3, 2.5]

weights1 = [2.1, 3.4, 5.8, -0.5]
weights2 = [1.0, 0.3, -0.8, 0.1]
weights3 = [0.9, -0.4, -0.6, 0.8]

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [weights1[0]*inputs[0] + weights1[1]*inputs[1] + weights1[2]*inputs[2] + bias1,
          weights2[0]*inputs[0] + weights2[1]*inputs[1] + weights2[2]*inputs[2] + bias2,
          weights3[0]*inputs[0] + weights3[1]*inputs[1] + weights3[2]*inputs[2] + bias3]

print(output)