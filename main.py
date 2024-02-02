import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('box.png', cv.IMREAD_GRAYSCALE)
# Constructor default params: nOctaveLayers = 3,
# contrastThreshold = 0.04, edgeThreshold = 10, sigma = 1.6
sift = cv.SIFT_create()  # construct
kp = sift.detect(img)  # detect keypoints

xmin = img.shape[0]
xmax = img.shape[1]
ymin = img.shape[0]
ymax = img.shape[1]

foundKps = [k for k in kp if xmin <= k.pt[0] <= xmax and ymin <= k.pt[1] <= ymax]  # keypoint within rectangle
foundKps = sorted(kp, key=lambda x: x.size, reverse=True)  # 3 largest keypoints


def unpackSIFTOctave(kpt):
    """unpackSIFTOctave(kpt)->(octave,layer,scale)
    @created by Silencer at 2018.01.23 11:12:30 CST
    @brief Unpack Sift Keypoint by Silencer
    @param kpt: cv2.KeyPoint (of SIFT)
    """
    _octave = kpt.octave
    octave = _octave & 0xFF
    layer = (_octave >> 8) & 0xFF
    if octave >= 128:
        octave |= -128
    if octave >= 0:
        scale = float(1 / (1 << octave))
    else:
        scale = float(1 << -octave)
    return (octave, layer, scale)


n_value = [10, 100, 500]
for n in n_value:
    # Select the top n keypoints with the highest response
    selected_kps = foundKps[:n]

    # Display the properties of the selected keypoints
    print(f"\nTop {n} keypoints with highest response:")
    for i, keypoint in enumerate(selected_kps):
        octave, layer, scale = unpackSIFTOctave(keypoint)
        print(f"Keypoint {i + 1}: Response - {keypoint.response}, Octave - {octave}, Layer - {layer}, Scale - {scale}")

    img_with_kps = cv.drawKeypoints(img, selected_kps, img.copy(), flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

img_with_kp = cv.drawKeypoints(img, kp, img, None,
                               cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img_with_kp)
plt.show()
