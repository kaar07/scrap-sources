import pandas as pd



if __name__ == "__main__":
    data = pd.read_csv("goodreads_library_export.csv")
    size = len(data)
    consol = list()
    for i in range(size):
        consol.append([str(data["Title"][i]),str(data["Author"][i])])
    with open("new.md","w") as new:
        for each in consol:
            new.write("**" + each[0] + "** - *" + each[1]+"*\n")



# Works for all books without any Bookshelves
