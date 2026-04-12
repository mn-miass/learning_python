try :
    import pandas
    print(f"[OK] pandas {pandas.__version__} - Data manipulation ready")
except ImportError:
    print("pandas not found, install it with: pip install pandas")

try :
    import numpy
    print(f"[OK] numpy {numpy.__version__}) - Numerical computation ready")
except ImportError:
    print("numpy not found, install it with: pip install numpy")

try :
    import matplotlib
    print(f"[OK] matplotlib {matplotlib.__version__} - Visualization ready")
except ImportError:
    print("matplotlib not found, install it with: pip install matplotlib")


data = numpy.random.randn(1000)
print("\nAnalyzing Matrix data...")
print(f"Processing {len(data)} data points...")

df = pandas.DataFrame(data, columns=["signal"])
print(df.describe())