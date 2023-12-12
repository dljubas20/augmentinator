from PIL import Image

def rotateImg(img_path: str, howManyTimes: int):
    for deg in range(0, 360, 360 // howManyTimes):
        img = Image.open(img_path)
        rotated = img.rotate(deg)
        path_parts = img_path.split("/")
        img_name_parts = path_parts[len(path_parts) - 1].split(".")
        rotated.save("new/" + img_name_parts[0] + "@" + str(deg) + "." + img_name_parts[1])