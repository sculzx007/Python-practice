import urllib.request as req

respone = req.urlopen("http://placekitten.com/g/1920/1080")

cat_image = respone.read()

with open("cat_image.jpg","wb") as image:
    image.write(cat_image)

html = respone.read().decode("utf-8")

print(html)
