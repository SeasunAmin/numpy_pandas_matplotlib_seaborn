import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = mpimg.imread('F:\python\Ml_Practice\data_set\coding.png')
plt.imshow(img)
plt.axis("off") #hiding the image axis
plt.colorbar()
plt.show()

