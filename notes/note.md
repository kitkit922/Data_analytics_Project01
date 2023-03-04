# Tech Note

- [Tech Note](#tech-note)
  - [Steps 1: Virtual Environment](#steps-1-virtual-environment)
  - [Steps 2: download training images](#steps-2-download-training-images)
  - [Step 3: label training images](#step-3-label-training-images)

---

## Steps 1: Virtual Environment

1. Create virtual environment

   `python -m venv .venv`

2. Activate virtual environment

   `.venv\scripts\activate`

3. select Python interpretor

---

## Steps 2: download training images

1. update pip

   `pip install --upgrade pip`

2. install `simple_image_download` version: 0.4

   `pip install simple_image_download==0.4`

3. create `image_downloader.py`

```py
from simple_image_download import simple_image_download as simp

# package/image_downloader.py
def down_images(keyword, num_pic):
    response = simp.simple_image_download()

    for kw in keyword:
        response.download(keywords=kw, limit=num_pic)
```

4. update `main.py`

```py
import package.image_downloader as downloader

# /main.py
def main():
    str = "__main__"
    print("\n--------Main--------\n")

    keywords = ["toronto bus"]
    num_pic = 20

    downloader.down_images(keywords, num_pic)


if __name__ == "__main__":
    main()
```

---

## Step 3: label training images

1. install

---

[TOP](#tech-note)
