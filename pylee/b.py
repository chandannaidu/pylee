'''
    chandan The Vehicle object contains a lot of vehicles

    Args:
        arg (str): The arg is used for...
        *args: The variable arguments are used for...
        **kwargs: The keyword arguments are used for...

    Attributes:
        arg (str): This is where we store arg,
'''
class abc:
    def __init__(self,name,age):  #myobject--> self
        self.name = name
        self.age = age
    def myfunction(self):  #abcd --> self
        print('hello '+self.name+' your age isv'+self.age)

class pqr:
    '''
    pqr Returns the reversed String.

    Parameters:
        str1 (str):The string which is to be reversed.

    Returns:
        reverse(str1):The string which gets reversed.   
    '''
    def __init__(self,l1,l2):  #myobject--> self
        if len(l1) == len(l2):
            self.l1 = l1
            self.l2 = l2
        else:
            print("l1 and l2 are not in same size")
    def sum(self):  #abcd --> self
        '''
            chandan chandan Returns the reversed String.

            Parameters:
                str1 (str):The string which is to be reversed.

            Returns:
                reverse(str1):The string which gets reversed.   
        '''
        res = 0
        for i in range(len(self.l1)):
            res+= int(self.l1[i])
        for i in range(len(self.l2)):
            res+= int(self.l2[i])
        return res

def input_var():
    val_list = list()
    number = int(input('enter number '))
    for i in range (number):
        val = input("input "+ str(i) +"number ")
        val_list.append(val)
    return val_list


        ### l1 = input_var()
        ### l2 = input_var()
        ### a = pqr(l1, l2)
        ### a.sum()


def gn(time):
    return print("it's already"+str(time)+"go to sleep gn")

def night(name):
    return print("go to sleep"+name)