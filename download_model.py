import urllib.request
import bz2

# Dlib의 얼굴 랜드마크 모델 파일 다운로드
url = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"
urllib.request.urlretrieve(url, "shape_predictor_68_face_landmarks.dat.bz2")

# 압축 풀기
with bz2.BZ2File("shape_predictor_68_face_landmarks.dat.bz2") as fr, open("shape_predictor_68_face_landmarks.dat", "wb") as fw:
    fw.write(fr.read())

print("shape_predictor_68_face_landmarks.dat 파일이 성공적으로 다운로드 및 압축 해제되었습니다.")