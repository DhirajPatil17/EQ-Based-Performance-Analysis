from cProfile import label
from tokenize import Name
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from .models import visualize
import numpy,math
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error



def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    image_png=buffer.getvalue()
    
    graph=base64.b64encode(image_png)
    
    graph=graph.decode('utf-8')
    
    buffer.close()
    return graph
def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(16,4))
    plt.title('sales of items')
    plt.plot(x,y)
   
    plt.xlabel('Names')
    plt.ylabel('Behaviour')
    plt.tight_layout()
    plt.legend()

    graph=get_graph()
    return graph
def get_scatter_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,3))
    plt.title('sales of items')
    plt.scatter(x,y,alpha=0.5)
    plt.show()
    plt.xlabel('Behavioral')
    plt.ylabel('Marks')
    plt.legend()
    plt.tight_layout()
    graph=get_graph()
    return graph
def get_bar_plot(x1,x2,x3,name):
    barWidth=0.20
    qs=visualize.objects.all()
    values=numpy.arange(len(name))
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Performance of the Students')
    
    value2 = [x + barWidth for x in values]
    value3 = [x + barWidth for x in value2]
    plt.bar(values,x1, color ='r', width = barWidth,
        edgecolor ='grey', label ='Behavioral')
    plt.bar(value2,x2, color ='g', width = barWidth,
        edgecolor ='grey', label ='Attendence')
    plt.bar(value3,x3, color ='b', width = barWidth,
        edgecolor ='grey', label ='Marks')
    plt.show()
    plt.xlabel('Behavioral-Attendence-Marks')
    # plt.xticks([x1 for r in range(len(Name))],
    #     [x.Name for x in qs])
    plt.tight_layout()
    plt.legend()
    graph=get_graph()
    return graph
def get_bar_behaviour(name,behaviour):
    plt.switch_backend('AGG')
    plt.figure(figsize=(16,5))
    plt.title('Behaviour of students')
    plt.bar(name,behaviour,width=0.3)
    plt.xlabel('Name')
    plt.ylabel('behaviour')
    plt.show()
    plt.legend()
    plt.tight_layout()
    graph=get_graph()
    return graph
def get_bar_Marks(name,Marks):
    plt.switch_backend('AGG')
    plt.figure(figsize=(16,5))
    plt.title('Marks of students')
    plt.bar(name,Marks,width=0.3)
    plt.xlabel('Name')
    plt.ylabel('Marks')
    plt.show()
    plt.legend()
    plt.tight_layout()
    graph=get_graph()
    return graph
def get_bar_Attendence(name,attedence):
    plt.switch_backend('AGG')
    plt.figure(figsize=(16,5))
    plt.title('Attendence of students')
    plt.bar(name,attedence,width=0.3)
    plt.xlabel('Name')
    plt.ylabel('Attendence')
    plt.show()
    plt.legend()
    plt.tight_layout()
    graph=get_graph()
    return graph
def get_single_bar(name,behaviour,marks,attendence):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,4))
    plt.title(name+" Over All Performance")
    l1=[behaviour,marks,attendence]
    label=["Behaviour","Marks","Attendence"]
    plt.bar(label,l1,width=0.3)
    plt.show()
    plt.legend()
    plt.tight_layout()
    graph=get_graph()
    return graph
def get_single_line(name,behaviour,marks,attendence):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,4))
    plt.title(name+" Over All Performance")
    l1=[behaviour,marks,attendence]
    label=["Behaviour","Marks","Attendence"]
    plt.plot(label,l1)
    
    plt.show()
    plt.legend()
    plt.tight_layout()
    graph=get_graph()
    return graph





