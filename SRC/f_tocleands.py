def repl(x):
# Function to change a missing value Age in years by column mean
    if x == 1:
        return 33
    else:
        return x



def educ(x):
# Function to categorise education column 
    if x == 1 or x == 2:
        return 1
    elif x == 3:
        return 2
    else:
        return 3


def rescale(x):
# Function to rescale country values from 1 to 5
    if x == 6:
        return 5
    else:
        return x