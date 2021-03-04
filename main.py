from checker import Checker
from network.model import Model

from numba import cuda

print(cuda.gpus)
cuda.select_device(0)

max_size = 20000

def train():
    with tf.device('/GPU:0'):
        model = Model("data.txt", max_size)
        model.load()
        model.train(50)

def test():
    model = Model("data.txt", max_size)
    model.load()
    checker = Checker()
    print(">", end='')
    while True:
        text = input()
        print("Input :", text)
        output = model.test(text)
        print("Output:", output)
        fixed = checker.correct(output[0])
        print("Fixed :", fixed)
        print(">", end='')


if __name__ == '__main__':
    import tensorflow as tf
    print("GPUs Available: ", tf.config.list_physical_devices('GPU'))
    # train()
    test()
