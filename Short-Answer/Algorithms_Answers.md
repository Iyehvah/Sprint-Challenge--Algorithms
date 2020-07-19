#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This function i think is 0(n) because the loop depends entirely on how many n's it has to loop over
    Answer: 0(n)
b) Since this has 2 nested for loops at first i thought it was going to be exponential but then realized as you go it gets harder for n to be more than j since you are growing j exponentially. so i think its 
    Answer: 0(log n)


c) The first if statement i think is 0(1) since its just checking to see if number of bunnies is 0 and if it is returning 0 which i think is also an 0(1) operation
    The next return statement is saying if bunnies exist then each bunny has 2 ears and so its counting 1 bunnies ears and -1 from bunnies count till its 0. This is a 0(n) operation i think.
    Answer: 0(n)

## Exercise II

I would use a binary search tree here and start at the middle of f and if the egg breaks at f move down the left part of the tree to the next node. If that breaks then move to the left of that node and not the right. If it doesnt break on that node then move up one node and go to the right of that node. If it breaks on that node go back up a node and call it a day. 

If the egg doesnt break at the mid point of f then move down the right part of the tree. Go through till it breaks then move up a node and move to the left of the node of where our egg broke. If it still breaks then move up 2 nodes and call it a day. 


