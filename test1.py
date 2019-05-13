import matplotlib
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import numpy as np
import time

w, fi = 2*np.pi, 0
start_time = time.time()
run = True
while run:
    cycle_num = 1
    state = int(input("Enter number of the state\n"))
    if state == 1:
        cycle_num += 1
        A = float(input("Enter the Amplitude value\n"))
        t = np.arange(0.0, 5.0, 0.01)
        s = A * np.sin(w * t + fi)
        fig, ax = plt.subplots()
        ax.plot(t, s)
        ax.set(xlabel='time', ylabel='coords',
               title='Гармонический осциллятор')
        ax.grid()
        collection = collections.BrokenBarHCollection.span_where(
            t, ymin=0, ymax=A, where=s > 0, facecolor='green', alpha=0.5)
        ax.add_collection(collection)

        collection = collections.BrokenBarHCollection.span_where(
            t, ymin=-A, ymax=0, where=s < 0, facecolor='red', alpha=0.5)
        ax.add_collection(collection)
        fig.savefig(str(cycle_num))
        plt.show()
    else:
        run = False
print(str(time.time() - start_time))
