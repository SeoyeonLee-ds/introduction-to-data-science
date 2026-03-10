import cv2
from sklearn.cluster import KMeans
import numpy as np
from tqdm import tqdm

def segment_image_with_kmeans(img, n_clusters, user_colors):

    h, w, c = img.shape
    pixels = img.reshape(-1, 3) #2차원을 1차원으로 합침

    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(pixels)
    labels = kmeans.labels_ #0, 1, 2
    user_colors_np = np.array(user_colors, dtype=np.uint8)
    segmented_pixels = user_colors_np[labels]
    segmented_image = segmented_pixels.reshape(h, w, c)

    return segmented_image

def process_video(input_path, output_path, n_clusters, user_colors):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print("비디오를 열 수 없습니다.")
        return
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    print("비디오 처리 중...")
    for _ in tqdm(range(total_frames)): #몇번 째 수행중인지 볼 수 있음
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        segmented_frame = segment_image_with_kmeans(frame_rgb, n_clusters, user_colors)
        segmented_bgr = cv2.cvtColor(segmented_frame, cv2.COLOR_RGB2BGR)

        out.write(segmented_frame)

    cap.release()
    out.release()
    
    # image = cv2.imread(image_path)
    # image = cv2.resize(image, (320,240))
    # image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # h, w, c = image_rgb.shape

    # pixels = image_rgb.reshape(-1, 3) #2차원을 1차원으로 합침

    # kmeans = KMeans(n_clusters=n_clusters)
    # kmeans.fit(pixels)
    # labels = kmeans.labels_ #0, 1, 2
    # user_colors_np = np.array(user_colors, dtype=np.uint8)
    # segmented_pixels = user_colors_np[labels]
    # segmented_image = segmented_pixels.reshape(h, w, c)

    # cv2.imwrite('seg.jpg', segmented_image)

    # return segmented_image


user_defined_colors = [(255,0,0), (0,255,0), (0,0,255)]
segmented_img = process_video("video_sample.mp4", "segmented_output.mp4", n_clusters=3, user_colors=user_defined_colors)