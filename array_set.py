""" 
Author: Affan Sheikh
Date: 09/10/2014
"""


from t_array import Array

class Set:
    """
        Implements a contiguous implementation of a Set ADT that includes most of the functionality of 
        Python's built-in set type
    """
    
    def __init__(self, iterable = []):
        """
            Return a new Set object whose elements are taken from optional parameter iterable. 
            If iterable is not specified, a new empty set is returned.
            
            Arguments: 
              iterable (optional) - the object whos contents are copied to the set
              
            Returns: A new set object containing elements taken from iterable
        """
        self._array = Array(2)  # initializes a array to a length of two empty slots
        self._length = 0  # sets the length to zero for empty array
        self._cap = 2  # sets the capacity to the size of the array initialized
        for elem in iterable:
            self.add(elem)
                
    def add(self, elem):
        """
            Add element elem to the set.
            
            Arguments:
              elem - the element that should be added to the end of the set
              
            No return value
        """
        if (self._noDuplicate(elem)):  # checking if element is not present in set
            if (self._length == self._cap):  # increase array size if the length matches the capacity
                self._resize()
            self._array[self._length] = elem  # add elements to array
            self._length = self._length + 1  
        
    def remove(self, elem):
        """
            Remove element elem from the set. Raises KeyError if elem is not contained in the set.
            
            Arguments:
              elem - the element that should be removed from the set if it exists
              
            No return value
        """
        if (self._noDuplicate(elem)):  # checking if element is not present in set
            raise KeyError
        else:
            new_Array = Array(self._cap)  # create a array with capacity of internal set array
            for i in range(self._length):  # range through internal array to check for match of elem
                if (self._array[i] == elem):  # if the match is found
                    found_index = i  # stores the index of the element to be removed
                    self._length = self._length - 1  
            for i in range(self._length):  
                if (i < found_index):  # if index is less than the found index copy everything
                    new_Array[i] = self._array[i]  # copy elements to new array
                else:
                    new_Array[i] = self._array[i+1]  # get element from index + 1 to not copy over element that is removed
            self._array = new_Array
            
    def discard(self, elem):
        """
            Remove element elem from the set if it is present.
            
            Arguments:
              elem - the element that is to be discared 
              
            No return value
        """
        if (not self._noDuplicate(elem)):  # checks to see if element is present
            self.remove(elem)  # call remove to to take out the elem
        
    def pop(self):
        """
            Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
        
            No Arguments
            
            Return: The element that is popped from the set
        """
        if (self._length == 0):
            raise KeyError
        else:
            elem = self._array[self._length-1]  # obtain the element from array
            self.remove(elem)  # call remove function to remove the element from array
            return elem
    
    def clear(self):
        """
            Remove all elements from the set.
            
            No Arguments
            
            No return value
        """
        for i in range(self._length): 
            self._array[i] = None  # set every element to None
        self._length = 0  # change the length back to zero
        
    def __contains__(self, x):
        """
            Test x for membership in s.
            
            Arguments:
              x - the variable to be checked to see if it is contained in the set
              
            Return: A boolean indicating whether the element is contained or not
        """
        contains = False  # boolean to keep track of whether element has been found
        for i in range(self._length):
            if (self._array[i] == x):  # if the element is found
                contains = True  
        return contains 
            
    def isdisjoint(self, other):
        """
            Return True if the set has no elements in common with other. Sets are disjoint if and only if
            their intersection is the empty set. Raises a TypeError if other is not a Set instance.
        
            Arguments:
              other - the set that is being compared with self to see if they have no common elements
              
            Return: A boolean that indicates whether the sets have no elements in common
        """
        if (isinstance(other, Set)):  # check if other is of set type
            if ((len(self & other)) == 0):  # checks to see if the intersection of the two sets is empty
                return True  # return true if intersection is empty
            else:    
                return False
        else:
            raise TypeError  # raise error if other is not of set type
    
    def issubset(self, other):
        """
            Will return true if the other set is a subset. Raises a TypeError if other is not a Set instance.
            
            Arguments:
              other - the set that is checked to see if its a subset of self set
            
            Returns: True if other is a subset
        """
        if (isinstance(other, Set)):  # check if other is of set type
            for i in range(self._length):
                if (other._noDuplicate(self._array[i])):  # if the element in self set is not found in other set
                    return False  # other is not subset returns false immediately 
            return True
        else:
            raise TypeError  # raise error if other is not of set type
    
    def __lt__(self, other):
        """
            Test whether the set is a proper subset of other, that is, set <= other and set != other.
            Raises a TypeError if other is not a Set instance
            
            Arguments:
              other - the set that that is used to see if self is proper subset 
              
            Returns: a boolean if the set is a proper subset of other
        """
        if (isinstance(other, Set)):  # check if other is of set type
            if (self._length < len(other)):  # if other set is greater, satisfied the proper condition
                return self.issubset(other)  # call less than equal to see if it is a subset
            else:
                return False  
        else:
            raise TypeError  # raise error if other is not of set type

    def __le__(self, other):
        """
            Test whether every element in the set is in other. Raises a TypeError if other is 
            not a Set instance.
            
            Arguments:
              other - set used to compare with whether all elements in self set are in this set
              
            Returns: A boolean whether every element in set is in other
        """
        return self.issubset(other)  # return the result obtained from calling issubset
        
    def issuperset(self, other):
        """
            Will return true if the other set is a superset.  Raises a TypeError if other is not a Set instance.
            
            Arguments:
              other - set used to compare with self set to see it other is superset
              
            Return: A boolean whether other is a superset
        """
        if (isinstance(other, Set)):  # check if set passed in is type of set
            for i in range(len(other)):  
                if (self._noDuplicate(other._array[i])):  # if the element in other set is not found in self set
                    return False  # return false if if statement is not satisfied
            return True  # return true if false is not returned
        else:
            raise TypeError  # raise error if other is not set
        
    def __gt__(self, other):
        """
            Test whether the set is a proper superset of other, that is, set >= other and set != other. 
            Raises a TypeError if other is not a Set instance.
            
            Arguments:
              other - set used to compare with self set to see if every element in self is in other
            
            Returns: A boolean whether self set is a superset of other
        """
        if (isinstance(other, Set)):  # see if other is of set type
            if (self._length > len(other)):  # see if self set is a proper of other set, must be bigger
                return self.issuperset(other)  # call to super set to see if it is a superset
            else:
                return False
        else:
            raise TypeError  # raise error if other is not of set type
        
    def __ge__(self, other):
        """
            Test whether every element in other is in the set. Raises a TypeError if other is 
            not a Set instance.
            
            Arguments:
              other - set used to compare with self set to see it other is superset
              
            Return: A boolean whether other is a superset
        """
        return self.issuperset(other)  # return the result obtained form issuperset
    
    def union(self, other):
        """
            Return a new set with elements from the set and all others. Raises a TypeError if other 
            is not a Set instance.
            
            Arguments: 
              other - set used alongside self set to create a union set 
              
            Return: A set which contains elements found in both self set and other set
        """
        if (isinstance(other, Set)):  # check if other is of set type
            union_set = Set()
            for elem in self:  # iterate through self set and add items to union set
                union_set.add(elem)
            for elem in other:  # iterate through other set and add items to union set if element is not already in union set
                if union_set._noDuplicate(elem):
                    union_set.add(elem)
            return union_set
        else:
            raise TypeError  # raise error if other is not of set type

    def __or__(self, other):
        """
            Return a new set with elements from the set and all others. Raises a TypeError if other 
            is not a Set instance.
            
            Arguments: 
              other - set used alongside self set to create a union set 
              
            Return: A set which contains all the different elements from other and self set
        """
        return self.union(other)  # return the value obtained from calling union function
                
    def intersection(self, other):
        """
            Return a new set with elements common to the set and all others. Raises a TypeError if 
            other is not a Set instance.
            
            Arguments:
              other - set used alongside self to create a intersection set
        
            Return: A set which contains elements that are only present in both sets 
        """
        if (isinstance(other, Set)):  # check if other is of set type
            intersection_set = Set()
            for elem in self:  # for every element in self set, only add if it is also present in other
                if elem in other:
                    intersection_set.add(elem)  # add element to intersection set
            return intersection_set
        else:
            raise TypeError  # raise Type error if not of set type

    def __and__(self, other):
        """
            Return a new set with elements common to the set and all others. Raises a TypeError if 
            other is not a Set instance.
            
            Arguments:
              other - set used alongside self to create a intersection set
        
            Return: A set which contains elements that are only present in both sets 
        """
        return self.intersection(other)  # return the value obtained when calling intersection function
    
    def difference(self, other):
        """
            Return a new set with elements in the set that are not in the others. Raises a TypeError if 
            other is not a Set instance.
            
            Arguments:
              other - set used to compare whether its elements are contained in self set or not
              
            Returns: A set with elements in the self set but not in others
        """
        if (isinstance(other, Set)):  # check if other is of set type
            sub_set = Set()
            for elem in self:  # add every element from self set that is not in other set to a new set
                if elem not in other:
                    sub_set.add(elem)
            return sub_set
        else:
            raise TypeError  # raise error if other is not of set type
        
    def __sub__(self, other):
        """
            Return a new set with elements in the set that are not in the others. Raises a TypeError if 
            other is not a Set instance.
            
            Arguments:
              other - set used to compare whether its elements are contained in self set or not
              
            Returns: A set with elements in the self set but not in others
        """
        return self.difference(other)  # return the value obtained from calling the difference function
                
    def symmetric_difference(self, other):
        """
            Return a new set with elements in either the set or other but not both. Raises a TypeError
            if other is not a Set instance.
            
            Arguments:
              other - the set used to see if its contents don't belong in self set and self set not in other set
              
            Return: A set containing elements in either self set or other but not both
        """
        if (isinstance(other, Set)):  # if other is of set type
            s_difference = Set()
            for elem in self:  # add every element that is in self set but not in other set
                if elem not in other:
                    s_difference.add(elem)
            for elem in other:  # add every element that is in other set but not in self set
                if elem not in self:
                    s_difference.add(elem)
            return s_difference  
        else:
            raise TypeError  # raise error if other is not of set type
                                
    def __xor__(self, other):
        """
            Return a new set with elements in either the set or other but not both. Raises a TypeError
            if other is not a Set instance.
            
            Arguments:
              other - the set used to see if its contents don't belong in self set and self set not in other set
              
            Return: A set containing elements in either self set or other but not both
        """
        return self.symmetric_difference(other)  # return the value obtained from calling symmetric_difference function
    
    def copy(self):
        """
            Return a new set with a shallow copy of s.
            
            No Arguments
            
            Return: A shallow copy of the set
        """
        return Set(self)
    
    def  __len__(self):
        """
            Return the cardinality of the set.
        
            No Arguments
        
            Return: The length of the set
        """
        return self._length
    
    def  __eq__(self, other):
        """
            Returns true if the set is equal to another set. Two sets are equal if and only if every 
            element of each set is contained in the other (each is a subset of the other). 
            Raises a TypeError if other is not a Set instance.
            
            Arguments:
              other - The set that is used to compare the equality with self set
              
            Return: A boolean indicating whether the sets are equal or not
        """
        equality = False
        if (isinstance(other, Set)):  # it other is of set type
            if (self._length == len(other)):  # sets length must be equal for them to be equal
                if ((self.issubset(other)) & (other.issubset(self))):  # checking if both sets are subsets of each other
                    equality = True  # true only if both are subsets of each other
        return equality
            
    def __str__(self):
        """
            Returns a string of the set
            
            No arguments
            
            Return: The string representation of the set
        """
        setString = ""
        if (self._length == 0):  # if the set is empty make the string represent a empty set
            setString = "set([])"
        else:
            setString = "set(["  # assign the appropriate beginning of the string for a set representation
            for i in range(self._length):  # iterate through the array
                if (i != self._length-1):  # if its not the last element add the element to the string obtained using repr and a comma
                    setString = setString + repr(self._array[i]) + ","
                else:  # add the elements to the string by using repr and the closing brackets
                    setString = setString + repr(self._array[i]) + "])"
        return setString
        
    def __repr__(self):
        """
            Return a string representation of the set.
            
            No arguments
            
            Return - the string representation of the set
        """
        answer = self.__str__()
        return answer  # call string method to return 
    
    def  __iter__(self):
        """
            Return an iterator for the set.
            
            No arguments
            
            Return - The iterator for the set
        """
        for i in range(self._length):
            yield self._array[i]  # use generator approach to iterate through the array

    def _resize(self):
        """
            Resizes the current array by 2 times while copying the contents
            
            No Arguments
            
            No return Value
        """
        self._cap = self._cap * 2  # resize the capacity by 2 times
        new_Array = Array(self._cap)  # make new array with the new capacity
        for i in range(self._length):  # iterate through the length of array and add elements to the new array
            new_Array[i] = self._array[i]
        self._array = new_Array  # reference the internal class array to the new array created

    def _noDuplicate(self, elem):
        """
            Private helper method that returns true adding element to array wont cause duplicates
            
            Arguments:
              elem - the element checked to see if it is contained in the internal array
              
            Return - A boolean value that indicates true if the element is not contained in array
        """
        for i in range(self._length):  # iterate through the internal array
            if (self._array[i] == elem):  # if the element is found, return False
                return False
        return True
