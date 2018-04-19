import os
from google_images_download import google_images_download


class KittyPy(object):
    """ Gets cat pictures from the interwebs. The best. Only the best
    """

    def __init__(self, local_cache_dir=".kitties", limit=20):

        self.query = "cats"
        self.limit = limit
        self.local_cache_dir = "{}/{}".format(local_cache_dir,
                                              self.query)
        self.response = google_images_download.googleimagesdownload()

        try:
            self.response.download({"keywords": self.query,
                                    "limit": self.limit,
                                    "output_directory": local_cache_dir})

        except Exception as e:
            print("Oops! the internet is out of cats temporarily!")

        print("Downloaded {0} cats".format(self.limit))

    def get_kitty(self):
        """Get the path to a kitty downloaded from the internets!
        """

        for kittyfile in os.listdir(self.local_cache_dir):
            yield kittyfile
