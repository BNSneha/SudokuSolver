from board import Board
import copy


def isComplete(assignment, variablesDomainDict):
    if(len(assignment) == 0):
        return False
    for key in variablesDomainDict.keys():
        if key not in assignment.keys():
            return False
    return True


# pick a variable that has not yet been assigned and has the least number
# of choices in its domain
# to do this, sort unAssignedDict by len of domain i.e. by len of its values
# and pick the first value
def minimumRemainingValue(variablesDomainDict, assignment):
    unAssignedDict = {
        k: v for k, v in variablesDomainDict.items()
        if k not in assignment.keys()}
    sorted_List_of_UnAssignedDict = sorted(
        unAssignedDict, key=lambda k: len(unAssignedDict[k]))
    return sorted_List_of_UnAssignedDict[0]


# get neighbours of var
# remove 'value' from the domains of neighbours
# if any of their domains becomes empty return failure
# else collect them in the inference dictionary and return it
def forwardChecking(var, value, variablesDomainDict, sample_board):
    inferences = {}
    neighbours = sample_board.getNeighbours(var)
    for neighbour in neighbours:
        temp = variablesDomainDict[neighbour]
        temp = temp - set(value)
        if(len(temp) == 0):
            return False
        inferences[neighbour] = set(temp)
    return inferences


# assignment is a dictionary with 1:1 relationship between variables and values
def backTrack_search(sample_board):
    assignment = {k: v for k,
                  v in sample_board.variablesDomainDict.items() if len(v) == 1}
    return backTrack(sample_board.variablesDomainDict,
                     assignment, sample_board)


def backTrack(variablesDomainDict, assignment, sample_board):
    if(isComplete(assignment, variablesDomainDict)):
        return assignment
    var = minimumRemainingValue(variablesDomainDict, assignment)
    for value in variablesDomainDict[var]:
        assignment[var] = set(value)
        inferences = forwardChecking(
            var, value, variablesDomainDict, sample_board)
        variablesDomainDictCopy = copy.deepcopy(variablesDomainDict)
        if isinstance(inferences, dict):
            variablesDomainDictCopy.update(inferences)
            result = backTrack(variablesDomainDictCopy,
                               assignment, sample_board)
            if isinstance(result, dict):
                return result
        assignment.pop(var)
    return False


def main():
    sample_board = Board(
        "080706000467009000000000040004097000701000084090000020000002000029070000000350006")
    answer = backTrack_search(sample_board)
    output_board = ''
    for i in range(9):
        for j in range(9):
            output_board += ', '.join(
                answer[sample_board.letters[i] + str(j + 1)])
    print(output_board)


if __name__ == "__main__":
    main()