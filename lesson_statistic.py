import pandas as pd

data = {
    "набор А" : [85, 90, 95, 100, 105],
    "набор Б" : [70, 80, 95, 110, 120]
}

df = pd.DataFrame(data)

stdA = df["набор А"].std()
stdB = df["набор Б"].std()

print(f"Стандартное отклонение 1 набор - {stdA}")
print(f"Стандартное отклонение 2 набор - {stdB}")
