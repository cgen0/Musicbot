from mutagen.flac import FLAC

def fetch_metadata(song):

    file = FLAC(song)
    duration = (file.info.length)
    title = (file['title'][0])
    album = str((file['album'][0]))
    artist = str((file['artist'][0]))
    genrelist = str((file['style'][0])).split(", ")
    genrelist = ['#' + element.replace(" ", "") for element in genrelist]
    genre= ' '.join(genrelist)
    print(genre)
    version_date = str((file['date'][0]))
    release_date=str((file['comment'][0]))
    bits = str(file.info.bits_per_sample) + "bit"
    sample_rate = str(file.info.sample_rate/1000) + "kHz"
    totalstring = artist + " - " + album + " \n" \
        + "Release Date: " + release_date + " \n" \
        + "Version Date: " + version_date + " \n" \
        + "Genre: " + genre + " \n" \
        + "Codec: FLAC " + sample_rate +" " + bits
    metadata = {"title": title, "album": album, "artist": artist,"genre": genre, "version_date": version_date,
                "release_date": release_date, "bits": bits, "sample_rate": sample_rate, 'duration': duration,
                "total": totalstring}
    return metadata
def fetch_images(song):
    file = FLAC(song)
    pics = file.pictures
    # print(pics)
    for p in pics:
        if p.type == 3:  # front cover
            with open("copertina.jpg", "wb") as f:
                f.write(p.data)
                f.close()
            # with open('copertina.jpg', 'rb') as t:
            #     with Image.open(t) as image:
            #         thumb = resizeimage.resize_cover(image, [200, 200])
            #         thumb.save('thumb.jpg', thumb.format)


if __name__ == "__main__":
    string = fetch_metadata("your/test/song/path")
    print(string)
    fetch_images("your/test/song/path")
