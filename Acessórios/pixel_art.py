from PIL import Image
def converter_pixel_art(image_path, pixel = 80, pallet = 16):
    image=  Image.open(image_path)
    peq_image = image.resize(
        (image.width // pixel, image.height // pixel),
        resample=Image.NEAREST
    )



    peq_image = peq_image.convert("P", palette=Image.ADAPTIVE, colors=pallet)


    pixel = peq_image.resize(image.size, resample=Image.NEAREST)

    return pixel

#Coloque o path da imagem que deseja pixelizar
filename = ""
img_pixel = converter_pixel_art(filename, pixel=10, pallet=16)
#Talvez seja preciso mudar o parâmetro "pixel" do img_pixel  de acordo com a resolução da imagem
# Aumentar caso queira pixelizar mais, Diminuir caso queira menos pixelizado
img_pixel.show()