import pygame
import cv2
import time
import numpy as np
import mediapipe as mp
from mediapipe.python.solutions.drawing_utils import _normalized_to_pixel_coordinates as denormalize_coordinates
import os


pygame.mixer.init()
def get_mediapipe_app(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
):
    """Initialize and return Mediapipe FaceMesh Solution Graph object"""
    face_mesh = mp.solutions.face_mesh.FaceMesh(
        max_num_faces=max_num_faces,
        refine_landmarks=refine_landmarks,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence,
    )

    return face_mesh


def distance(point_1, point_2):
    """Calculate l2-norm between two points"""
    dist = sum([(i - j) * 2 for i, j in zip(point_1, point_2)]) * 0.5
    return dist

def play_mp3_hidden(filename):
    # pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Do other things while the music plays (if necessary)

    

def get_ear(landmarks, refer_idxs, frame_width, frame_height):
    """
    Calculate Eye Aspect Ratio for one eye.

    Args:
        landmarks: (list) Detected landmarks list
        refer_idxs: (list) Index positions of the chosen landmarks
                            in order P1, P2, P3, P4, P5, P6
        frame_width: (int) Width of captured frame
        frame_height: (int) Height of captured frame

    Returns:
        ear: (float) Eye aspect ratio
    """
    try:
        # Compute the euclidean distance between the horizontal
        coords_points = []
        for i in refer_idxs:
            lm = landmarks[i]
            coord = denormalize_coordinates(lm.x, lm.y, frame_width, frame_height)
            coords_points.append(coord)

        # Eye landmark (x, y)-coordinates
        P2_P6 = distance(coords_points[1], coords_points[5])
        P3_P5 = distance(coords_points[2], coords_points[4])
        P1_P4 = distance(coords_points[0], coords_points[3])

        # Compute the eye aspect ratio
        ear = (P2_P6 + P3_P5) / (2.0 * P1_P4)

    except:
        ear = 0.0
        coords_points = None

    return ear, coords_points


def calculate_avg_ear(landmarks, left_eye_idxs, right_eye_idxs, image_w, image_h):
    # Calculate Eye aspect ratio

    left_ear, left_lm_coordinates = get_ear(landmarks, left_eye_idxs, image_w, image_h)
    right_ear, right_lm_coordinates = get_ear(landmarks, right_eye_idxs, image_w, image_h)
    Avg_EAR = (left_ear + right_ear) / 2.0

    return Avg_EAR, (left_lm_coordinates, right_lm_coordinates)


def plot_eye_landmarks(frame, left_lm_coordinates, right_lm_coordinates, color):
    for lm_coordinates in [left_lm_coordinates, right_lm_coordinates]:
        if lm_coordinates:
            for coord in lm_coordinates:
                cv2.circle(frame, coord, 2, color, -1)

    frame = cv2.flip(frame, 1)
    return frame


def plot_text(image, text, origin, color, font=cv2.FONT_HERSHEY_SIMPLEX, fntScale=0.8, thickness=2):
    image = cv2.putText(image, text, origin, font, fntScale, color, thickness)
    return image



def run1():
    
    global start, endd,cal,summ,tong,flag
    flag = False
    start = None
    cal= 0
    endd= None
    summ=0
    tong=0
    mpfacemesh = mp.solutions.face_mesh
    face =get_mediapipe_app()
    mpdraw = mp.solutions.drawing_utils

    left_eyes = list(mpfacemesh.FACEMESH_LEFT_EYE)
    right_eyes = list(mpfacemesh.FACEMESH_RIGHT_EYE)

    left_eyes = set(np.ravel(left_eyes))
    right_eyes = set(np.ravel(right_eyes))
    pTime = 0
    cTime = 0
    chosen_left_eye_idxs = [362, 385, 387, 263, 373, 380]
    chosen_right_eye_idxs = [33, 160, 158, 133, 153, 144]
    all_chosen_idxs = chosen_left_eye_idxs + chosen_right_eye_idxs

    eye = left_eyes.union(right_eyes)
    cap = cv2.VideoCapture(0)
    
    while  True :
        if face:
            cTime = time.time()
            ret,img = cap.read()
            imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
            results = face.process(imgRGB)
            imgH, imgW, _ = img.shape
            if results.multi_face_landmarks:
                for facelm in results.multi_face_landmarks:
                    for id, lm in enumerate(facelm.landmark):
                        if id in chosen_left_eye_idxs : #left_eyes:
                            ih, iw, ic = img.shape
                            x, y = int(lm.x * iw), int(lm.y * ih)
                            cv2.circle(img , (x,y),1 , (0,255,0),1)
                        if id in chosen_right_eye_idxs : #right_eyes:
                            ih, iw, ic = img.shape
                            x, y = int(lm.x * iw), int(lm.y * ih)
                            cv2.circle(img, (x, y), 1, (0, 255, 0), 1)
                      
                if results.multi_face_landmarks:
                    for face_id, face_landmarks in enumerate(results.multi_face_landmarks):
                        landmarks = face_landmarks.landmark
                        EAR, _ = calculate_avg_ear(
                            landmarks,
                            chosen_left_eye_idxs,
                            chosen_right_eye_idxs,
                            imgW,
                            imgH
                        )
                        cv2.putText(img,
                                    f"EAR: {round(EAR, 2)}", (10, 70),
                                    cv2.FONT_HERSHEY_COMPLEX,
                                    1, (0, 255, 0), 2
                                    )
                    """if EAR < 0.15:
                        end_time = time.perf_counter()
                    """
              # When the eyes are closed
            if results.multi_face_landmarks:
                if EAR < 0.15:
                    if start is None:
                        start = time.time()
                        summ =start
                    else:
                        if start is not None:
                            
                            endd = time.time()
                            cal = endd - start
                            tong = endd - summ
                            tong = "{:.2f}".format(tong)
                        #  print("thời gian tính được là: ", tong)
                            if cal > 1:
                            #  while EAR < 0.15:
                            #q  for i in range(1,10000000):
                                start = time.time() + 1.3
                                filename = "C:\\Users\\Administrator\\Downloads\\wake.wav"
                                play_mp3_hidden(filename)
                        
                else:
                    start = None
                    endd = None
                    cal = 0.0
                    pygame.mixer.music.stop()
        #    pygame.mixer.quit()
            cv2.putText(img,f"Your eyes closed in: {tong}",(10,130),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
            cv2.imshow("hii",img)
            key = cv2.waitKey(1)
            if cv2.waitKey(1) == ord('q'):
                break
        
        else :
             cv2.putText(img, "No face detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.putText(img ,"FPS: " +str(int(1/(cTime-pTime))) ,(10,100),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)
        pTime= cTime
            
          

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    run1()