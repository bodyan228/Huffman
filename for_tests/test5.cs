using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Incapsulation.RationalNumbers
{
    public class Rational
    {
        public readonly int Numerator;
        public readonly int Denominator;
        public double Number;


        public bool IsNan => Number is double.NaN;

        public Rational(int numerator, int denominator = 1)
        {
            Numerator = numerator;
            Denominator = denominator;
            if (Denominator == 0)
            {
                Number = double.NaN;
                return;
            }
            if (Numerator == 0)
            {
                Denominator = 1;
                return;
            }
            Number = (double) Numerator / Denominator;

            int nod = Evclid(Numerator, Denominator);
            if (Denominator < 0 && Numerator < 0 || Denominator > 0 && Numerator > 0)
            {
                Numerator = Math.Abs(Numerator / nod);
                Denominator = Math.Abs(Denominator / nod);
            }
            if (Denominator < 0 && Numerator > 0 || Denominator > 0 && Numerator < 0)
            {
                Numerator = - Math.Abs(Numerator / nod);
                Denominator = Math.Abs(Denominator / nod);
            }
        }

        public static Rational operator +(Rational first, Rational second)
        {
            if (first.IsNan || second.IsNan) return new Rational(1, 0);
            int new_num = first.Numerator*second.Denominator + first.Denominator*second.Numerator;
            int new_den = first.Denominator*second.Denominator;
            int nod = (int)Evclid(new_num, new_den);
            return new Rational (new_num / nod, new_den / nod);
        }

        public static Rational operator -(Rational first, Rational second)
        {
            if (first.IsNan || second.IsNan) return new Rational(1, 0);
            int new_num = first.Numerator * second.Denominator - first.Denominator * second.Numerator;
            int new_den = first.Denominator * second.Denominator;
            int nod = (int)Evclid(new_num, new_den);
            return new Rational(new_num / nod, new_den / nod);
        }

        public static Rational operator *(Rational first, Rational second)
        {
            if(first.IsNan || second.IsNan) return new Rational(1, 0);
            int new_num = first.Numerator * second.Numerator;
            int new_den = first.Denominator * second.Denominator;
            int nod = (int)Evclid(new_num, new_den);
            if (new_den < 0 || new_den < 0)
            {
                return new Rational(-Math.Abs(new_num / nod), Math.Abs(new_den / nod));
            }
            return new Rational(new_num / nod, new_den / nod);

        }

        public static Rational operator /(Rational first, Rational second)
        {
            if (first.IsNan || second.IsNan || second.Numerator == 0) return new Rational(1, 0);
            int new_num = first.Numerator * second.Denominator;
            int new_den = first.Denominator * second.Numerator;
            int nod = (int)Evclid(new_num, new_den);
            if (new_den < 0 || new_den < 0)
            {
                return new Rational(-Math.Abs(new_num / nod), Math.Abs(new_den / nod));
            }
            return new Rational(new_num / nod, new_den / nod);
        }

        public static implicit operator double(Rational number)
        {
            if (number.IsNan) return double.NaN;
            return number.Number;
        }

        public static implicit operator int(Rational number)
        {
            if (number.Numerator % number.Denominator == 0) return (int)number.Number;
            throw new ArgumentException();
        }

        public static implicit operator Rational(int number)
        {
            return new Rational(number);
        }
        public static int Evclid(int num, int den)
        {
            if (num == 0 || den == 0) return Math.Max(num, den);
            num = Math.Abs(num);
            den = Math.Abs(den);
            while (den != num)
            {
                if (den > num) den = den - num;
                else num = num - den;
            }
            return Math.Max(den,num);
        }

        public static 
    }
}
