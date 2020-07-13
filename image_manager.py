import logging
import datetime
import io
import os
from PIL import Image

LOG_FILENAME = f"image_creator_{datetime.date.today()}.log"

logging.basicConfig(
    filename=LOG_FILENAME,
    filemode="w",
    level=logging.INFO,
    format='[%(levelname)s]%(asctime)s: %(message)s'
)


class ImageManager:
    """
    This class is used to manipulate binary images
    """
    IMAGE_GENERATOR_FOLDER = "./_image-creator"

    def createImageFile(self, imageName, binaryImage):
        """
        Creates a image file

        Parameters:
            imageName (string): the name of the image
            binaryImage (bytes): the binary content of the image
        """
        with Image.open(io.BytesIO(binaryImage), 'r') as image:
            try:
                os.mkdir(self.IMAGE_GENERATOR_FOLDER)
            except OSError as e:
                if e.errno == 17:
                    print("Creation of the directory failed: Already exist.")
                    logging.error("Creation of the directory failed: Already exist.")
            else:
                print("Successfully created the directory.")
                logging.info("Successfully created the directory.")

            with open(f"{self.IMAGE_GENERATOR_FOLDER}/{imageName}.{image.format.lower()}", "wb") as outputImage:
                try:
                    image.save(outputImage)
                    logging.info(f"{imageName}.{image.format.lower()} has been created.")
                except OSError:
                    print("cannot convert image", image[0])
                    logging.error(f"cannot convert image {image[0]}")

    def createAllImagesFiles(self, images):
        """
        Creates all images files

        Parameters:
            images (list): the list of the image
        """
        for image in images:
            imageName = image[0]
            binaryImage = image[1]

            with Image.open(io.BytesIO(binaryImage), 'r') as imagePIL:
                try:
                    os.mkdir(self.IMAGE_GENERATOR_FOLDER)
                except OSError as e:
                    if e.errno == 17:
                        print("Creation of the directory failed: Already exist.")
                        logging.error("Creation of the directory failed: Already exist.")
                else:
                    print("Successfully created the directory.")
                    logging.info("Successfully created the directory.")

                with open(f"{self.IMAGE_GENERATOR_FOLDER}/{imageName}.{imagePIL.format.lower()}", "wb") as outputImage:
                    try:
                        imagePIL.save(outputImage)
                        logging.info(f"{imageName}.{imagePIL.format.lower()} has been created.")
                    except OSError:
                        print("cannot convert image", imagePIL[0])
                        logging.error(f"cannot convert image {imagePIL[0]}")

