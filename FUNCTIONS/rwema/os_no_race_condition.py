import multiprocessing

def increase(counter, barrier):
    barrier.wait()     # Let both processes start together
        
    with counter.get_lock():    # Only one process can update the counter at a time
        counter.value += 1


if __name__ == "__main__":
    counter = multiprocessing.Value('i', 0)
    barrier = multiprocessing.Barrier(2)

    p1 = multiprocessing.Process(
        target=increase, args=(counter, barrier)
    )
    p2 = multiprocessing.Process(
        target=increase, args=(counter, barrier)
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final counter:", counter.value)
    print("Expected counter: 2")