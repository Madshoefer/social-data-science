from myFINd1P import FINDHasherp
import concurrent.futures

find = FINDHasherp()

def multiprocess(filepath):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results=executor.map(find.fromFile, filepath)
        hn = {}
    for filename in results:
        hn[filename[1]] = filename[0]
    return hn

if __name__ == "__main__":
    import sys
    for filename in sys.argv[1:]:
        h=find.fromFile(filename)