from task5 import is_even


class Solution:
    prime_numbers = [1, 2, 3]   # a list of prime numbers that are identified by a class instances so far
    max_number = 3              # a number indicating a maximum number until which `prime_numbers` are taken

    def __init__(self, number: int):
        self.number = number # a number until which we need to get the prime numbers
    

    def find_closest_less_prime(self, number: int) -> bool:
        """ Binary search implementation for prime numbers' list. 
            Determines the max number in a list `lst` which is not greater than `number`.
            Returns its position.
        """
        lst = self.prime_numbers
        left = 0                # pointer to the most left element in a current viewport
        right = len(lst) - 1    # pointer to the most rigth element in a current viewport

        while left <= right:
            left_flag = False
            mid = (left + right) // 2

            if lst[mid] > number:
                right = mid - 1
                left_flag = True
            elif lst[mid] < number:
                left = mid + 1
            else:
                return mid
        mid = mid - 1 if left_flag else mid

        return mid


    def is_prime(self, number: int) -> bool:
        """ Function which takes an integer as its only argument and 
            returns a boolean representing whether this `number` is prime.
        """
        if number > 0 and number < 4:
            return True

        for i in range(2, number):
            if number % i == 0:
                return False

        return True


    def find_primes(cls):
        """ Function which takes a number as its argument. Generates and
            Returns the list of all prime numbers starting from 1 until that number.
        """
        number = cls.number
        if number > cls.max_number:
            # primes = cls.prime_numbers
            for i in range(cls.max_number, number):
                if cls.is_prime(i):
                    cls.prime_numbers.append(i)

            cls.max_number = number

            return cls.prime_numbers

        elif number < cls.max_number:
            max_pos = cls.find_closest_less_prime(number)
            return cls.prime_numbers[:max_pos+1]
            
        else:
            max_pos = cls.prime_numbers.index(number)
            return cls.prime_numbers[:max_pos]
        

    def goldbach_conjecture(self):
        """ Function that accepts an even `number` and 
            returns the two prime numbers which, when summing, give the provided `number`.
        """

        if is_even(self.number):
            primes = self.find_primes()
            left = 0
            right = len(primes) - 1

            while True:
                if primes[left] + primes[right] < self.number:
                    left += 1
                elif primes[left] + primes[right] > self.number:
                    right -= 1
                else:
                    return primes[left], primes[right]
        
        return None   
        

if __name__ == "__main__":
    s = Solution(199452)
    print(s.goldbach_conjecture())

