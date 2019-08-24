import os


def url():
    return input("Please type competition url: ")


def title_script(url_name):
    title = url_name.split("/")[4]
    print("Directory name: ", title)

    if os.path.isdir("Competition/" + title):
        print("既に作られています")
    else:
        os.mkdir("Competition/" + title)
        os.mkdir("Competition/" + title + "/data")
        os.mkdir("Competition/" + title + "/model")
        os.mkdir("Competition/" + title + "/notebook")
        os.mkdir("Competition/" + title + "/Log")

        with open("Competition/" + title + "/README.md", "w") as f:
            f.write("# " + title)

        print("Done")
        print("Kaggle精進しろ")


if __name__ == "__main__":
    title_script(url())
