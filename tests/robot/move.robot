*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move north from 0,0                 0             0             4                     NORTH         0           1            5    
Move south from 0,0                 0             0             4                     SOUTH         0           0            5
Move east from 0,0                 0             0             7                      EAST          1           0           8
Move west from 0,0                 0             0             270                     WEST        0            0          271
Move north from 0,9                 0             9             12                     NORTH         0           9          13 
Move south from 0,9                 0             9             4                     SOUTH         0           8            5
Move east from 0,9                 0              9            7                      EAST          1           9           8
Move west from 0,9                 0              9             270                     WEST        0            9         271
Move north from 9,9                 9             9             12                     NORTH         9           9          13 
Move south from 9,9                 9             9             4                     SOUTH         9           8            5
Move east from 9,9                 9              9            7                      EAST          9           9           8
Move west from 9,9                 9              9             270                     WEST        8            9         271
Move north from 9,0                 9             0             12                     NORTH         9           1          13 
Move south from 9,0                 9             0             4                     SOUTH         9           0            5
Move east from 9,0                 9              0            7                      EAST          9           0           8
Move west from 9,0                 9              0             270                     WEST        8            0         271
Move north from 5,5                 5             5             12                     NORTH         5           6          13 
Move south from 5,5                 5             5             4                     SOUTH         5           4            5
Move east from 5,5                 5              5            7                      EAST          6           5           8
Move west from 5,5                 5              5             270                     WEST        4            5         271

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}
    