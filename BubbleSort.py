import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output

# Was planning to make the numbers in array glow, doesnt work for some reasons
def display_array(arr, index1, index2):
    highlighted_array = ""
    for i, value in enumerate(arr):
        if i == index1:
            highlighted_array += f"\033[93m{value}\033[0m "  # Yellow for smaller index
        elif i == index2:
            highlighted_array += f"\033[91m{value}\033[0m "  # Red for larger index
        else:
            highlighted_array += f"{value} "
    plt.text(0, max(arr) + 5, f'Array: {highlighted_array}', fontsize=12, ha='left', color='black')


def visualize(arr, index1, index2):
    clear_output(wait=True)  # Clear the previous graph
    plt.clf()  # Clear the current figure to avoid residuals

    # Draw all bars in blue
    plt.bar(range(len(arr)), arr, color='blue')

    # Highlight the bars being compared
    if arr[index1] > arr[index2]:
        plt.bar(index1, arr[index1], color='red')    # Larger bar
        plt.bar(index2, arr[index2], color='yellow') # Smaller bar
    else:
        plt.bar(index1, arr[index1], color='yellow') # Smaller bar
        plt.bar(index2, arr[index2], color='red')    # Larger bar

    # Display the current state of the array above the graph
    plt.text(0, max(arr) + 5, f'Array: {arr}', fontsize=12, ha='left', color='black')

    # Display numbers above the bars in black
    for i, value in enumerate(arr):
        plt.text(i, value + 1, str(value), fontsize=12, ha='center', color='black')

    plt.ylim(0, max(arr) + 10)
    plt.show()  # Show the current graph
    plt.pause(5)  # Pause to create an animation effect


def bubble_sort(arr):
    n = len(arr)
    # let's say the array is
    # 100, 50, 60, 70, 10
    # and we want to arrange the number in ascending i.e. smallest to largest
    # we all know the final ans is 10, 50, 60, 70, 100
    # We will compare first element of the array and second which is the index 0 and index 1
    # apparently 100 > 50, we will mark 100 as red bar, 50 as yellow bar,
    # then swap the location of them, making array become 50, 100, 60, 70, 1
    # At the end of first iteration, red bar number i.e. largest number will be at the rightmost
    # Since we have moved the largest to the right, the rightmost is finished,
    # this will make it we now fix the n-1 array and no longer need to fix the nth array
    # Keep doing so until it is completely sorted
    for i in range(n):
        for j in range(0, n-i-1):
            visualize(arr, j, j+1)    
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 

    # It is true that it works but you have to loop it n^2
    # This make the run time O(n^2)

arr = np.random.randint(1, 100, size=10)
plt.ion()  # Enable interactive mode
bubble_sort(arr)
plt.ioff()  # Disable interactive mode
plt.show()
