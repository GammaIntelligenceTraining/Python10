def area(width, height):
    return width * height


def perimeter(width, height):
    return (width + height) * 2


def material_amount(order):
    res_dict = {}
    for key, value in order.items():
        carpet_material = area(value[0], value[1]) * value[2] / 10000
        edge_material = perimeter(value[0], value[1]) * value[2] / 100
        res_dict[key] = [carpet_material, edge_material]
    return res_dict


def print_results(result):
    total_carpet_material = 0
    total_edge_material = 0
    for key, value in result.items():
        print(f'Carpet material for {key}: {value[0]} square meters.')
        print(f'Edge material for {key}: {value[1]} meters.')
        total_carpet_material += value[0]
        total_edge_material += value[1]
    print(f'Total carpet material: {total_carpet_material} square meters.')
    print(f'Total edge material: {total_edge_material} meters.')




products = {'small': [20, 20, 40], 'medium': [40, 60, 35], 'large': [50, 90, 22], 'xlarge':[100, 100, 15]}

print_results(material_amount(products))
