import numpy as np
from scipy.misc import derivative
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

def fn_plot1d(fn,x_min,x_max,filename):
    # num = np.floor((x_min-x_max)*100)
    x = np.linspace(x_min,x_max)
    f = np.vectorize(fn)
    y = f(x)
    plt.figure()
    plt.plot(x,y)
    plt.title("plot of function: " + fn.__name__) 
    plt.xlabel("x values")
    plt.ylabel(fn.__name__+"(x)")
    plt.xlim(x_min,x_max)
    plt.savefig(filename)

def fn_plot2d(fn,x_min,x_max,y_min,y_max,filename):
    # num = np.floor((x_min-x_max)*100)
    x = np.linspace(x_min,x_max)
    y = np.linspace(y_min,y_max)
    grid_x,grid_y = np.meshgrid(x,y)
    # print(grid_x.shape)
    f = np.vectorize(fn)
    z = f(grid_x,grid_y)
    plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(grid_x,grid_y,z)
    plt.title("plot of function: " + fn.__name__) 
    ax.set_xlabel("x values")
    ax.set_ylabel("y values")
    ax.set_zlabel(fn.__name__+"(x,y)")
    ax.set_xlim(x_min,x_max)
    ax.set_ylim(y_min,y_max)
    plt.savefig(filename)
    # plt.show()

def nth_derivative_plotter(fn,n,xmin,xmax,filename):
    x = np.linspace(xmin,xmax,1000*n)
    f = np.vectorize(lambda x: derivative(fn,x,n=n,dx=1e-6))
    y = f(x)
    plt.figure()
    plt.plot(x,y)
    plt.title(r"$plot~of~"+ r"d^"+str(n)+fn.__name__+r"(x)/dx^"+str(n)+r"$") 
    plt.xlabel("x values")
    plt.ylabel(r"$d^"+str(n)+fn.__name__+r"(x)/dx^"+str(n)+'$')
    plt.xlim(xmin,xmax)
    plt.savefig(filename)

def b(x):
    h = lambda t: np.exp(-1/t**2) if t>0 else 0
    g = lambda t: h(2-t)/(h(2-t)+h(t-1))
    return g(abs(x))

def sinc(x,y):
    z = np.sqrt(x**2 + y**2)
    if z>0:
        return np.sin(z)/z
    else:
        return 1

fn_plot1d(b,-2,2,"fn1plot.png")
fn_plot2d(sinc,-1.5*np.pi,1.5*np.pi,-1.5*np.pi,1.5*np.pi,"fn2plot.png")
nth_derivative_plotter(b,1,-2,2,"bd_1.png")
nth_derivative_plotter(b,2,-2,2,"bd_2.png")