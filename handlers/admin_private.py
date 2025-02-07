from PIL import Image

img = Image.open("images/start_image_2.jpg")  # Открываем JPG
img.save("images/start_image_2.webp", "WEBP")  # Сохраняем в WebP
