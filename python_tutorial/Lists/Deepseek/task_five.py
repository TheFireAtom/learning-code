colors = ["красный", "зелёный", "синий", "жёлтый"]
for color in colors: 
    print("Цвет: ", color)
for i in range(len(colors)):
    print("Индекс: ", i)
for idx, color in enumerate(colors):
    print("Индекс и цвет: ", idx, color)
upper_colors = []
for color in colors:
    upper_colors.append(color.upper())
print(upper_colors)


