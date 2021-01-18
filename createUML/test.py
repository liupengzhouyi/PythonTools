
# class

line1 : str
line1 = "class a"
line1 = line1[0:6]
print(line1)

# def
line2: str
line2 = "  def p(self, number: int, ii: str) -> int:"
if 'def' in line2 and '(' in line2 and ')' in line2:
    print(line2.find('def '))
    print(line2[line2.index('def ') + 4:line2.index('(')])
    c = line2[line2.find('(self, ') + 7:line2.index(')')]
    s = c.split(', ')
    print(s)
    for i in s:
        i1 = i.split(': ')
        print(i1)
    if '->' in line2:
        print(line2[line2.find('-> ') + 3:len(line2)-1])

# item
line3: str
line3 = "  name: str"
if ':' in line3 and line3.find(':') != len(line3)-1 and line3.find(':', line3.find(':') + 1) == -1:
    print(line3.find(':'))
    print(len(line3))
    list = line3.split(':')
    for i in list:
        print(i.strip())

