from distutils.log import debug

showPlot = False

def isShowPlot():
    return showPlot

debugLog = False

def printDebug(*s):
    if debugLog:
        print(s)

IntToClassMapping = {
  0: "Sum",
  1: "Prod",
  2: "Max",
  3: "Min",
  4: "Mean",
  5: "All",
  6: "Any",
  7: "Count_Nonzero",
  8: "Std",
  9: "Cumsum",
  10: "Argmax",
  11: "Argmin",
  12: "Add",
  13: "Where",
  14: "Dot",
  15: "Matmul",
  16: "Outer",
  17: "Clip",
  18: "Diff",
  19: "Arange",
  20: "Linspace",
  21: "Allclose",
  22: "Transpose",
  23: "Ravel",
  24: "Moveaxis",
  25: "Squeeze",
  26: "Reshape",
  27: "Atleast_1D",
  28: "Concatenate",
  29: "Vstack",
  30: "Hstack",
  31: "Stack",
  32: "Tile",
  33: "Append",
  34: "Insert",
  35: "Repeat",
  36: "Eye",
  37: "Diag",
  38: "Full",
  39: "Sort",
  40: "Argsort",
  41: "Percentile",
  42: "Median",
  43: "Unique",
  44: "Searchsorted",
  45: "Take",
}

ClassToIntMapping = {v: k for (k, v) in IntToClassMapping.items()}