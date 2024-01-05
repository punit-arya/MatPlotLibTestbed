import matplotlib.pyplot as mapy
import inspect
import pandas
import numpy as np
import matplotlib

# TUTORIALS.

# fig = mapy.figure()  # an empty figure with no axes
# fig.suptitle('No axes on this figure')  # Add a title so we know which it is
# fig, ax_lst = mapy.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# mapy.show()

# myDF = pandas.DataFrame(np.random.rand(4, 5), columns = list("abcde"))
# myNPArray = myDF.values
# print("type(myDF):", type(myDF))
# print("type(myNPArray):", type(myNPArray))

# myNPMatrix = np.matrix([[1, 2], [3, 4]])
# myNPArray = np.asarray(myNPMatrix)
# print("type(myDF):", type(myNPMatrix))
# print("type(myNPArray):", type(myNPArray))

# x = np.linspace(-1, 1, 100)
# mapy.plot(x, x, label = 'linear')
# mapy.plot(x, x ** 2, label = 'quadratic')
# mapy.plot(x, x ** 3, label = 'cubic')
#
# mapy.plot(x, (x - 1) ** 2, label = "horizontal right shift")
# mapy.plot(x, (x + 1) ** 2, label = "horizontal left shift")
#
# mapy.plot(x, x ** 2 - 1, label = "vertical down shift")
# mapy.plot(x, x ** 2 + 1, label = "vertical up shift")
#
# mapy.plot(x, (2 * x) ** 3, label = "horizontal compress")
# mapy.plot(x, (x ** 3) / 2, label = "vertical compress")
#
# mapy.plot(x, (x / 2) ** 3, label = "horizontal stretch")
# mapy.plot(x, 2 * (x ** 3), label = "vertical stretch")
#
# mapy.plot(x, (-x ** 2), label = "reflect across y-axis")
# mapy.plot(x, -(x ** 2), label = "reflect across x-axis")
#
# mapy.xlabel('x-axis label')
# mapy.ylabel('y-axis label')
# mapy.title("Simple Plot")
# mapy.legend()
# mapy.show()

# x = np.arange(0, 10, 0.2)
# y = np.sin(x)
# fig, ax = mapy.subplots()
# ax.plot(x, y)
# mapy.show()

# def my_plotter(ax, data1, data2, param_dict):
# 	"""
# 	A helper function to make a graph
# 	Parameters
# 	----------
# 	ax : Axes
# 	The axes to draw to
# 	data1 : array
# 	The x data
# 	data2 : array
# 	The y data
# 	param_dict : dict
# 	Dictionary of kwargs to pass to ax.plot
# 	Returns
# 	-------
# 	out : list
# 	list of artists added
# 	"""
# 	out = ax.plot(data1, data2, **param_dict)
# 	return out

# which you would then use as:
data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, ax = mapy.subplots(1, 1)
# my_plotter(ax, data1, data2, {'marker': 'x'})
# mapy.show()

# fig, (ax1, ax2) = mapy.subplots(1, 2)
# my_plotter(ax1, data1, data2, {"marker": "x"})
# my_plotter(ax2, data3, data4, {"marker": "o"})
# mapy.show()

# print(matplotlib.is_interactive())
# print(mapy.isinteractive())
# mapy.ion()
# mapy.plot([1.5, 3])
# mapy.show()

# axes = mapy.gca()
# axes.plot([1.9, 2.9])

# mapy.ioff()
# for i in range(3):
# 	mapy.plot(np.random.randn(10))
# 	mapy.show()

# mapy.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
# mapy.axis([0, 10, 0, 11])
# mapy.grid(True)
# mapy.show()

# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
# # red dashes, blue squares and green triangles
# mapy.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# mapy.axis([0, 10, 0, 111])
# mapy.show()

# data = {"a": np.arange(10), "c": np.random.randint(0, 10, 10), "d": np.random.randn(10)}
# # data = {"a": np.arange(10), "c": list(range(0, 1000, 100)), "d": np.random.randn(10)}
# data["b"] = data["a"] + 10 * np.random.randn(10)
# data["d"] = np.abs(data["d"]) * 150
# print("a: " + str(data["a"]))
# print("b: " + str(data["b"]))
# print("c: " + str(data["c"]))
# print("d: " + str(data["d"]))
# mapy.scatter("a", "b", c = "c", s = "d", data = data)	# "c": data["c"]: 0: brownish purple, 9: yellow, 2 for bluish gray marker color, "s": marker size in pixels corresponding to data["d"], bigger numbers correspond to bigger marker.
# mapy.grid(True)
# mapy.legend()
# mapy.show()

# names = ["group_a", "group_b", "group_c"]
# values = [1, 10, 100]
# mapy.figure(1, figsize = (9, 3), dpi = 192)
# mapy.subplot(131)
# mapy.bar(names, values)
# mapy.subplot(132)
# mapy.scatter(names, values)
# mapy.subplot(133)
# mapy.plot(names, values)
# mapy.suptitle("Categorical Plotting")
# mapy.show()

# line1, line2 = mapy.plot(0, 10, 5, 20)
# print(type(line1))
# mapy.show()

# line1, = mapy.plot(range(0, 10), range(0, 100, 10), "-")
# line1.set_antialiased(False)
# mapy.show()

# lines = mapy.plot([list(range(5, 15)), list(range(0, 100, 10)), list(range(0, 1000, 100)), list(range(0, 10000, 1000))])
# # Use keyword arguments.
# mapy.setp(lines, color = "r", linewidth = 2.0)
# # Or MATLAB-style sting-value pairs.
# mapy.setp(lines, "color", "r", "linewidth", 2.0)
# mapy.show()

# lines = mapy.plot(0, 1)
# mapy.setp(lines)

# # MINE
#
# mapy.grid(True, 'both', drawstyle = "steps-mid", fillstyle = "full", markevery = 0.5, linestyle = "-.")
# mapy.tick_params(axis = "both", which = "both", width = 0.1, length = 0.1)
# x = [i for i in range(-10, 10)]
# y1 = [i ** 2 for i in x]
# y2 = [i ** 2 + i for i in x]
# y3 = [i ** 2 + i + 1 for i in x]
# # y4 = [i ** 2 + 5 * i + 1 for i in x]
# # y5 = [i ** 2 - i + 1 for i in x]
# # y6 = [i ** 2 + i - 1 for i in x]
# # y7 = [((i ** 3) / 3) - ((i ** 2) / 2) - (2 * i) + (1 / 3) for i in range(-10, 10, 2)]
# mapy.plot(x, y1, 'o-r')
# mapy.annotate("i ** 2", xy = (x[0], y1[0]), xytext = (0, 5), arrowprops = dict(facecolor = 'black', shrink = 0.05))
# mapy.plot(x, y2, '^-g')
# mapy.annotate("i ** 2 + i", xy = (x[0], y2[0]), xytext = (0, 6), arrowprops = dict(facecolor = 'black', shrink = 0.05))
# mapy.plot(x, y3, 's-b')
# mapy.annotate("i ** 2 + i + 1", xy = (x[0], y3[0]), xytext = (0, 7), arrowprops = dict(facecolor = 'black', shrink = 0.05))
# # mapy.plot(x, y4, 'p-c')
# # mapy.plot(x, y5, 'h-m')
# # mapy.plot(x, y6, '8-y')
# # mapy.plot(x, y7, 'x-k')
# mapy.show()
