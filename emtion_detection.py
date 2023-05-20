from deepface import DeepFace
import cv2

def face_analize(image):
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
    emotion = DeepFace.analyze(img_path = image, detector_backend = backends[4], actions=['emotion'])
    return emotion[0]['dominant_emotion']