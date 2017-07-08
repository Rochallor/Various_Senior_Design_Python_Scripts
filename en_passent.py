#==============================================================================
# File Name: 	en_passent
# Author: 	   Khira Morgan
# Project:	   Senior Design Fall 2017
# 
# Description: This function will analyze the move en passent, update the new 
#		         board positions from the old board positions, and return the 
#              updated board.
# Inputs: 
# 	      i.    oldboard = 2D list of old board positions
# 	      ii.   new_blank is a 1D list with two elements designating the square
#		         that the piece was moved from -- occupied->space
# 	      iii.  new_occupied is a 1D list with two elements designating the 
#              square that the piece was moved to -- space->occupied
#        iv.   pawn_taken indicates the pawn that was taken
#==============================================================================

def en_passent(oldboard, new_blank, new_occupied, pawn_taken):

    newboard = oldboard[:];
    
    temp = oldboard[new_blank[0]][new_blank[1]];

    newboard[new_blank[0]][new_blank[1]] = 's';
    newboard[pawn_taken[0]][pawn_taken[1]] = 's';
    newboard[new_occupied[0]][new_occupied[1]] = temp;
    
    return newboard;
