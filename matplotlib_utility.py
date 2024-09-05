import matplotlib.pyplot as plt

class MatPlotLibUtility():
    @staticmethod
    def plot_images(image_1, image_2,title_1="Orignal",title_2="New Image"):
        plt.figure(figsize=(10,10))
        plt.subplot(1, 2, 1)
        plt.imshow(image_1)
        plt.title(title_1)
        plt.subplot(1, 2, 2)
        plt.imshow(image_2)
        plt.title(title_2)
        plt.show()