import cv2
import pygame
from deepface import DeepFace

cap = cv2.VideoCapture(0)
pygame.mixer.init()

duygu_ceviri = {
    "angry": "Kızgın",
    "disgust": "Tiksinti",
    "fear": "Korku",
    "happy": "Mutlu",
    "sad": "Üzgün",
    "surprise": "Şaşırmış",
    "neutral": "Nötr"
}

duygu_sesleri = {
    "happy": "happy.mp3",
    "sad": "sad.mp3",
}

son_duygu = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        for face in analysis:
            x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']

            emotion = face['dominant_emotion']
            turkce_emotion = duygu_ceviri.get(emotion, emotion)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, turkce_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            if emotion in duygu_sesleri and emotion != son_duygu:
                pygame.mixer.music.load(duygu_sesleri[emotion])
                pygame.mixer.music.play()
                son_duygu = emotion

    except Exception as e:
        print(f"Hata: {e}")

    cv2.imshow("Gerçek Zamanlı Duygu Analizi", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
