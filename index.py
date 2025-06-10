from Analytics.file1 import Most_sales
from Visualization.file1 import bar_graph

try:

    Result = Most_sales()
    print("Result === ",Result)

    bar_graph(Result)

    print('....Execution Completed.....')



except Exception as e:
    print("Error:",e)
