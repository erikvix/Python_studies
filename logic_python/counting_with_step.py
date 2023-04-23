from time import sleep


def counting_with_steps(start, stop, step):
    print("-="*12)
    print(f'Counting from {start} to {stop} in steps of {step}')
    if start < stop:
        count = start
        while count <= stop:
            print(count)
            sleep(0.5)
            count += step
        print('End')
    else:
        count = start
        while count >= stop:
            print(count)
            sleep(0.5)
            count -= step
        print('End')


counting_with_steps(0, 10, 1)
counting_with_steps(10, 0, 2)
start = int(input("Enter the start: "))
stop = int(input("Enter the stop: "))
step = int(input("Enter the step: "))
counting_with_steps(start, stop, step)
