from importlib import util, metadata
from typing import List


def check_pakage(name: str) -> bool:
    if util.find_spec(name):
        print(f"[OK] {name} ({metadata.version(name)}) "
              "- Data manipulation ready")
        return True
    print(f"[KO] {name} - Data manipulation Don't exist")
    return False


def load_pakage(packages: List) -> bool:
    print("Checking dependencies:")
    all_exist = True
    for package in packages:
        all_exist &= check_pakage(package)
    return all_exist


def run_packages() -> None:
    data = numpy.random.randn(1000)
    print("Analyzing Matrix data...")
    print(f"Processing {len(data)} data points...")
    df = pandas.DataFrame(data)
    print(df)
    print("Generating visualization...\n")
    matplotlib.pyplot.plot(df[0])
    matplotlib.pyplot.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    packages = ["numpy", "pandas", "matplotlib"]
    f = load_pakage(packages)
    if f is False:
        print("Exiting the program...")
    else:
        import numpy
        import matplotlib.pyplot
        import pandas

        run_packages()
