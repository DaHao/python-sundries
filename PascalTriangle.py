class PascalTriangle:
    def __init__(self, level=1):
        self.level = level if level > 0 else 1
        self.pt = self.create(self.level)

    def create(self, level):
        result = [[1]]
        for idx in range(level-1):
            nowLv, nextLv = result[idx], [] 
            additem = 0
            for item in nowLv:
                nextLv += [additem + item]
                additem = item
            
            result.append(nextLv + [1])
        return result

    def print(self):
        place = self.level * 2 - 1
        middle = self.level - 1

        for idx, nowLv in enumerate(self.pt):
            print('    '*(middle-idx), end='')
            for item in nowLv:
                print('%4s    ' % item, end='')
            print('')

if __name__ == "__main__":
    x = PascalTriangle(15)
    x.print()
