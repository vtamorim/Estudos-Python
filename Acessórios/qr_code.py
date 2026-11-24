import qrcode
import qrcode.image.svg

data = 'https://expotec.cnat.ifrn.edu.br/#programacao'

factory = qrcode.image.svg.SvgPathImage

img = qrcode.make(
    data,
    image_factory=factory
)

img.save("MyQrCode.svg")