# A class that functions as a vector. It is a complete data
# structure and is based off an array. It also keeps track
# of the size.

import array


class Vector(array.array):

    def __init__(self, inputType):
        self.elements = array.array(inputType, [])
        self.elementSize = 2  # This is value that stores the size of vector.

    # This returns how many elements are in the vector.
    def length(self):
        return len(self.elements)

    # This checks if a certain value is in the vector.
    def contains(self, inputData):
        if inputData in self.elements:
            return True
        else:
            return False

    # This returns a value at a given index. It will return
    # error if the index is out of range.
    def getItem(self, inputIndex):
        if inputIndex <= (len(self.elements) + 1) and inputIndex >= 0:
            return self.elements[inputIndex]
        elif inputIndex >= (-1 - len(self.elements)) and inputIndex <= 0:
            return self.elements[inputIndex]
        else:
            raise IndexError("The index was out of range.")

    # Sets the given index to the value that is stated.
    # Checks to make sure the index is in range.
    def setItem(self, inputIndex, inputData):
        if inputIndex <= len(self.elements) and inputIndex >= 0:
            self.elements[inputIndex] = inputData
        elif inputIndex >= (-len(self.elements)) and inputIndex <= 0:
            self.elements[inputIndex] = inputData
        else:
            raise IndexError("The index was out of range.")

    # This adds an elements to the end of vector.
    # It increases the size of the vector if needed.
    def append(self, inputData):
        if (len(self.elements)) < self.elementSize:
            self.elements.append(inputData)
        else:
            self.elementSize *= 2
            self.elements.append(inputData)

    # Inserts an element at a given index.
    # It calls a helper function if needed.
    def insert(self, inputIndex, inputData):
        if inputIndex < 0:
            inputIndex = (len(self.elements)) + inputIndex
        if inputIndex > len(self.elements):
            print("The index is out of range.")
        elif inputIndex < 0:
            print("The index was out of range.")
        elif len(self.elements) == 0:
            self.elements.append(inputData)
        elif (len(self.elements)) < self.elementSize:
            self.insertHelper(inputIndex, inputData)
        else:
            self.elementSize *= 2
            self.insertHelper(inputIndex, inputData)

    # This is the helper function for insert() that
    # takes the same parameters and does the tasks.
    def insertHelper(self, inputIndex, inputData):
        tempPlace1 = self.elements[inputIndex]
        tempPlace2 = 0
        for i in range(len(self.elements) + 1):
            if len(self.elements) == 1:
                self.elements[0] = inputData
                self.elements.append(tempPlace1)
            if (i + inputIndex) == (len(self.elements)):
                self.elements.append(tempPlace1)
                break
            if i == 0:
                self.elements[inputIndex] = inputData
                continue
            tempPlace2 = self.elements[i + inputIndex]
            self.elements[i + inputIndex] = tempPlace1
            tempPlace1 = tempPlace2

    # This removes the given index from the vector as long
    # as it was in range.
    def remove(self, inputIndex):
        if inputIndex < len(self.elements):
            tempPlace1 = self.elements[inputIndex]
            del self.elements[inputIndex]
            return tempPlace1
        else:
            print("That index is not valid.")

    # Finds a given element within the vector and
    # returns the index.
    def indexOf(self, inputData):
        for i in range(len(self.elements)):
            if self.elements[i] == inputData:
                return i
        print("The item was not in the vector.")

    # This extends the calling vector with the
    # vector that was input as an argument.
    def extend(self, inputVector):
        for i in range(len(inputVector.elements)):
            self.elements.append(inputVector.elements[i])

    # This creates and returns a vector from the
    # given index as long as they are in range.
    def subVector(self, inputIndexFront, inputIndexEnd):
        if inputIndexFront < 0 or inputIndexEnd < 0:
            print("The index was out of range.")
            return
        elif inputIndexFront < inputIndexEnd:
            if inputIndexFront > len(self.elements) or inputIndexEnd > len(self.elements):
                print("The index was out of range.")
                return
            else:
                tempVector = Vector(self.typecode)
                for i in range(inputIndexFront, inputIndexEnd):
                    tempVector.append(self.elements[i])
                return tempVector
        else:
            print("The index was out of range.")
            return


vector1 = Vector('i')
vector2 = Vector('i')

print(vector1.elements)
print(vector1.elementSize)


vector1.append(2)

vector1.append(5)

vector1.append(10)

vector1.append(40)

vector2.append(100)

vector2.append(300)
vector1.extend(vector2)

print(vector1.elements)
vector3 = vector1.subVector(1, 4)
print(vector3.elements)
# print(vector1.elements)
#vector1.insert(1, 30)
# print(vector1.elements)
#vector1.insert(-2, 400)
# print(vector1.elements)
# print(vector1.remove(3))
# print(vector1.elements)
# print(vector1.indexOf(10))
#vector1.setItem(1, 100)
# print(vector1.elements)
# print(vector1.length())
# print(vector1.contains(5))
# print(vector1.contains(100))
# print(vector1.getItem(1))
# print(vector1.getItem(3))
