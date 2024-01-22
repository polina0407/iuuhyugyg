from PIL import Image
from PIL import ImageFilter
with Image.open('SonicTH.png') as pic_original:
    print('Розмір:', pic_original.size)
    print('Формат:', pic_original.format)
    print('Тип:', pic_original.mode)
    pic_original.show()

    pic_bw = pic_original.convert('L')
    pic_bw.save('bw.png')
    pic_bw.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('blured.png')
    pic_blured.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save('up.png')
    pic_up.show()

    pic_rotated = pic_original.rotate(30, expand=True)
    pic_rotated.save('rotated.png')
    pic_rotated.show()
