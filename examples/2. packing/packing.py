import pypdfplot.auto_extract as plt
import pandas as pd

df = pd.read_excel('data.xlsx')
plt.plot(df.x,df.y,'ro-')

with open('title.txt','r') as f:
    title = f.readline()
    xlabel = f.readline()
    ylabel = f.readline()

plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.publish(file_list = ['data.xlsx',
                         'title.txt'],
            cleanup = True,
            )
