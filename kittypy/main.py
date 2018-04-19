import argparse
from kitties import KittyPy

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit", default="20",
                        help="Total kitties to get")
    parser.add_argument("-d", "--debug", action='store_true',
                        help="Count of apps to launch")
    args = parser.parse_args()

    kpy = KittyPy(limit=int(args.limit))

    gen = kpy.get_kitty()

    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
