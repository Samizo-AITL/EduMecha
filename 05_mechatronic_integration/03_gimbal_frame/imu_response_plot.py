# imu_response_plot.py
# ジンバルIMUログ（角度応答）を可視化するスクリプト

import matplotlib.pyplot as plt

# サンプルログ（時刻[s], IMU角度[deg]）
# 必要に応じてCSVや外部ログに置き換えてください
time_data = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
imu_angle_data = [0.0, 2.4, -1.1, 0.6, -0.2, 0.05]

# 目標値（例：0 deg）
target_value = [0.0 for _ in time_data]

# プロット
plt.figure(figsize=(8, 4))
plt.plot(time_data, imu_angle_data, marker='o', label='IMU Output')
plt.plot(time_data, target_value, linestyle='--', label='Target (0°)')

plt.title("IMU Response Plot (Pitch Axis)")
plt.xlabel("Time [s]")
plt.ylabel("Angle [deg]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("imu_response_plot.png", dpi=300)
plt.show()
