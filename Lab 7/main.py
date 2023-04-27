from PIL import Image, ImageDraw, ImageFont
image = Image.open("Postcard.png")
width, height = image.size
new_image = image.crop((100,100,width - 100,height-100))
new_image.save("Cropped_image.png")
new_image.show()

holidays = {"День рождения": "Birthday.png", "Новый год": "New_Year.jpg", "Свадьба": "wedding.png"}
holiday = input("Какой праздник вам нужон? ")
for day in holidays:
    if day == holiday:
        image = Image.open(holidays[day])
        image.show()
name = str(input("Кого вы хотите поздравить? "))
font = ImageFont.truetype('Roboto-Black.ttf', size=40)
width, height = image.size
draw_text = ImageDraw.Draw(image)
draw_text.text(
    (width / 2, height / 2),
    name,
    font = font,
    fill = ("#FFFFFF")
    )
font = ImageFont.truetype('Pacifico-Regular.ttf', size=40)
draw_text = ImageDraw.Draw(image)
draw_text.text(
    (width / 2 - 30, height / 2 + 50),
    ", поздравляю",
    font = font,
    fill = ("#F64141")
    )
image.show()
image.save("congratulation.png")