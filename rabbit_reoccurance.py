import matplotlib.pyplot as plt 
from matplotlib import style

style.use('fivethirtyeight')
fig=plt.figure()
ax1 = fig.add_subplot(111)

def fibbonacci_loop(number):
    start =1
    new, old = start,start
    for itr in range(number - 1):
        temp = new
        new = old 
        old = old + temp 
    return new 

def rabbits_and_recursion(months, offspring):
    parent, child = 1,1
    for itr in range(months - 1):
        child,parent = parent, parent + child*offspring
    return child 

def rabbit_data_pop(offspring,end_month):
    f = open(f'k{offspring}.txt','w+')
    #f.write('k={}\n'.format(offspring))
    for month in range(end_month):
        pop = rabbits_and_recursion(month, offspring)
        f.write(f'{month},{pop}\n')
    f.close()

def rabbit_graph():
    graph_data = open('k1.txt','r').read()
    lines = graph_data.split('\n')
    xs1 = []
    ys1 = []
    for line in lines:
        if len(line)>1:
            x,y =line.split(',')
            xs1.append(float(x))
            ys1.append(float(y))
    ax1.plot(xs1,ys1)
    #k2
    graph_data = open('k2.txt','r').read()
    lines = graph_data.split('\n')
    xs2 = []
    ys2 = []
    for line in lines:
        if len(line)>1:
            x,y =line.split(',')
            xs2.append(float(x))
            ys2.append(float(y))
    ax1.plot(xs2,ys2, color ='red')
    #k3
    graph_data = open('k3.txt','r').read()
    lines = graph_data.split('\n')
    xs3 = []
    ys3 = []
    for line in lines:
        if len(line)>1:
            x,y =line.split(',')
            xs3.append(float(x))
            ys3.append(float(y))
    ax1.plot(xs3,ys3, color ='green')
    #k4
    graph_data = open('k4.txt','r').read()
    lines = graph_data.split('\n')
    xs4 = []
    ys4 = []
    for line in lines:
        if len(line)>1:
            x,y =line.split(',')
            xs4.append(float(x))
            ys4.append(float(y))
    ax1.plot(xs4,ys4, color ='yellow')
    plt.show()

def main():
    for i in range(1,4):
        rabbit_data_pop(i,15)
    rabbit_graph()
    

if __name__ == '__main__':
    main()




