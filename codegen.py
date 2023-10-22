class Indent:
    def __init__(self, out, symbol='\t'):
        self.out = out
        self.symbol = symbol
        self.indent = 0

    def parse(self, line):
        indent = self.indent if line else 0
        self.indent += line.count('{') - line.count('}')
        indent = min(self.indent, indent)
        return f'{indent*self.symbol}{line}'

    def write(self, arg):
        return self.out.write('\n'.join(self.parse(line) for line in arg.split('\n')))

    def flush(self):
        return self.out.flush()


import sys

sys.stdout = Indent(open('calc.c', 'w'))


maxval = 1000
print('#include <stdio.h>')
print('int main() {')
print('int value;')
print('scanf("%d", &value);')
for i in range(maxval):
    print('if (value == %d) {' % i)
    print('scanf("%*[ \\n]");')
    print('scanf("%c", (char*) &value);')
    for c in '+-*/':
        print('if ((char) value == \'%c\') {' % c)
        print('scanf("%d", &value);')
        for j in range(maxval):
            line = ' '.join(map(str, (i, c, j)))
            try:
                res = int(eval(line))
            except ZeroDivisionError:
                res = 'nan'
            print('if (value == %d) {' % j)
            print('printf("%s = %s\\n");' % (line, res))
            print('return 0;')
            print('}')
        print('*(volatile int*)NULL;')
        print('}')
    print('*(volatile int*)NULL;')
    print('}')
print('*(volatile int*)NULL;')
print('}')
