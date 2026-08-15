def value(colors):
    result = ""
    color_input = colors[0:2]
    for item in color_input:
        result += color_code(item)
    return int(result)

def color_code(color):
    color_list = get_colors()
    return str(color_list.index(color))


def get_colors():
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
