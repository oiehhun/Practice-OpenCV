import cv2
import dlib
import numpy as np
from deepface import DeepFace

# Dlib 초기화: 얼굴 감지기와 랜드마크 예측기
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # 모델 파일 필요

def analyze_face(face_image):
    """
    DeepFace를 사용하여 얼굴 속성(성별, 나이, 감정)을 분석합니다.
    """
    try:
        analysis = DeepFace.analyze(face_image, actions=['age', 'gender', 'emotion'], enforce_detection=False)
        
        # analysis가 리스트 형태일 경우 첫 번째 요소 선택
        if isinstance(analysis, list):
            analysis = analysis[0]
        
        return analysis['age'], analysis['gender'], analysis['dominant_emotion']
    
    except Exception as e:
        print(f"DeepFace 분석 에러: {e}")
        return None, None, None

def calculate_eye_direction(landmarks):
    """
    눈의 시선 방향을 계산합니다.
    왼쪽, 오른쪽, 위, 아래 방향을 추정합니다.
    """
    left_eye = landmarks[36:42]  # 왼쪽 눈 랜드마크
    right_eye = landmarks[42:48]  # 오른쪽 눈 랜드마크
    nose = landmarks[30]  # 코 끝

    # 눈 중심 계산
    left_eye_center = np.mean(left_eye, axis=0)
    right_eye_center = np.mean(right_eye, axis=0)

    # 눈 중심과 코 끝의 벡터 계산
    gaze_vector = np.mean([left_eye_center, right_eye_center], axis=0) - nose

    # 시선 방향 추정
    if gaze_vector[0] > 5:
        direction = "왼쪽"
    elif gaze_vector[0] < -5:
        direction = "오른쪽"
    elif gaze_vector[1] > 5:
        direction = "위"
    else:
        direction = "아래"

    return direction

def draw_overlay(frame, face_rect, age, gender, emotion, direction):
    """
    얼굴 영역에 네모 박스를 그리고 분석 결과를 표시합니다.
    """
    x, y, w, h = face_rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 얼굴 네모 박스

    # 분석 결과 텍스트 오버레이
    cv2.putText(frame, f"Age: {age}", (x, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(frame, f"Gender: {gender}", (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(frame, f"Emotion: {emotion}", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(frame, f"Direction: {direction}", (x, y - 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

def main():
    cap = cv2.VideoCapture(0)  # 웹캠 활성화
    if not cap.isOpened():
        print("웹캠을 열 수 없습니다.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)  # 얼굴 감지

        for face in faces:
            x, y, w, h = (face.left(), face.top(), face.width(), face.height())

            # 얼굴 이미지 잘라내기
            face_image = frame[y:y + h, x:x + w]

            # 얼굴 속성 분석
            age, gender, emotion = analyze_face(face_image)

            # 랜드마크 추출
            landmarks = predictor(gray, face)
            landmarks = np.array([[p.x, p.y] for p in landmarks.parts()])

            # 시선 방향 계산
            direction = calculate_eye_direction(landmarks)

            # 분석 결과 및 시선 방향 오버레이
            if age is not None and gender is not None and emotion is not None:
                draw_overlay(frame, (x, y, w, h), age, gender, emotion, direction)

        # 결과 표시
        cv2.imshow("Face Analysis and Eye Direction", frame)

        # 'q'를 누르면 종료
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()