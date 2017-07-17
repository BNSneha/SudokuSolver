from board import Board


def AC3(sample_board):
    queue = sample_board.constraints
    while(queue):
        arc = queue.pop()
        Xi = arc[0]
        Xj = arc[1]
        if(Revise(Xi, Xj, sample_board)):
            if(len(sample_board.variablesDomainDict[Xi]) == 0):
                return False
            neighbours = sample_board.getNeighbours(Xi)
            neighbours.remove(Xj)
            for Xk in neighbours:
                queue.add((Xk, Xi))
    return True


def Revise(Xi, Xj, sample_board):
    revised = False
    # the constraint that must be satisfied is that Xi and Xj must be different
    if(len(sample_board.variablesDomainDict[Xj]) == 1 and
            sample_board.variablesDomainDict[Xj] <=
            sample_board.variablesDomainDict[Xi]):
        sample_board.variablesDomainDict[Xi] \
            = sample_board.variablesDomainDict[
            Xi] - sample_board.variablesDomainDict[Xj]
        revised = True
    return revised


def isSolved(dictionary):
    for key in dictionary.keys():
        if(len(dictionary[key]) != 1):
            return False
    return True


def main():
    sample_board = Board(
        "003020600900305001001806400008102900700000008006708200002609500800203009005010300")
    if(AC3(sample_board)):
        if(isSolved(sample_board.variablesDomainDict)):
            output_board = ''
            for i in range(9):
                for j in range(9):
                    output_board += ', '.join(
                        sample_board.variablesDomainDict[
                            sample_board.letters[i] + str(j + 1)])
            print(output_board)


if __name__ == "__main__":
    main()