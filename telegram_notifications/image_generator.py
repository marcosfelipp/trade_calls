import imgkit


string = "<!DOCTYPE html><html lang=\"pt-br\"><head><link rel=\"stylesheet\" href=\"template.css\"></head><body><div class=\"box\"><img src=\"OIBR3.png\" width=\"100\" height=\"100\">bbabababababb</div></body>"


def generate_html(ativo, tipo, obetivo, entrada, stop_loss):

    with open("template_teste.html", 'w') as f:
        f.write(string)


def generate_image(ativo, tipo, obetivo, entrada, stop_loss):
    options = {
        'format': 'png',
        'crop-h': '200',
        'crop-w': '200',
        'encoding': "UTF-8",
    }
    generate_html(ativo, tipo, obetivo, entrada, stop_loss)

    imgkit.from_file('template_teste.html', 'out.png', options=options)


