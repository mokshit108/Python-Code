'''nums = [7,8,9,5]
for i in nums:
     print(i)
     
print(next(it)
'''
"""it = iter(nums)

print(it.__next__())

for i in nums:
  print(i)
  """
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
         val=self.num
         self.num +=1
         return val
        else:
            raise StopIteration

value = TopTen()
print(next(value))
for i in value:
  print(i)





