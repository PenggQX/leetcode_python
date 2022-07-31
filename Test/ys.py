import imageio
from PIL import Image, ImageSequence

image_list = []

im = Image.open('a.gif')

if __name__ == '__main__':

    i = 1
    for frame in ImageSequence.Iterator(im):
        i += 1
        if i % 8 != 0:
            continue

        frame = frame.convert('RGB', colors=128)
        # frame.save('press.jpg', quality=1)
        image_list.append(frame)
        # image_list.append(imageio.imread('press.jpg'))

    duration = (im.info)['duration'] / 1000
    print(duration, i)

    imageio.mimsave('c001.gif', image_list, duration=duration * 3.5)


