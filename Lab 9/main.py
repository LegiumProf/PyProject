from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
i = 0
summa = 0
directory = "img"
p = Path("new_img")
if not p.is_dir():
    p.mkdir(parents=True)
pathlist = Path(directory).glob("*.jpg")
for path in pathlist:
    image = Image.open(path)
    enhancer = ImageEnhance.Sharpness(image)
    img = enhancer.enhance(5)
    i += 1
    img.save(Path(p, str(i) + ".jpg"))
with open("123.csv", encoding='utf-8') as file:
    file.readline()
    for s in file:
        print(f"{s.split(',')[0]} - {s.split(',')[1]} шт. за {int(s.split(',')[1]) * int(s.split(',')[2])} руб.")
        summa += int(s.split(',')[1]) * int(s.split(',')[2])
    print(f"Сумма: {summa}")
