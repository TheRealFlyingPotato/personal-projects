import pprint

EMPTY = "-"
P1 = "X"
P2 = "O"
BOARD_SIZE = 7

class Cell:
  def __init__(self):
    self.val = EMPTY
  def __str__(self):
    return self.val
  def __int__(self):
    if self.val == EMPTY:
      return 0
    if self.val == P1:
      return 1
    return 2


def full_column(col, b):
  for row in b:
    

def initialize_board(s):
  """returns an empty list of lists with the given size"""
  return [[Cell() for x in range(s)] for x in range(s)]

def print_board(b):
  print("")
  for c in range(BOARD_SIZE):

    print (c+1, end=" ")
  print("")
  for row in b:
    for item in row:
      print(item, end=" ")
    print("")


def main():
  board = initialize_board(BOARD_SIZE)
  print_board(board)


main()