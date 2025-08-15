import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read velocity data and zero out vertical component
vel_df = pd.read_csv('mouse_velocities.csv')
vel_df['velocity_y'] = 0.0

# Time deltas in seconds
timestamps = pd.to_datetime(vel_df['timestamp'])
dt = timestamps.diff().dt.total_seconds().fillna(0).to_numpy()

# Velocity arrays
vx = vel_df['velocity_x'].to_numpy()
vy = vel_df['velocity_y'].to_numpy()

# Integrate iteratively using previous velocity and current dt
positions_x = [0.0]
positions_y = [0.0]
for i in range(1, len(vx)):
    positions_x.append(positions_x[-1] + vx[i-1] * dt[i])
    positions_y.append(positions_y[-1] + vy[i-1] * dt[i])

x = np.array(positions_x)
y = np.array(positions_y)

plt.figure(figsize=(8, 8))
plt.plot(x, y, lw=2, color='navy')
plt.title('Reconstructed Mouse Path')
plt.axis('equal')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.grid(True, alpha=0.3)
plt.savefig('reconstructed_path.png', dpi=300)
plt.close()
