
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the size of the list1:4\n",
      "Enter number at location 0 :\n",
      "1\n",
      "Enter number at location 1 :\n",
      "-6\n",
      "Enter number at location 2 :\n",
      "3\n",
      "Enter number at location 3 :\n",
      "7\n",
      "The sum of items in the list is: 5\n"
     ]
    }
   ],
   "source": [
    "#Python program to sum all the items in a list\n",
    "def sumlist(items):\n",
    "    sumnum=0\n",
    "    for x in items:\n",
    "        sumnum=sumnum+x\n",
    "    return sumnum\n",
    "list1=[]\n",
    "n=int(input(\"Enter the size of the list1:\"))\n",
    "for i in range(0, n):\n",
    "    print(\"Enter number at location\", i, \":\")\n",
    "    item = int(input())\n",
    "    list1.append(item)\n",
    "print(\"The sum of items in the list is:\",sumlist(list1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of empty dictionaries:6\n",
      "The list of empty dictionaries is: [{}, {}, {}, {}, {}, {}]\n"
     ]
    }
   ],
   "source": [
    "#Python program to create a list of empty dictionaries\n",
    "x=int(input(\"Enter the number of empty dictionaries:\"))\n",
    "dict1=[{}]*x\n",
    "print(\"The list of empty dictionaries is:\",str(dict1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the index:1\n",
      "Arudino\n"
     ]
    }
   ],
   "source": [
    "#Python program to access dictionary keys element by index\n",
    "list1={\"Python\":95,\"Arudino\":94,\"Robotics\":96}\n",
    "n=int(input(\"Enter the index:\"))\n",
    "print(list(list1)[n])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "One is referred as 1\n",
      "Two is referred as 2\n",
      "Three is referred as 3\n",
      "Four is referred as 4\n"
     ]
    }
   ],
   "source": [
    "#Python program to iterate over dictionaries using for loops\n",
    "dict1={\"One\":1,\"Two\":2,\"Three\":3,\"Four\":4} \n",
    "for key,val in dict1.items():\n",
    "     print(key,\"is referred as\",dict1[key])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The sum of the dictionary items is: 29\n"
     ]
    }
   ],
   "source": [
    "#Python program to sum all the items in a dictionary\n",
    "dict2={\"data1\":10,\"data2\":-5,\"data3\":24}\n",
    "print(\"The sum of the dictionary items is:\",sum(dict2.values()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}\n"
     ]
    }
   ],
   "source": [
    "#Python script to concatenate following dictionaries to create a new one\n",
    "dict1={1:10,2:20}\n",
    "dict2={3:30,4:40}\n",
    "dict3={5:50,6:60}\n",
    "dict4={}\n",
    "for d in (dict1,dict2,dict3):dict4.update(d)\n",
    "print(dict4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "() it is empty tuple\n",
      "('Shaik', 'Afridi') is a tuple\n"
     ]
    }
   ],
   "source": [
    "#Python program to create a tuple \n",
    "emptytuple=() \n",
    "print(emptytuple,\"it is empty tuple\")\n",
    "tuple1=(\"Shaik\",\"Afridi\") \n",
    "print(tuple1,\"is a tuple\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('String', False, 3.2, 1)\n"
     ]
    }
   ],
   "source": [
    "#Python program to create a tuple with different data types \n",
    "tuple2=(\"String\",False,3.2,1)\n",
    "print(tuple2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "G I T A M\n"
     ]
    }
   ],
   "source": [
    "#Python program to convert a tuple to a string \n",
    "def convertTuple(tup): \n",
    "    str=' '.join(tup) \n",
    "    return str \n",
    "tuple1=(\"G\",\"I\",\"T\",\"A\",\"M\") \n",
    "str=convertTuple(tuple1) \n",
    "print(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(8, 4)\n",
      "(2, 5, 3, 8, 4, 9)\n",
      "(9, 3, 6, 9, 3, 1, 7, 0)\n",
      "(2, 5, 3, 8, 4, 9, 3, 6, 9, 3, 1, 7, 0)\n",
      "(9, 3, 6, 9)\n",
      "('H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D')\n",
      "('L', 'O', 'W', 'R')\n",
      "('H', 'O', 'R')\n",
      "('L', ' ')\n"
     ]
    }
   ],
   "source": [
    "#Python program to slice a tupl\n",
    "tuple1=(2,5,3,8,4,9,3,6,9,3,1,7,0)\n",
    "_slice = tuple1[3:5]\n",
    "print(_slice)\n",
    "_slice = tuple1[:6]\n",
    "print(_slice)\n",
    "_slice = tuple1[5:]\n",
    "print(_slice)\n",
    "_slice = tuple1[:]\n",
    "print(_slice)\n",
    "_slice = tuple1[-8:-4]\n",
    "print(_slice)\n",
    "tuple1=tuple(\"HELLO WORLD\")\n",
    "print(tuple1)\n",
    "_slice = tuple1[2:9:2]\n",
    "print(_slice)\n",
    "_slice = tuple1[::4]\n",
    "print(_slice)\n",
    "_slice = tuple1[9:2:-4]\n",
    "print(_slice)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('S', 'h', 'a', 'i', 'k', 'A', 'F', 'R', 'I', 'D', 'I')\n",
      "Length of the tuple is: 11\n"
     ]
    }
   ],
   "source": [
    "#Python program to find the length of a tuple\n",
    "tuple1=tuple(\"ShaikAFRIDI\")\n",
    "print(tuple1)\n",
    "print(\"Length of the tuple is:\",len(tuple1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'One': 1, 'Two': 2, 'Three': 3}\n"
     ]
    }
   ],
   "source": [
    "#Python program to convert a tuple to a dictionary\n",
    "tuple1=((1,\"One\"),(2,\"Two\"),(3,\"Three\"))\n",
    "print(dict((y, x) for x,y in tuple1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('y', 't', 'i', 's', 'r', 'e', 'v', 'i', 'n', 'U', 'M', 'A', 'T', 'I', 'G')\n",
      "(15, 12, 9, 6, 3)\n"
     ]
    }
   ],
   "source": [
    "#Python program to reverse a tuple \n",
    "x=(\"GITAMUniversity\")\n",
    "y=reversed(x)\n",
    "print(tuple(y))\n",
    "x=(3,6,9,12,15)\n",
    "y=reversed(x)\n",
    "print(tuple(y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'One': [1], 'Two': [2], 'Three': [3], 'Four': [4], 'Five': [5], 'Six': [6]}\n"
     ]
    }
   ],
   "source": [
    "#Python program to convert a list of tuples into a dictionary\n",
    "def Convert(tup,di): \n",
    "    for a,b in tup: \n",
    "        di.setdefault(a,[]).append(b) \n",
    "    return di \n",
    "tuple1=[(\"One\",1),(\"Two\",2),(\"Three\",3),(\"Four\",4),(\"Five\",5),(\"Six\",6)] \n",
    "dict1={} \n",
    "print(Convert(tuple1, dict1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'One': [1], 'Two': [2], 'Three': [3], 'Four': [4], 'Five': [5], 'Six': [6]}\n"
     ]
    }
   ],
   "source": [
    "#Python program to convert a list to a tuple\n",
    "def Convert(tup,di): \n",
    "    for a,b in tup: \n",
    "        di.setdefault(a,[]).append(b) \n",
    "    return di \n",
    "tuple1=[(\"One\",1),(\"Two\",2),(\"Three\",3),(\"Four\",4),(\"Five\",5),(\"Six\",6)] \n",
    "dict1={} \n",
    "print(Convert(tuple1, dict1))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}