import numpy as np

import tkinter as tk


import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)

matplotlib.use("TKAgg")


figure = Figure(figsize=(8, 2), dpi=100)
plot1 = figure.add_subplot(111)


def plot(windows, volumn=None, SEGMENT_MS=None, predicted_starts=None):

    y = [0 for i in range(100)]

    if(volumn != None):
        plot1.clear()
        x_axis = np.arange(len(volumn)) * (SEGMENT_MS / 1000)
        plot1.plot(x_axis, volumn)

        for ms in predicted_starts:
            plot1.axvline(x=(ms / 1000), color="g",
                          linewidth=0.5, linestyle=":")
        plot1.show()
    else:
        plot1.plot(y)

    canvas = FigureCanvasTkAgg(figure, master=windows)

    canvas.draw()
    if volumn == None:
        canvas.get_tk_widget().pack(
            side=tk.BOTTOM,
            fill=tk.BOTH,
            expand=True
        )
    # else:
    #     canvas.flush_events()
    # canvas.update()
    windows.update()

    # toolbar = NavigationToolbar2Tk(canvas, windows)

    # toolbar.update()

    # canvas.get_tk_widget().pack()

    # Add vertical lines for predicted note starts and actual note starts
    # for ms in predicted_starts:
    #     plt.axvline(x=(ms / 1000), color="g", linewidth=0.5, linestyle=":")
