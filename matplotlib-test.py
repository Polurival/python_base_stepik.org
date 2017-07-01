from pylab import *
x = linspace(0,5, 10)
y = x ** 2
print(x)
print(y)

%matplotlib inline

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()