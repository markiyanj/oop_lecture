class Car:
    def __init__(self, engine):
        self.engine = engine

    def run(self):
        print(f'Running {self.engine.engine_type} engine...')


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type


engine = Engine('electric')
# car = Car(engine)  # If I destroy this Car instance,
# the Engine instance still exists
# car.run()


engine_type = engine.engine_type
print(engine_type)
