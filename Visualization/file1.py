import matplotlib.pyplot as plt

x_axis = []
y_axis = []
def bar_graph(table):
    for i in table:
        x_axis.append(i[0])
        y_axis.append(i[1])

    plt.figure(figsize=(20, 10))
    plt.bar(x_axis,y_axis)
    plt.xlabel('Product Name')
    plt.ylabel('Quantity')
    plt.title('Top 10 Products with most sales')
    plt.savefig('/home/nitha/PycharmProjects/PythonProject/Bigdata91/hive_project/Result/Analytics_1/Most_sales.png')
