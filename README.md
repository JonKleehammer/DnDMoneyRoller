# DnDMoneyRoller
## Personal Python Program by Jon Kleehammer
### Problem
I like to have the magic items picked out ahead of time in a pool, typically randomly generated then curated. However the actual coins/currency accompanying those items I don't have prepared ahead of time. 

Using available generators online they were able to create the loot, but splitting the loot in a quick way was impossible. They would often follow too closely to the DMG leading to results like "1700 copper, 900 silver, 50 gold" which was meaningless. 

### My Solution
My program rolls the coins according to the DMG similar to other generators, but it also adds on the value of the gems/art objects. With the total coin value it splits the total up according to the number of players specified (defaults to 5). After splitting up the currency it converts simplifies it according to my money simplification method.

#### The money simplification
I have simplified the money into what I consider to be the most pleasing format.

Example: *50pp 391gp 6sp*

We'll only ever use 1 digit of copper, as 10 copper = 1 silver
We'll only ever use 1 digit of silver, as 10 silver = 1 gold
We want to only have 3 digits of gold, but only below 500 gold.
Anything above 500 gold we will convert to platinum in increments of 50 (50 platinum = 500 gold) until we are below 500 gold

### The Inclusion of gems and art objects
One of my players likes accepting some of his coin value in gems or art objects. I included the description of the art objects according to the DMG. He convert coins from his loot to the specified gem/art object.

### Running The Program
You can run the program yourself by downloading the .py file yourself and use a command such as
`python MoneyRoller.py`

#### You may pass in 2 arguments
The first argument is the choice of treasure hoard [0-3]:

Choice | Hoard CR
--- | ---
0 | 0-4
1 | 5-10
2 | 11-16
3 | 17+

The Second arument should be the number of players the loot is being split between [>0]
If you don't pass in any arguments the defaults will be used (1, 5)

Here's what it would look like if you ran it with arguments (a CR 11-16 treasure split between 4 players)
`python MoneyRoller.py 2 4`



### Example Output
```
Grand Total of: 400pp 458gp including 11 (50gp) Bloodstone (opaque dark gray with red flecks)

Split evenly between 5 players:

50pp 391gp 6sp
```
