# Various_Senior_Design_Python_Scripts
This repository is the location of the python scripts required to run our senior design chess project (minus the image 
processing, and the master.py script).

Explanations:

-boardupdater.py

--STATUS:

PARTIALLY COMPLETE - REQUIRE PIECE LOCATION IN OUTPUT

--INPUT(S):

--- 8x8 list (essentially a python array) of letters B, W, and S to indicate black piece, white piece, and space locations on 
the chessboard

--- example:

board_initial = [['B','B','B','B','B','B','B','B'],['B','B','B','B','B','B','B','B'],['S','S','S','S','S','S','S','S'],
['S','S','S','S','S','S','S','S'],['S','S','S','S','S','S','S','S'],['S','S','S','S','S','S','S','S'],
['W','W','W','W','W','W','W','W'],['W','W','W','W','W','W','W','W']]
 
so that to access the second list, fourth element we would write:

board_initial[1][3] 

Where we have 1 and 3 instead of 2 and 4 because python lists are zero indexed. 
 
--OUTPUT(S):

---General:

The output should indicated the move type by calling a relevent function named after the move type and indicate where the 
white piece moved.

--Explicit:

This will be updated when aforementioned 'relevent functions' have been written
