from PIL import Image

gif = Image.open("C:\\Users\\loge7\\Desktop\photo\\2D Pixel Dungeon Asset Pack\\Dungeon_gif.gif")
while True:
    num = gif.tell()
    gif.save("C:\\Users\\loge7\\Desktop\\photo\\2D Pixel Dungeon Asset Pack\\1" + "\\%d.png"%num)
    gif.seek(num+1)