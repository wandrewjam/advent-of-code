# https://adventofcode.com/2019/day/8
import matplotlib.pyplot as plt


def load_file(filename: str) -> list:
    with open(filename) as f:
        image = f.readline()[:-1]
    image = [int(pixel) for pixel in image]
    return image


def count_digits(layer: list, digit: int) -> int:
    count = 0
    for pixel in layer:
        if pixel == digit:
            count += 1
    return count


def main(image: list):
    dimensions = (25, 6)
    layer_size = dimensions[0] * dimensions[1]
    num_layers = len(image) // layer_size
    assert len(image) % layer_size == 0

    layers = [image[(i * layer_size):(i + 1)*layer_size]
              for i in range(num_layers)]

    min_layer = -1
    fewest_zeros = layer_size
    for j, layer in enumerate(layers):
        num_zeros = count_digits(layer, 0)
        if num_zeros < fewest_zeros:
            fewest_zeros = num_zeros
            min_layer = j

    num_ones = count_digits(layers[min_layer], 1)
    num_twos = count_digits(layers[min_layer], 2)
    print(num_ones * num_twos)

    final_image = list()
    for i in range(layer_size):
        j = 0
        while True:
            color = layers[j][i]
            if color != 2:
                break
            j += 1
        final_image.append(color)
    print(final_image)

    # Split into layers
    img = [final_image[i * dimensions[0]: (i+1) * dimensions[0]]
           for i in range(dimensions[1])]

    for row in img:
        print(row)

    plt.imshow(img)
    plt.show()



if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        puzzle_input = load_file(sys.argv[1])
    else:
        puzzle_input = load_file('problem08.in')

    main(puzzle_input)
