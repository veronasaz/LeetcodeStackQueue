'''Maximum Frequency Stack'''

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.groups = {}
        self.maxFreq = 0

    # def __str__(self) -> str:
    #     return f'The stack is {self.groups}'

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
        if self.freq[val] > self.maxFreq:
            self.maxFreq = self.freq[val]
        if self.freq[val] not in self.groups:
            self.groups[self.freq[val]] = []
        self.groups[self.freq[val]].append(val)

    def pop(self) -> int:
        first = self.groups[self.maxFreq].pop()
        self.freq[first] -= 1
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1 
        return first

freqStack = FreqStack()
freqStack.push(5) #The stack is [5]
freqStack.push(7) #The stack is [5,7]
freqStack.push(5) #The stack is [5,7,5]
freqStack.push(7) #The stack is [5,7,5,7]
freqStack.push(4) #The stack is [5,7,5,7,4]
freqStack.push(5) #The stack is [5,7,5,7,4,5]
print(freqStack.pop()) #return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4]
print(freqStack.pop()) #return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4]
print(freqStack.pop()) #return 5, as 5 is the most frequent. The stack becomes [5,7,4]
print(freqStack.pop()) #return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7]
print(freqStack)
