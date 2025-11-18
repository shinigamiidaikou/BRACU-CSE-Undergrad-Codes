#!/bin/bash

echo "Number 1"
read num1
echo "Number 2"
read num2
echo "Number 3"
read num3

highest=$num1
if [ $num2 -gt $highest ]; then
highest=$num2
fi
if [ $num3 -gt $highest ]; then
highest=$num3
fi

lowest=$num1
if [ $num2 -lt $lowest ]; then
lowest=$num2
fi
if [ $num3 -lt $lowest ]; then
lowest=$num3
fi

echo "The highest is : $highest"
echo "The lowest is : $lowest"
