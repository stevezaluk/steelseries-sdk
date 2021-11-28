import os, sys

def main():
    game = {
        "game":"game1",
        "event":"event1",
        "data": {
            "value":"1"
        }
    }
    print('Game1: ', game)

    game2 = {
        "game":"game2",
        "event":"event2"
    }
    print('Game 2: ', game2)
    game2.update({"data":{"value":1}})
    print('Game 2: ', game2)

if __name__ == '__main__':
    main()
