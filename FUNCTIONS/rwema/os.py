import multiprocessing

def increase(counter, barrier):
    old_value = counter.value

    # Wait until both processes have read the counter
    barrier.wait()

    counter.value = old_value + 1

if __name__ == "__main__":
    counter = multiprocessing.Value('i', 0, lock=False)
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
    
  