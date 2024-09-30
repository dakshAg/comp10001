import matplotlib.pyplot as plt


def visualise_path(path):
    """Visualise the path of the lawnmower"""
    fig, ax = plt.subplots()
    x, y = zip(*path)
    ax.scatter(x, y)

    for i, (x, y) in enumerate(path):
        ax.text(x, y, str(i))

    plt.show()