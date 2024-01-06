import matplotlib.pyplot as mapy

# MINE.

mapy.grid(True, "both", drawstyle = "steps-mid", fillstyle = "full", markevery = 0.5, linestyle = "-.")
mapy.tick_params(axis = "both", which = "both", width = 0.1, length = 0.1)
x = [i for i in range(-10, 10)]
y1 = [i ** 2 for i in x]
y2 = [i ** 2 + i for i in x]
y3 = [i ** 2 + i + 1 for i in x]
# y4 = [i ** 2 + 5 * i + 1 for i in x]
# y5 = [i ** 2 - i + 1 for i in x]
# y6 = [i ** 2 + i - 1 for i in x]
# y7 = [((i ** 3) / 3) - ((i ** 2) / 2) - (2 * i) + (1 / 3) for i in range(-10, 10, 2)]
mapy.plot(x, y1, "o-r")
# mapy.annotate("i ** 2", xy = (x[0], y1[0]), xytext = (0, 5), arrowprops = dict(facecolor = 'black', shrink = 0.05))
mapy.plot(x, y2, "^-g")
# mapy.annotate("i ** 2 + i", xy = (x[0], y2[0]), xytext = (0, 6), arrowprops = dict(facecolor = 'black', shrink = 0.05))
mapy.plot(x, y3, "s-b")
# mapy.annotate("i ** 2 + i + 1", xy = (x[0], y3[0]), xytext = (0, 7), arrowprops = dict(facecolor = 'black', shrink = 0.05))
# mapy.plot(x, y4, 'p-c')
# mapy.plot(x, y5, 'h-m')
# mapy.plot(x, y6, '8-y')
# mapy.plot(x, y7, 'x-k')
mapy.show()
