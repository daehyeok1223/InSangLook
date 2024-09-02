import cv2
import dlib
from collections import defaultdict

# Dlib의 얼굴 검출기와 랜드마크 예측기 초기화
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # 이미 다운로드한 모델 파일 사용

# 사용자 지정 이미지 경로
image_path = "/Users/handaehyeok/face_recognition_project/static/images/uploaded/muu.jpg"  # 로컬에 있는 이미지 파일 경로로 변경하세요.

# 이미지 읽기
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 검출
faces = detector(gray)

# 랜드마크의 설명을 저장하는 리스트
landmark_descriptions = [
    "턱선 1", "턱선 2", "턱선 3", "턱선 4", "턱선 5", "턱선 6", "턱선 7", "턱선 8", "턱선 9", "턱선 10",
    "턱선 11", "턱선 12", "턱선 13", "턱선 14", "턱선 15", "턱선 16", "턱선 17",
    "왼쪽 눈썹 1", "왼쪽 눈썹 2", "왼쪽 눈썹 3", "왼쪽 눈썹 4", "왼쪽 눈썹 5",
    "오른쪽 눈썹 1", "오른쪽 눈썹 2", "오른쪽 눈썹 3", "오른쪽 눈썹 4", "오른쪽 눈썹 5",
    "코 다리 1", "코 다리 2", "코 다리 3", "코 다리 4",
    "코 아래 1", "코 아래 2", "코 아래 3", "코 아래 4", "코 아래 5",
    "왼쪽 눈 1", "왼쪽 눈 2", "왼쪽 눈 3", "왼쪽 눈 4", "왼쪽 눈 5", "왼쪽 눈 6",
    "오른쪽 눈 1", "오른쪽 눈 2", "오른쪽 눈 3", "오른쪽 눈 4", "오른쪽 눈 5", "오른쪽 눈 6",
    "입 바깥 라인 1", "입 바깥 라인 2", "입 바깥 라인 3", "입 바깥 라인 4", "입 바깥 라인 5",
    "입 바깥 라인 6", "입 바깥 라인 7", "입 바깥 라인 8", "입 바깥 라인 9", "입 바깥 라인 10", "입 바깥 라인 11", "입 바깥 라인 12",
    "입 안쪽 라인 1", "입 안쪽 라인 2", "입 안쪽 라인 3", "입 안쪽 라인 4", "입 안쪽 라인 5", "입 안쪽 라인 6", "입 안쪽 라인 7", "입 안쪽 라인 8"
]

SEOUL = defaultdict(list)
SEOUL["ISTJ"] = ["행정학부", "국가안보학과","경영학부","경제금융학부","핀테크전공"]

# list 로 점 배열들 저장
face_point = defaultdict(list)

# 리스트
checking_list = [0] * 7

# golden ratio
golen_ratio = {"미간": 56, "중안부": 132,
               "하안부": 133, "눈썹길이":106,
               "눈크기": 19, "눈꼬리":3,
               "코 넓이": 2627, "인중": 33,
               "입술두께": 36}
def check():
    Migan = face_point[22][0] - face_point[21][0]
    if Migan > golen_ratio["미간"]:
        checking_list[0] = 1
    elif Migan < golen_ratio["미간"]:
        checking_list[0] = -1

    JungAnbu = face_point[32][1] - face_point[22][1]
    if JungAnbu > golen_ratio["중안부"]:
        checking_list[1] = 1
    elif JungAnbu < golen_ratio["중안부"]:
        checking_list[1] = -1

    HaAnbu = face_point[8][1] - face_point[32][1]
    if HaAnbu > golen_ratio["하안부"]:
        checking_list[2] = 1
    elif HaAnbu < golen_ratio["하안부"]:
        checking_list[2] = -1

    NunSseopGil = face_point[26][0] - face_point[22][0]
    if NunSseopGil > golen_ratio["눈썹길이"]:
        checking_list[3] = 1
    elif NunSseopGil < golen_ratio["눈썹길이"]:
        checking_list[3] = -1

    NunKeokGi = face_point[43][1] - face_point[47][1]
    if NunKeokGi > golen_ratio["눈크기"]:
        checking_list[4] = 1
    elif NunKeokGi < golen_ratio["눈크기"]:
        checking_list[4] = -1

    NunKkori = face_point[42][1] - face_point[45][1]
    if NunKkori > golen_ratio["눈꼬리"]:
        checking_list[5] = 1
    elif NunKkori < golen_ratio["눈꼬리"]:
        checking_list[5] = -1

    KoNeolBi = face_point[35][0] - face_point[31][0]
    if KoNeolBi > golen_ratio["코 넓이"]:
        checking_list[6] = 1
    elif KoNeolBi < golen_ratio["코 넓이"]:
        checking_list[6] = -1

    # InJung = face_point[33][1] - face_point[51][1]
    # if InJung > golen_ratio["인중"]:
    #     checking_list[7] = 1
    # elif InJung < golen_ratio["인중"]:
    #     checking_list[7] = -1

    # IpSoolDukke = face_point[51][1] - face_point[57][1]
    # if IpSoolDukke > golen_ratio["입술두께"]:
    #     checking_list[8] = 1
    # elif IpSoolDukke < golen_ratio["입술두께"]:
    #     checking_list[8] = -1
    
for face in faces:
    # 얼굴 랜드마크 추출
    landmarks = predictor(gray, face)

    # 각 랜드마크의 좌표 출력
    for n in range(68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        face_point[n] = [x,y]
        print(face_point[n])
        print(f"랜드마크 {n} ({landmark_descriptions[n]}): (x={x}, y={y})")  # 각 랜드마크의 번호와 좌표 및 설명 출력
        # 랜드마크를 이미지에 표시
        cv2.circle(image, (x, y), 2, (255, 0, 0), -1)
        # 랜드마크 번호를 이미지에 표시
        cv2.putText(image, str(n), (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

# 결과 이미지 출력
cv2.imshow("Landmarks", image)
check()
print(checking_list)

# 'q' 키를 누르면 창을 닫기
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
