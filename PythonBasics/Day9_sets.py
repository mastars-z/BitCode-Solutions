# Enter your code here. Read input from STDIN. Print output to STDOUT
total = int(input())
countries = []
count = 0
for N in range(total):
    inp = input()
    countries.append(inp)
unique_countries = set(countries)
for i in unique_countries:
    count += 1
print(count)
