import package.image_downloader as downloader


def main():
    str = "__main__"
    print("\n--------Main--------\n")

    keywords = ["toronto bus"]
    num_pic = 50

    downloader.down_images(keywords, num_pic)


if __name__ == "__main__":
    main()