import imgkit


string = "<!DOCTYPE html><html lang=\"pt-br\"><head><link rel=\"stylesheet\" href=\"template.css\"><meta charset=\"utf-8\"></head><body><div class=\"header-box\"><h3>Recomendação de #valor-t</h3></div><div class=\"box\"><div class=\"img-box\"><img src=\"#valor-ativo.png\"></div><div class=\"stock-name\"><h2>#valor-ativo</h2></div><table><tr><th></th><th>Valor</th></tr><tr><td><h3>Entrada: </h3></td><td><h3>#valor-entrada</h3></td></tr><tr><td><h3>Objetivo: </h3></td><td><h3>#valor-objetivo</h3></td></tr><tr><td><h3>Stop: </h3></td><td><h3>#valor-stop</h3></td></tr><tr><td><h3>Lucro: </h3></td><td><h3>#valor-lucro</h3></td></tr></table></div></body>"


def generate_html(ativo, tipo, obetivo, entrada, stop_loss):
    new_str = string.replace("#valor-t", tipo).replace("#valor-entrada", entrada).replace("#valor-objetivo", obetivo).replace("#valor-stop", stop_loss).replace("#valor-ativo", ativo)
    with open("template_teste.html", 'w') as f:
        f.write(new_str)


def generate_image(ativo, tipo, obetivo, entrada, stop_loss):
    options = {
        'format': 'png',
        'crop-h': '500',
        'crop-w': '320',
        'encoding': "UTF-8",
    }
    generate_html(ativo, tipo, obetivo, entrada, stop_loss)

    imgkit.from_file('template_teste.html', 'out.png', options=options)


if __name__ == "__main__":
    generate_image("OIBR3", "Venda", "0,54", "0,50", "0,40")