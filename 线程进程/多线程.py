from threading import Thread


def count(name, day):
    for i in range(100):
        print(f'{name}+{day}:{i}')


class MyThread(Thread):
    def run(self) -> None:
        for i in range(100):
            print(f'count{i}')


if __name__ == '__main__':
    th = Thread(target=count,
                #args=('zsf','23')
                kwargs={'name': '线程1', 'day': '24'}
    )
    # th = MyThread()
    th.start()
    for i in range(100):
        print(f'main{i}')
