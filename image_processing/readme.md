##### Image processing
```python
from PIL import Image, ImageFilter

img = Image.open("./ab.jpg")
print(img.format)
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

smooth_img = img.filter((ImageFilter.SMOOTH))
smooth_img.save("smooth.png", "png")

sharpen = img.filter((ImageFilter.SHARPEN))
sharpen.save("smooth.png", "png")

grey_scale = img.convert('L')
grey_scale.save("grey.png", "png")
# print(dir(img))
```

---

#### Show images
```python
from PIL import Image, ImageFilter

img = Image.open("./ab.jpg")

show_img = img.filter(ImageFilter.DETAIL)
show_img.show("my_png")
```

---

##### Rotate images
```python
from PIL import Image, ImageFilter

img = Image.open("./ab.jpg")

rotate_img = img.filter(ImageFilter.DETAIL)
crooked = rotate_img.rotate(90)
crooked.save("rotate_imge.png", "png")

```

---

##### Resize images
```python
from PIL import Image, ImageFilter

img = Image.open("./ab.jpg")

rotate_img = img.filter(ImageFilter.DETAIL)
resize = rotate_img.resize((300,300))
resize.save("resize.png", "png")

```


---

##### Crop images
```python
from PIL import Image, ImageFilter

img = Image.open("./ab.jpg")

filtered_image = img.convert('L')
box = (100,100,400,400)
region = filtered_image.crop(box)
region.save("cropped_image.png", "png")
 
```


#### thumbnail
```python
from PIL import Image, ImageFilter

img = Image.open("./ab.jpg")
img.thumbnail((400,400))
img.save("thumbnail.jpg")


```