def getSize(d):
  size = len(d)
  return size

def getPrefix(num , k):
  if getSize(num) < k:
    return num
  else:
    return num[:k]

def getprefixMatched(num, d):
  if d == '4' and d ==num[0]:
    return True
  elif d == num[:2] and d == '37':
    return True
  elif d == '5' and d ==num[0]:
    return True
  elif d == '6' and d ==num[0]:
    return True
  else:
    return False

def getDigit(num):
  index = len(str(num)) - 1
  if index >= 1:
    num = int(num[0]) + int(num[1])
    return str(num)
  else:
    num = num[0]
    return str(num)

def SumOfDoubleEvenPlace(num):
  nums = []
  index = len(num) - 2

  while index >= 0:
    nums.append(num[index])
    index = index - 2
  for i in range(len(nums)):
    nums[i] = int(nums[i])*2
    nums[i] = int(getDigit(str(nums[i])))
  total = sum(nums)
  return total

def sumOfOddPlace(num):
  nums = []
  index = len(num) - 1
  while index >= 0:
    nums.append(num[index])
    index = index - 2
  for i in range(len(nums)):
    nums[i] = int(nums[i])
    
  total = sum(nums)
  return total
  
def isValid(num):
  if getSize(num) >= 13 and getSize(num) <= 16:
    p = getPrefix(num,1)
    p2 = getPrefix(num,2)
    if getprefixMatched(num, p):
      even = SumOfDoubleEvenPlace(num)
      odd = sumOfOddPlace(num)
      total = even + odd
      
      if int(total) % 10 == 0:
        return 'Valid asf'
      else:
        return 'Invalid'
    elif getprefixMatched(num, p2):
      even = SumOfDoubleEvenPlace(num)
      odd = sumOfOddPlace(num)
      total = even + odd
      if total % 10 == 0:
        return 'Valid asf'
      else:
        return 'Invalid'
    else:
      return 'Invalid'
  else:
    return 'Invalid'

        