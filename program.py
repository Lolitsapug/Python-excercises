from math import sqrt
import matplotlib.pyplot as plt

f = 1
X1 = -5
X2 = 5

L = []

for Z in range(10,1000):
    x1 = -f*X1/Z
    x2 = -f*X2/Z
    L.append(sqrt((x1-x2)**2))

plt.figure(figsize=(9, 5))
plt.plot(Z, projected_length)
plt.xlabel("Distance Z")
plt.ylabel("Projected segment length (sensor units)")
plt.title("Perspective Projection: Segment Length vs Distance")
plt.grid(True)
plt.tight_layout()
plt.show()
