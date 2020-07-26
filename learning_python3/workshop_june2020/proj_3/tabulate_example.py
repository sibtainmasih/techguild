"""
This module has tabulate example
"""
from tabulate import tabulate

a = int(input("Enter a number: "))
X = 10
Y = 20
answer = a + X + Y
table = [
    ["Sun", 696000, 1989100000],
    ["Earth", 6371, 5973.6],
    ["Moon", 1737, 73.5],
    ["Mars", 3390, 641.85],
]
print(tabulate(table))
