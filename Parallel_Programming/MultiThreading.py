from threading import Thread

def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))
  
def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))
  
if __name__ == "__main__":
    # creating processes
    p1 = Thread(target=print_square, args=(3, ))
    p2 = Thread(target=print_cube, args=(4, ))
  
    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()
  
    # both processes finished
    print("Done!")

