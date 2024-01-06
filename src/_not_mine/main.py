import matplotlib.pyplot as mapy
import inspect
import pandas
import numpy as np
import matplotlib
import matplotlib.ticker as mati

# # TUTORIALS.
#
# fig = mapy.figure()  # an empty figure with no axes
# fig.suptitle("No axes on this figure")  # Add a title so we know which it is
# fig, ax_lst = mapy.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# mapy.show()
#
# myDF = pandas.DataFrame(np.random.rand(4, 5), columns=list("abcde"))
# myNPArray = myDF.values
# print("type(myDF):", type(myDF))
# print("type(myNPArray):", type(myNPArray))
#
# myNPMatrix = np.matrix([[1, 2], [3, 4]])
# myNPArray = np.asarray(myNPMatrix)
# print("type(myDF):", type(myNPMatrix))
# print("type(myNPArray):", type(myNPArray))
#
# x = np.linspace(-1, 1, 100)
# mapy.plot(x, x, label="linear")
# mapy.plot(x, x**2, label="quadratic")
# mapy.plot(x, x**3, label="cubic")
#
# mapy.plot(x, (x - 1) ** 2, label="horizontal right shift")
# mapy.plot(x, (x + 1) ** 2, label="horizontal left shift")
#
# mapy.plot(x, x**2 - 1, label="vertical down shift")
# mapy.plot(x, x**2 + 1, label="vertical up shift")
#
# mapy.plot(x, (2 * x) ** 3, label="horizontal compress")
# mapy.plot(x, (x**3) / 2, label="vertical compress")
#
# mapy.plot(x, (x / 2) ** 3, label="horizontal stretch")
# mapy.plot(x, 2 * (x**3), label="vertical stretch")
#
# mapy.plot(x, (-(x**2)), label="reflect across y-axis")
# mapy.plot(x, -(x**2), label="reflect across x-axis")
#
# mapy.xlabel("x-axis label")
# mapy.ylabel("y-axis label")
# mapy.title("Simple Plot")
# mapy.legend()
# mapy.show()
#
# x = np.arange(0, 10, 0.2)
# y = np.sin(x)
# fig, ax = mapy.subplots()
# ax.plot(x, y)
# mapy.show()
#
#
# def my_plotter(ax, data1, data2, param_dict):
#     """
#     A helper function to make a graph
#     Parameters
#     ----------
#     ax : Axes
#     The axes to draw to
#     data1 : array
#     The x data
#     data2 : array
#     The y data
#     param_dict : dict
#     Dictionary of kwargs to pass to ax.plot
#     Returns
#     -------
#     out : list
#     list of artists added
#     """
#     out = ax.plot(data1, data2, **param_dict)
#     return out
#
#
# # which you would then use as:
# data1, data2, data3, data4 = np.random.randn(4, 100)
# # fig, ax = mapy.subplots(1, 1)
# my_plotter(ax, data1, data2, {"marker": "x"})
# mapy.show()
#
# fig, (ax1, ax2) = mapy.subplots(1, 2)
# my_plotter(ax1, data1, data2, {"marker": "x"})
# my_plotter(ax2, data3, data4, {"marker": "o"})
# mapy.show()
#
# print(matplotlib.is_interactive())
# print(mapy.isinteractive())
# mapy.ion()
# mapy.plot([1.5, 3])
# mapy.show()
#
# axes = mapy.gca()
# axes.plot([1.9, 2.9])
#
# mapy.ioff()
# for i in range(3):
#     mapy.plot(np.random.randn(10))
#     mapy.show()
#
# mapy.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
# mapy.axis([0, 10, 0, 11])
# mapy.grid(True)
# mapy.show()
#
# # evenly sampled time at 200ms intervals
# t = np.arange(0.0, 5.0, 0.2)
# # red dashes, blue squares and green triangles
# mapy.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^")
# mapy.axis([0, 10, 0, 111])
# mapy.show()
#
# data = {"a": np.arange(10), "c": np.random.randint(0, 10, 10), "d": np.random.randn(10)}
# # data = {"a": np.arange(10), "c": list(range(0, 1000, 100)), "d": np.random.randn(10)}
# data["b"] = data["a"] + 10 * np.random.randn(10)
# data["d"] = np.abs(data["d"]) * 150
# print("a: " + str(data["a"]))
# print("b: " + str(data["b"]))
# print("c: " + str(data["c"]))
# print("d: " + str(data["d"]))
# mapy.scatter(
#     "a", "b", c="c", s="d", data=data
# )  # "c": data["c"]: 0: brownish purple, 9: yellow, 2 for bluish gray marker color, "s": marker size in pixels corresponding to data["d"], bigger numbers correspond to bigger marker.
# mapy.grid(True)
# mapy.legend()
# mapy.show()
#
# names = ["group_a", "group_b", "group_c"]
# values = [1, 10, 100]
# mapy.figure(1, figsize=(9, 3), dpi=192)
# mapy.subplot(131)
# mapy.bar(names, values)
# mapy.subplot(132)
# mapy.scatter(names, values)
# mapy.subplot(133)
# mapy.plot(names, values)
# mapy.suptitle("Categorical Plotting")
# mapy.show()
#
# line1, line2 = mapy.plot(0, 10, 5, 20)
# print(type(line1))
# mapy.show()
#
# (line1,) = mapy.plot(range(0, 10), range(0, 100, 10), "-")
# line1.set_antialiased(False)
# mapy.show()
#
# lines = mapy.plot(
#     [
#         list(range(5, 15)),
#         list(range(0, 100, 10)),
#         list(range(0, 1000, 100)),
#         list(range(0, 10000, 1000)),
#     ]
# )
# # Use keyword arguments.
# mapy.setp(lines, color="r", linewidth=2.0)
# # Or MATLAB-style sting-value pairs.
# mapy.setp(lines, "color", "r", "linewidth", 2.0)
# mapy.show()
#
# lines = mapy.plot(0, 1)
# mapy.setp(lines)

# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
#
#
# t1 = np.arange(0.00, 5.00, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
# print("t1:", t1)
# print("t2:", t2)
# mapy.figure(1)
# mapy.subplot(321)
# mapy.plot(t1, f(t1), "bo", t2, f(t2), "k")
# mapy.subplot(323)
# mapy.plot(t2, np.cos(2 * np.pi * t2), "r--")
# mapy.show()

# mapy.figure(1)
# mapy.subplot(211)
# mapy.plot([1, 4, 9, 16, 25])
# mapy.subplot(212)
# mapy.plot([1, 8, 27, 64, 125])
#
# mapy.figure(2)
# mapy.plot([1, 16, 81, 4**4, 5**4])
#
# mapy.figure(1)
# mapy.subplot(211)
# mapy.title("Referring to a previous subplot.")
# mapy.show()

# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
# print("x:", x, "len(x):", len(x))
# n, bins, patches = mapy.hist(x, 10, density=1, facecolor="g", alpha=0.75)
# mapy.xlabel("Smarts", fontsize=14, color="cyan")
# mapy.ylabel("Probability")
# mapy.title("Histogram of IQ")
# mapy.text(60, 0.025, r"$\mu = 100, \ \sigma = 15$")
# mapy.axis((40, 160, 0, 0.03))
# mapy.grid(True)
# mapy.show()

# ax = mapy.subplot(111)
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2 * np.pi * t)
# (line,) = mapy.plot(t, s, lw = 2)
# mapy.annotate("local max", xy = (2, 1), xytext = (3, 1.5), arrowprops = dict(facecolor = "black", shrink = 0.05),)
# mapy.ylim(-2, 2)
# mapy.show()

# np.random.seed(19438018)  # Using a fixed initial state for reproducibility.
# y = np.random.normal(loc = 0.5, scale = 0.4, size = 1000)
# print("y:", y, "len(y):", len(y))
# y = y[(y > 0) & (y < 1)]
# y.sort()
# print("y:", y, "len(y):", len(y))
# x = np.arange(len(y))
#
# mapy.figure(1)
# mapy.subplot(221)
# mapy.plot(x, y)
# mapy.yscale("linear")
# mapy.title("linear")
# mapy.grid(True, which = "both")
#
# mapy.subplot(222)
# mapy.plot(x, y)
# mapy.yscale("log")
# mapy.title("log")
# mapy.grid(True, which = "both")
#
# mapy.subplot(223)
# # mapy.plot(x, y - y.mean())
# mapy.plot(x, y)
# # mapy.yscale("symlog", linthreshy=0.01)
# mapy.yscale("symlog")
# mapy.title("symlog")
# mapy.grid(True, which = "both")
#
# mapy.subplot(224)
# mapy.plot(x, y)
# mapy.yscale("logit")
# mapy.title("logit")
# mapy.grid(True, which = "both")
#
# # To use empty strings as minor axis labels.
# mapy.gca().yaxis.set_minor_formatter(mati.NullFormatter())
# mapy.subplots_adjust(top = 0.92, bottom = 0.08, left = 0.1, right = 0.95, hspace = 0.25, wspace = 0.35)  # *[???]*
# mapy.show()
