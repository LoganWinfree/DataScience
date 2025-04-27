import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import Sorting

def main():

    sort = Sorting.step_sort()

    arr = np.arange(1, 100, dtype=int)
    arr2 = arr.copy()
    np.random.shuffle(arr2)


    fig, ax = plt.subplots()
    bar = ax.bar(arr, arr2, width=1, color="#000000")
    ax.set_xbound(0,100)
    ax.set_ybound(0,100)
    ax.set_xticks([])
    ax.set_yticks([])

    sort.insertion(arr2)
    
    def update(frame):
        sort.step(arr2)
        for i, bars in enumerate(bar):
            bars.set_height(arr2[i])
        return bar


    ani = animation.FuncAnimation(fig=fig, func=update, frames=len(sort.swap_arr), repeat=False, interval=10)
    plt.show()


if __name__ == "__main__":
    main()