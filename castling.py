#==============================================================================
# File Name: 	castling
# Author: 	   Khira Morgan
# Project:	   Senior Design Fall 2017
# 
# Description: This function will analyze a castling move, update the new board 
#		         positions from the old board positions, and return the updated 
#              board.
# Inputs: 
# 	      i.    oldboard = 2D list of old board positions
# 	      ii.   "side" indicates whether the castling occurs on the King or Queen
#              side of the board
#        iii.  "player" indicates whether White or Black made the castling
#              move
# Assumptions:
# 	      i.    In King Side Castling, the two spaces between the King and the
#              Rook are already blank.
#        ii.   In Queen Side Castling, the three spaces between the King and
#              the Rook are already blank.
#==============================================================================

def castling(oldboard, side, player):

    newboard = oldboard[:];
    
    if player == 'W':
        
        if side == 'K':
            newboard[0][4] = 's';
            newboard[0][7] = 's';
            newboard[0][6] = 'k';
            newboard[0][5] = 'r';
            
        elif side == 'Q':
            newboard[0][4] = 's';
            newboard[0][0] = 's';
            newboard[0][2] = 'k';
            newboard[0][3] = 'r';
            
    elif player == 'B':
        
        if side == 'K':
            newboard[7][4] = 's';
            newboard[7][7] = 's';
            newboard[7][6] = 'k';
            newboard[7][5] = 'r';
            
        elif side == 'Q':
            newboard[7][4] = 's';
            newboard[7][0] = 's';
            newboard[7][2] = 'k';
            newboard[7][3] = 'r';

    return newboard;
