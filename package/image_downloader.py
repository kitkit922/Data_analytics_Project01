from simple_image_download import simple_image_download as simp

# package/image_downloader.py
def down_images(keyword, num_pic):
    response = simp.simple_image_download()

    for kw in keyword:
        response.download(keywords=kw, limit=num_pic)
