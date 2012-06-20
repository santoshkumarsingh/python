using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DataStructure
{
    public static class Extensions
    {

        public static IEnumerable<long> Fibonacci()
        {
            long a = 1;
            long b = 1;
            yield return a;
            while (true)
            {

                long temp;
                temp = b;
                b = a;
                a = a + temp;
                yield return a;
            }
        }
        
        public static int Bin(int number)
        {
            string bin = string.Empty;
            if (number == 0)
                return 0;
            else
            {
                while (number>0)
                {
                    bin = (number % 2).ToString() + bin;
                    number = number / 2;

                }

            }
            return Convert.ToInt32(bin);

        }

        public static long Factorial(int num)
        {
           
            long fact = 1;
            for (int i = 1; i <= num; i++)
            {
                fact = fact * i;
            }
            return fact;

        }

        public static bool IsPalindrome(string name)
        {
            if (name.Length == 1)
                return true;
            else if (name[0] != name[name.Length - 1])
                return false;
            else
                return IsPalindrome(name.Substring(1, name.Length - 2));
        }

        public static string CeaserCipher(string plainText,int key)
        {
            string cipherText = string.Empty;
            foreach (var item in plainText.ToLower())
            {
                if (Char.IsWhiteSpace(item))
                    cipherText += item;
                else if (item < 'z')
                    cipherText += (char)(item + key);
                else
                    cipherText += (char)(item + key -26);
            }
            return cipherText;
        }

        public static string XOREncrypt(string plainText)
        {
            StringBuilder sb = new StringBuilder();
            int key = 25;
            foreach (var item in plainText)
            {
                sb.Append((char)((int)item ^ key));
            }
            return sb.ToString();
        }

        public static string XORDecrypt(string plainText)
        {
            StringBuilder sb = new StringBuilder();
            int key = 25;
            foreach (var item in plainText)
            {
                sb.Append((char)((int)item ^ key));
            }
            return sb.ToString();
        }

        public static long Power(int number, int power)
        {
            if (power == 0)
                return 1;
            else
                return number * Power(number, power - 1);

        }

        private static bool IsPrime(int number)
        {
            bool IsPrime = true;
            if (number == 2)
                IsPrime = true;
            else
            {
                for (int i = 2; i < number; i++)
                {
                    if (number % i == 0)
                        IsPrime = false;
                }
            }
            return IsPrime;
        }

        public static IEnumerable<int> Primes(int upto)
        {
            return Enumerable.Range(2, upto)
                   .Where(x => IsPrime(x))
                   .Select(y => y);

        }

        public static IEnumerable<string> Permutations(string input)
        {
            List<string> result = new List<string>();
            if (string.IsNullOrEmpty(input))
            {
                yield return string.Empty;
            }
            else
            {
                for (int i = 0; i < input.Count(); i++)
                {
                    foreach (string permutation in Permutations(input.Substring(0, i) + input.Substring(i + 1)))
                    {
                        yield return input[i] + permutation;
                    }
                }
            }
        }



    }
}
