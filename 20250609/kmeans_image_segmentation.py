import cv2
from sklearn.cluster import KMeans
import numpy as np

def segment_image_with_kmeans(image_path, n_clusters, user_colors):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (320,240))
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    h, w, c = image_rgb.shape

    pixels = image_rgb.reshape(-1, 3) #2차원을 1차원으로 합침

    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(pixels)
    labels = kmeans.labels_ #0, 1, 2
    user_colors_np = np.array(user_colors, dtype=np.uint8)
    segmented_pixels = user_colors_np[labels]
    segmented_image = segmented_pixels.reshape(h, w, c)

    cv2.imwrite('seg.jpg', segmented_image)

    return segmented_image


user_defined_colors = [(255,0,0), (0,255,0), (0,0,255)]
segmented_img = segment_image_with_kmeans("sample.jpg", n_clusters=3, user_colors=user_defined_colors)