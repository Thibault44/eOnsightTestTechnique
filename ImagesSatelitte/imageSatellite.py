import os
from osgeo import gdal
import numpy as np
from PIL import Image

class ImageProcessor:
    def __init__(self, path):
        self.path = path
        # Chargement des bandes
        self.red_band = gdal.Open(os.path.join(path, '2022-04-16-00[]00_2022-04-16-23[]59_Sentinel-2_L2A_B04_(Raw).tiff'))
        self.green_band = gdal.Open(os.path.join(path, '2022-04-16-00[]00_2022-04-16-23[]59_Sentinel-2_L2A_B03_(Raw).tiff'))
        self.blue_band = gdal.Open(os.path.join(path, '2022-04-16-00[]00_2022-04-16-23[]59_Sentinel-2_L2A_B02_(Raw).tiff'))
        self.geotransform = self.red_band.GetGeoTransform()

    def normalize_array(self, array):
        #normalisation des array
        return array * 255.0 / array.max()

    def clip_array(self, array):
        #modification du contraste
        return (array).clip(0, 255)

    def process_image(self, lat, lon):
        # Lecture des tableaux numpy correspondant à chaque image
        array_r = self.red_band.ReadAsArray().astype(np.float32)[0]
        array_g = self.green_band.ReadAsArray().astype(np.float32)[0]
        array_b = self.blue_band.ReadAsArray().astype(np.float32)[0]

        # Normalisation des valeurs
        array_r = self.normalize_array(array_r)
        array_g = self.normalize_array(array_g)
        array_b = self.normalize_array(array_b)

        # Appliquer un bon niveau de contraste aux données
        array_r = self.clip_array(array_r)
        array_g = self.clip_array(array_g)
        array_b = self.clip_array(array_b)

        # Empiler les tableaux numpy des 3 images de la bande
        rgb_image = np.dstack((array_r, array_g, array_b))
        # Conversion en uint8
        rgb_image = rgb_image.astype(np.uint8)

        # Récupération du carré autour du pont
        image_height, image_width, _ = rgb_image.shape
        x = int((lon + 180) * (image_width / 360))
        y = int((90 - lat) * (image_height / 180))

        # Extraire la taille du pixel en X à partir de la transformation géométrique
        pixel_size = self.geotransform[1]
        # Calculer les limites du carré de 2 km x 2 km
        half_size = int(2000 / pixel_size)
        xmin = max(0, x - half_size)
        ymin = max(0, y - half_size)
        xmax = min(image_width, x + half_size)
        ymax = min(image_height, y + half_size)

        # Rogner l'image
        cropped_image = rgb_image[ymin:ymax, xmin:xmax, :]
        return cropped_image

    def save_image(self, image, path):
        # Afficher et sauvarger l'image rognée
        im = Image.fromarray(image, 'RGB')
        im.save(path)
        im.show()

if __name__ == '__main__':
    # Chemins de fichiers universels
    base_dir = 'Documents'
    input_dir = os.path.join(base_dir, 'EO_Browser_images_uint16')
    output_dir = os.path.join('PycharmProjects', 'RousselEOnsight')
    output_file = os.path.join(output_dir, 'pont_crop.png')

    # Création d'une instance de la classe ImageProcessor
    ip = ImageProcessor(input_dir)

    # Traitement de l'image
    cropped_image = ip.process_image(44.4261111, 8.88861111111111)

    # Sauvegarde de l'image
    ip.save_image(cropped_image, output_file)