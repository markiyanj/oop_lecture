# Create metaclass with inheritance
Animal = type('Animal', (), {'move': 'I can move'})

Predator = type('Predator', (Animal,), {})


class Wolf(Predator):
    pass


if __name__ == '__main__':
    Nick = Wolf()

    print(Nick.move)
