# Eric Smithson

from threading import Thread, Condition
from time import sleep
import random
import Queue


class RandHolder:
    def __init__(self):
        self.rand_num = random.randrange(4, 99999)
        self.available = True
        self.consumed = False

    # sets and gets new number
    def produce_and_get(self):
        self.rand_num = random.randrange(4, 99999)
        self.available = True
        self.consumed = False
        return self.rand_num

    # gets the current rand number and sets the flag to false
    def consume(self):
        # define num as method scope in case a context switch happens
        #  during execution and sets rand_num to something else
        num = self.rand_num
        self.available = False
        self.consumed = True
        return num

    def num_available(self):
        return self.available

    def num_consumed(self):
        return self.consumed


# takes in an integer and produces the next prime number following that integer
def get_next_prime(num):
    flag = False
    while flag == False:
        num += 1
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break

    # if we get here num should equal our next prime
    return num


# counts down from 100. Assignment never specifies whether the counting should stop so I assumed it didn't.
def function1(self):
    i = 100
    while True:
        output_buffer.put("Thread 1: " + str(i))
        i -= 1
        sleep(1)


# I make use of thread locking here to make sure that...
#   RandConsumer never consumes the same number twice
#   RandProducer does not produce a new number until RandConsumer has consumed it's number
# i.e. avoids duplicates and skips
class RandProducer(Thread):
    # prints random number
    def run(self):
        while True:
            condition.acquire()
            # will ignore consumed condition if the RandConsumer thread isn't running
            if not rand_holder.num_consumed() and Thread.isAlive(rand_consumer):
                # print "thread 2 waiting"  # DEBUG
                condition.wait()
                # print "thread 2 released"  # DEBUG
            output_buffer.put("Thread 2: " + str(rand_holder.produce_and_get()))
            condition.notify()
            condition.release()
            sleep(1)


class RandConsumer(Thread):
    # divides random number generated in function2
    def run(self):
        while True:
            condition.acquire()
            if not rand_holder.num_available():
                # print "thread 3 waiting"  # DEBUG
                condition.wait()
                # print "thread 3 released"  # DEBUG
            output_buffer.put("Thread 3: " + str(rand_holder.consume() / 2.5))
            condition.notify()
            condition.release()
            sleep(1)


# prime numbers
def function4(self):
    prime_num = 1
    for i in range(0, 20):
        output_buffer.put("Thread 4: " + str(prime_num))
        prime_num = get_next_prime(prime_num)
        sleep(1)


# if I don't handle output like this I get weird behavior like two threads printing on the same line
def buffer_dump(self):
    while True:
        while not output_buffer.empty():
            print output_buffer.get()
        sleep(.5)


rand_holder = RandHolder()
rand_consumer = RandConsumer()
rand_producer = RandProducer()
condition = Condition()

output_buffer = Queue.Queue()


if __name__ == "__main__":

    random.seed()

    # these threads are not in a producer/consumer relationship with any of the other threads
    thread1 = Thread(target=function1, args=(1, ))
    thread4 = Thread(target=function4, args=(1, ))

    output_thread = Thread(target=buffer_dump, args=(1, ))

    thread1.start()
    output_thread.start()
    sleep(2)

    rand_producer.start()
    sleep(2)

    rand_consumer.start()
    sleep(2)

    thread4.start()