import numpy as np
import matplotlib.pyplot as plt
#instagram: waaclib
#web: waaclib.com
#x: thebeyazbaret
N = 2500  
c = 0.5   
golden_angle = np.pi * (3 - np.sqrt(5))
n = np.arange(N)
theta = n * golden_angle
radius = c * np.sqrt(n)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
fig = plt.figure(figsize=(10, 12), facecolor='black') 
ax = fig.add_axes([0.05, 0.2, 0.9, 0.75])
ax.set_facecolor('black')
colors = radius
sizes = 15 + radius * 1.5
ax.scatter(x, y, c=colors, s=sizes, cmap='twilight', alpha=0.8, edgecolors='none')
ax.axis('off')
ax.set_aspect('equal')
plt.figtext(0.5, 0.14, "Vogel Model - IG:WAACLIB", 
            ha="center", color="white", fontsize=20, fontname="Arial", fontweight="bold")
plt.figtext(0.5, 0.09, r"$\theta_n = n \times 137.508^{\circ} \quad , \quad r_n = c \sqrt{n}$", 
            ha="center", color="#dddddd", fontsize=16)
plt.figtext(0.5, 0.05, r"$x = r \cos(\theta) \quad , \quad y = r \sin(\theta)$", 
            ha="center", color="#aaaaaa", fontsize=14, style="italic")
print("Poster hazırlanıyor...")
plt.savefig("Vogel_Model_Poster.png", dpi=300, facecolor='black')
plt.show()