
initial = {
    1: [1, 0, 0],
    2: [2, 1, 2],
    3: [2, 1, 0],
}


def getColor(pos):
    color = 0
    for item in initial[pos]:
        if item != 0:
            color = item
    return color


def getSpace(pos):
    space = 0

    for item in initial[pos]:
        if item == 0:
            space = + 1
    return space


def move(move, pos):
    if move == pos:
        return False

    if getSpace(move) == 0:
        return False

    if getSpace(pos) == 0:
        return False

    moveColor = getColor(move)
    endColor = getColor(pos)

    if moveColor != endColor:
        return False

    return True

print(move(1,1))
print(move(1,2))
print(move(1,3))

print(move(2,1))
print(move(2,2))
print(move(2,3))

print(move(3,1))
print(move(2,2))
print(move(1,3))




# import copy
#
# initial = {
#     1: [1, 0, 0],
#     2: [2, 1, 2],
#     3: [2, 1, 0],
# }
#
# def getColor(board, pos):
#     color = 0
#     for item in board[pos]:
#         if item != 0:
#             color = item
#         else:
#             break
#     return color
#
# def getSpace(board, pos):
#     space = 0
#
#     for item in reversed(board[pos]):
#         if item == 0:
#             space =+ 1
#         else:
#             break
#
#     return space
#
# def editBoard(board, endPos, pos):
#     for item, index in enumerate(reversed(board[pos])):
#         if item != 0:
#             color = item
#             board[pos][index] = 0
#
#             break
#
#     for item,index in enumerate(reversed(board[endPos])):
#         if item == 0:
#             board[endPos][index] = color
#
#             break
#
# def move(board, pos, endPos):
#     if endPos == pos:
#         return False
#
#     if getSpace(board, pos) == 3:
#         return False
#
#     if getSpace(board, endPos) == 0:
#         return False
#
#     moveColor = getColor(board, endPos)
#     endColor = getColor(board, pos)
#
#     if moveColor != endColor and endColor != 0:
#         return False
#
#     # hier breakt es
#     editBoard(board, pos, endPos)
#
#     if getSpace(board, pos) != 0:
#         # print(board, endPos, pos)
#         # print(move(newBoard, endPos, pos))
#         state = move(copy.copy(board), endPos, pos)
#
#         if not state:
#             return False
#
#     return True
#
# print(move(initial, 3,1))
# print(move(initial, 1,3))
# print(move(initial, 2,3))
# print(move(initial, 2,2))
# print(move(initial, 3,2))