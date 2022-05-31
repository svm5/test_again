from PIL import Image, ImageDraw


new_img = Image.new("RGB", (950, 300), (255, 255, 255))

draw = ImageDraw.Draw(new_img)
draw.pieslice((50, 50, 250, 250), start=30, end=330, fill='#39E639')
draw.line((300, 50, 300, 250), fill='#33CCCC', width=10)
draw.arc((275, 50, 400, 150), start=180, end=120, fill='#33CCCC', width=10)
draw.arc((275, 150, 400, 250), start=230, end=150, fill='#33CCCC', width=10)

draw.line((450, 50, 450, 250), fill='#FF4040', width=13)
draw.line((425, 50, 550, 50), fill='#FF4040', width=13)
draw.line((450, 150, 550, 150), fill='#FF4040', width=13)
draw.line((444, 250, 550, 250), fill='#FF4040', width=13)
draw.line((550, 130, 550, 170), fill='#FF4040', width=13)
draw.arc((525, 25, 575, 75), start=0, end=180, fill='#FF4040', width=13)
draw.arc((525, 225, 575, 275), start=180, end=0, fill='#FF4040', width=13)
draw.line((675, 70, 675, 250), fill='#FF4000', width=13)
draw.line((620, 80, 730, 50), fill='#FF4000', width=13)
draw.polygon(((800, 50), (850, 250), (750, 250)), "green")
draw.polygon(((800, 80), (825, 250), (775, 250)), "white")
draw.line((780, 200, 830, 200), fill="green", width=13)
new_img.save("name.png")
# print("Ok, end")
