# 프로젝트 이름: My Face Reading App

## 개요
My Face Reading App은 사용자가 업로드한 얼굴 이미지를 분석하여 MBTI 성격 유형을 예측하고, 해당 성격 유형에 맞는 대학 학과를 추천해주는 웹 애플리케이션이다. 이 애플리케이션은 OpenCV와 dlib을 사용하여 얼굴 검출 및 랜드마크 예측을 수행하며, Flask 프레임워크를 이용해 서버를 구축한다.

## 주요 기능
얼굴 검출 및 랜드마크 예측: 업로드된 이미지에서 얼굴을 검출하고 얼굴의 68개 랜드마크를 예측한다.
MBTI 성격 유형 예측: 얼굴의 랜드마크를 기반으로 사용자의 MBTI 성격 유형을 예측한다.
대학 학과 추천: 예측된 MBTI 유형에 따라 사용자가 선택한 학교의 학과를 추천한다.
랜드마크 표시 이미지 생성: 얼굴 랜드마크가 표시된 이미지를 생성하여 결과와 함께 제공한다.

## 요구 사항
이 프로젝트를 실행하기 위해 다음과 같은 Python 라이브러리와 패키지가 필요하다:

Python 3.x

Flask

OpenCV (cv2)

dlib


## 프로젝트 구조
프로젝트 폴더는 다음과 같은 구조를 가지고 있어야 한다:

my_face_reading_app/
│

├── static/

│   └── images/

│       └── uploaded/   # 업로드된 이미지가 저장될 폴더

│

├── templates/

│   ├── index.html      # 메인 페이지 템플릿

│   ├── upload.html     # 업로드 페이지 템플릿

│   └── result.html     # 결과 페이지 템플릿

│

├── app.py              # Flask 애플리케이션 파일

└── shape_predictor_68_face_landmarks.dat  # dlib 모델 파일


4. Flask 애플리케이션 실행
프로젝트 디렉토리로 이동한 후 다음 명령어로 애플리케이션을 실행한다:

코드 복사
python app.py
서버가 시작되고 http://127.0.0.1:5000/에서 애플리케이션에 접근할 수 있다.

5. 사용 방법
메인 페이지에서 "Upload" 버튼을 클릭하여 얼굴 이미지를 업로드할 수 있는 페이지로 이동한다.
얼굴 이미지 파일을 선택하고, 학과 추천을 받을 학교를 선택한 후 "Upload" 버튼을 클릭한다.
분석이 완료되면 사용자의 MBTI 성격 유형과 추천 학과 목록, 얼굴 랜드마크가 표시된 이미지가 결과 페이지에 표시된다.
코드 설명
이 프로젝트의 주요 코드 흐름과 기능을 설명한다:

라이브러리 및 모듈 불러오기:

프로젝트에 필요한 다양한 Python 라이브러리 및 모듈을 불러온다. Flask는 웹 애플리케이션을 만들기 위해 사용되고, OpenCV와 dlib은 얼굴 검출 및 랜드마크 예측에 사용된다.
Flask 애플리케이션 설정:


```python
app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = 'my_face_reading_app/static/images/uploaded/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
Flask 애플리케이션을 초기화하고 정적 파일 경로와 업로드 폴더, 허용 파일 확장자를 설정한다.
얼굴 검출기 및 랜드마크 예측기 초기화:
makefile
코드 복사
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
```
dlib을 이용해 얼굴 검출기와 랜드마크 예측기를 초기화한다. shape_predictor_68_face_landmarks.dat 파일은 dlib의 사전 학습된 모델 파일로, 얼굴의 68개 랜드마크를 예측하는 데 사용된다.
MBTI 성격 유형 및 학과 매핑:

MBTI 성격 유형별로 추천 학과 리스트를 구성하여 사용자의 MBTI 결과에 따라 적합한 학과를 추천한다.
이미지 파일 처리 및 분석:


```python
def analyze_face(image_path, school):
    # 이미지를 읽고 그레이스케일로 변환한다.
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    # 얼굴이 감지되지 않으면 메시지를 반환한다.
    if len(faces) == 0:
        return "얼굴을 인식하지 못했습니다.", [], None

    # 각 얼굴에 대해 랜드마크 예측 및 이미지에 표시한다.
    for face in faces:
        landmarks = predictor(gray, face)
        for n in range(68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            face_point[n] = [x, y]
            cv2.circle(image, (x, y), 2, (255, 0, 0), -1)

        # 골든 레이시오를 체크한다.
        check()

    # 사용자가 선택한 학교에 따라 추천 학과 리스트를 설정한다.
    if school == 'inha':
        subject_list = INHA
    elif school == 'sangmyung-seoul':
        subject_list = SEOUL
    elif school == 'sangmyung-cheonan':
        subject_list = CHEONAN
    else:
        return "잘못된 학교 선택입니다.", [], None

    # 랜드마크가 표시된 이미지를 저장한다.
    output_image_path = image_path.replace(".jpg", "_landmarks.jpg").replace(".png", "_landmarks.png")
    cv2.imwrite(output_image_path, image)

    # 사용자의 MBTI 유형을 예측하고 추천 학과를 반환한다.
    mbti_type = check_MBTI(checking_list)
    return mbti_type, pick_random_subject(subject_list, mbti_type), output_image_path
```
이미지 파일을 읽어 얼굴을 검출하고 랜드마크를 예측한다.
골든 레이시오를 체크하여 얼굴의 비율에 따른 MBTI 유형을 예측한다.
예측된 MBTI 유형에 따라 적합한 학과를 추천한다.
파일 업로드 처리:

```python
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files or 'school' not in request.form:
        return redirect(request.url)

    file = request.files['file']
    school = request.form['school']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(filepath)

        mbti_type, recommended_subjects, landmarks_image_path = analyze_face(filepath, school)
        mbti_type = face_MBTI[mbti_type]
        recommended_subject = [{"name": item["name"], "url": item["url"]} for item in subjects if item["name"] in recommended_subjects]
        landmarks_image_path = landmarks_image_path.replace("my_face_reading_app/", "")
        return render_template('result.html', mbti_type=mbti_type, subjects=recommended_subject, image_path=landmarks_image_path)
```
        
사용자가 업로드한 이미지 파일과 선택한 학교 정보를 처리한다.
얼굴 분석을 수행하고, 예측된 MBTI 유형과 추천 학과를 result.html 템플릿에 렌더링한다.
기본 페이지 및 업로드 페이지 라우트 설정:

/, /upload, /result 라우트를 설정하여 각 페이지를 렌더링한다.
애플리케이션 실행:

```python
if __name__ == '__main__':
    app.run(debug=True)
```
Flask 애플리케이션을 디버그 모드로 실행하여 개발 중에 오류와 디버그 정보를 쉽게 확인할 수 있도록 한다.
