from PIL import Image
import cv2
import os

paths = "images"

images = [i for i in os.listdir(paths) if i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg")]

expected_size_collage = [1200, 1200]

expected_size_image = [600, 400]

collage = Image.new("RGBA", expected_size_collage, color=(255,255,255,0))

final_count = 0

for w in range(0, expected_size_collage[0], expected_size_image[0]):
    for h in range(0, expected_size_collage[1], expected_size_image[1]):
        print(final_count)
        filename = images[final_count]
        filepart = paths + f"/{filename}"
        image = Image.open(filepart).convert("RGBA")
        image_width = image.size[0]
        image_height = image.size[1]
        width_factor = image_width / expected_size_image[0]
        height_factor = image_height / expected_size_image[1]
        if width_factor != height_factor:
            size = min(width_factor, height_factor)
            expected_width = round(size * expected_size_image[0])
            expected_height = round(size * expected_size_image[1])
            start_width = round((image_width - expected_width)/2)
            start_height = round((image_height- expected_height)/2)
            end_width = round((image_width - expected_width)/2) + expected_width
            end_height = round((image_height- expected_height)/2) + expected_height
            image = image.crop((start_width, start_height, end_width, end_height))
        image = image.resize(expected_size_image)
        collage.paste(image, (w, h))
        final_count += 1

collage.save("hither.png")