import numpy as np

np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)

class Ocean:
    def __init__(self, x_size, y_size):
        self.ocean = np.zeros((x_size, y_size))

    def __str__(self):
        return str(self.ocean)
    
    def draw_vent(self, x1, y1, x2, y2):
        if x1 == x2:
            if y1 > y2:
                for i in range(0,(y1-y2)+1):
                    self.ocean[x1][y2+i] += 1
            elif y1 == y2:
                self.ocean[x1][y2] += 1
            else:
                for i in range(0,(y2-y1)+1):
                    self.ocean[x1][y1+i] += 1
        elif y1 == y2:
            if x1 > x2:
                for i in range(0,(x1-x2)+1):
                    self.ocean[x2+i][y1] += 1
            elif x1 == x2:
                self.ocean[x1][y2] += 1
            else:
                for i in range(0,(x2-x1)+1):
                    self.ocean[x1+i][y1] += 1
        else: # diagonal
            if y2 > y1 and x2 > x1:
                for i in range(0,(y2-y1)+1):
                    self.ocean[x1+i][y1+i] += 1
            elif y1 > y2 and x1 > x2:
                for i in range(0,(y1-y2)+1):
                    self.ocean[x2+i][y2+i] += 1
            elif y2 > y1 and x1 > x2: 
                for i in range(0,(y2-y1)+1):
                    self.ocean[x1-i][y1+i] += 1
            elif y1 > y2 and x2 > x1:
                for i in range(0,(y1-y2)+1):
                    self.ocean[x1+i][y1-i] += 1

    def count_overlap(self):
        return int(np.count_nonzero(self.ocean >= 2))

ocean = Ocean(1000,1000)

with open("input5.txt", "r") as file:
    lines = file.readlines()
    x_max = 0
    y_max = 0
    for line in lines:
        x1 = int(line.strip().split(" -> ")[0].split(',')[0])
        y1 = int(line.strip().split(" -> ")[0].split(',')[1])

        x2 = int(line.strip().split(" -> ")[1].split(',')[0])
        y2 = int(line.strip().split(" -> ")[1].split(',')[1])

        ocean.draw_vent(int(x1), int(y1), int(x2), int(y2))

print(ocean)
print(ocean.count_overlap())