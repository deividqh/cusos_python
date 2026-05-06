import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Semilla
np.random.seed(42)




channels = ['SEO', 'PPC', 'Social Media', 'Email']
# leads = [1250, 980, 750, 1100]
sns.barplot(x=channels, y=leads, palette="viridis" , hue=leads)
plt.title('Leads Generados por Canal')
plt.show()


['lunes', 'martes', 'miercoles', jueves, 'viernes'] 

