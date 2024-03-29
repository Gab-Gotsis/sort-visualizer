import pygame
import random
import time

WIDTH, HEIGHT = 2000, 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (50,205,50)
RED = (255,50,50)
COL_WIDTH = 3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sort Algorithm Visualizer")


array = [i for i in range(0, WIDTH // COL_WIDTH)]
random.shuffle(array)

running = True

def bubbleSort(arr):
    #BUBBLESORT
    n = len(array)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
            screen.fill(BLACK)
            for i in range(len(array)):
                if (i == j+1):
                    pygame.draw.rect(screen, RED, (i * COL_WIDTH, HEIGHT - array[i], COL_WIDTH, array[i] * 90))
                else:
                    pygame.draw.rect(screen, WHITE, (i * COL_WIDTH, HEIGHT - array[i], COL_WIDTH, array[i] * 90))

            pygame.display.update()
            pygame.time.Clock().tick(144)
        if (swapped == False):
            print("done")
            print(array)
            time.sleep(3)
            pygame.quit() 

def quickSort(array, left=0, right=len(array) - 1):
    if left >= right:
        return

    pivot = array[right]
    pivotIdx = left

    for i in range(left, right):
        if array[i] < pivot:
            array[i], array[pivotIdx] = array[pivotIdx], array[i]
            pivotIdx += 1
        screen.fill(BLACK)
        for j in range(len(array)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 


            if (j == pivotIdx or j == i):
                pygame.draw.rect(screen, RED, (j * COL_WIDTH, HEIGHT - array[j], COL_WIDTH, array[j] * 90))
            else:
                pygame.draw.rect(screen, WHITE, (j * COL_WIDTH, HEIGHT - array[j], COL_WIDTH, array[j] * 90))

        pygame.display.update()
        pygame.time.Clock().tick(144)

    


    array[right], array[pivotIdx] = array[pivotIdx], array[right]



    quickSort(array, left, pivotIdx - 1)
    quickSort(array, pivotIdx + 1, right)
    return #have to return for recurse to work
    time.sleep(3)
    pygame.quit() 


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #rect works by, first two are the cords for the left point width and height
        screen.fill(BLACK)
        for i in range(len(array)):
                pygame.draw.rect(screen, WHITE, (i * COL_WIDTH, HEIGHT - array[i], COL_WIDTH, array[i]))
        quickSort(array)





# def merge_sort(data, drawData, timeTick):
#     merge_sort_alg(data, 0, len(data)-1, drawData, timeTick)
