# TicTacToeAi
Designed a AI solving agent using minimax and minimax with alpha beta pruning algorithms for the Tic Tac Toe game.

Pseudocode used for both versions can be found here:
Minimax -> https://en.wikipedia.org/wiki/Minimax
Minimax w/ AlphaBeta -> https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning


I have commented the code thouroughly and exlanations of each algorithm can be found at the corresponding Wikipedia page. I will focus on results on number of states counted. 
Git-Hub link: https://github.com/Anton1123/TicTacToeAi
Results:  

-------------
Minimax
-------------

Computer goes first:

Move 1 - states explored 549,945

Move 3 - states explored 7,583 

Move 5 - states explored 173

Move 7 - states explored 9

It beat me... =[

Computer goes second:

Move 2 - states explored 55,504

Move 4 - states explored 932

Move 6 - states explored 50

Move 8 - states explored 4

we tied...

---------------
AlphaBeta
---------------

Computer goes first:

Move 1 - states explored 30,709

Move 3 - states explored 1,640 

Move 5 - states explored 112

Move 7 - states explored 9

It beat me... Again.. =[[ I should get better at tic-tac-toe.


Computer goes second:

Move 2 - states explored 6138

Move 4 - states explored 479

Move 6 - states explored 42

Move 8 - states explored 4

we tied...

------------------------------
Conlusion:       
------------------------------

As expected, if computer goes first, it has a chance to win (which was executed by my poor play). If it goes second, then you will most likely tie. The number of states explored is less when alpha-beta pruning is used, especially in the early stages of the game (Differences in explored states for the first computer move was a factor of near 10). Although not by -very- much, the number of states the computer explores does fluctuate with how the game goes.

