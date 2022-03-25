from multiprocessing import Process


def count(name='a', day=2):
    for i in range(100):
        print(f'{name}+{day}:{i}')


if __name__ == '__main__':
    p = Process(target=count,args=('aaa',4))
    p2 = Process(target=count,args=('bbb',5))

    p.start()
    p2.start()
