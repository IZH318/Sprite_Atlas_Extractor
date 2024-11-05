# 스프라이트 아틀라스 추출 도구 (Sprite Atlas Extractor)
![_2024_11_06_02_10_15_488-ezgif com-optimize](https://github.com/user-attachments/assets/fec3209f-9460-4d28-b9e9-07ee8c0801fa) <BR>
이 도구는 **스프라이트 아틀라스**(sprite atlas)에서 개별 스프라이트를 추출하여 각각의 PNG 이미지 파일로 저장합니다.<BR> <BR>
이 과정에서 **이미지 파일**(`.png`)과 **메타데이터 파일**(`.json`)이 필요하며, 메타데이터 파일은 스프라이트의 위치와 크기를 정의하는 정보를 포함하고 있어야 합니다.<BR> <BR>
이 도구는 게임 **'プリンセスコネクト！Re:Dive (プリコネR)'** 리소스 추출용으로 작성한 코드입니다. 필요에 따라 적절히 수정하여 사용하십시오.

<BR>

## 🔍 주요 기능

- **스프라이트 추출**: 주어진 아틀라스 이미지에서 여러 스프라이트를 추출하여 개별 이미지 파일로 저장합니다.
- **중복 처리**: 저장하려는 파일이 이미 존재하면 덮어쓰기 또는 파일 이름 끝에 숫자를 추가하여 구별할 수 있는 옵션을 제공합니다.
- **파일 선택 GUI**: `tkinter`를 이용한 간단한 GUI로 파일과 저장 경로를 선택할 수 있습니다.
- **확장성**: 새로운 스프라이트 아틀라스 파일 형식이나 기능을 추가하려면 코드 확장이 용이합니다.

<BR>

## 💾 다운로드 <BR>
| Program                                | URL                                                | 필수여부 | 비고                                                                                           |
|----------------------------------------|----------------------------------------------------|----------|------------------------------------------------------------------------------------------------|
| `Python`            | [Download](https://www.python.org/downloads/release/python-390/)   | 필수     | ◼ Python Script 동작, 파이썬 3.9.0 버전 또는 그 이상 사용 가능 |
| `반디집`             | [Download](https://kr.bandisoft.com/bandizip/)   | 필수     | ◼ (* 다른 압축 프로그램 사용 가능) |

<BR>

## 🛠️ 설치

1. Python 설치 파일을 실행 합니다. <BR> <BR>

2. Python을 설치합니다. <BR> <BR>
![2024-11-06 02 32 31](https://github.com/user-attachments/assets/0f9e2ed9-e57f-43e5-bbd3-14b4016be05d) <BR>
**[ ※ 주의 ] Python 설치 시 Add python.exe to PATH 에 반드시 체크 후 Install Now 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 또는 제거 후 재 설치) <BR> <BR>
![2024-11-06 02 33 33](https://github.com/user-attachments/assets/a891fae4-164f-4a56-8f9a-d21a7602f913) <BR>
**[ ※ 주의 ] 설치 후 Disable path length limit 기능을 사용할 수 있도록 반드시 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 후 작업 또는 제거 후 재 설치) <BR> <BR>

3. cmd 실행 후 아래 내용을 참고하여 필요한 패키지를 업데이트(선택) 또는 설치 합니다. <BR> <BR>
3-1. **(선택사항, 생략가능) Python Package Update** <BR> <BR>
(* 두 코드 중 하나 선택) <BR>
`pip install --upgrade pip` <BR>
or <BR>
`python -m pip install --upgrade pip` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 두 코드 중 하나 선택) <BR>
`pip install --upgrade pip --user` <BR>
or <BR>
`python -m pip install --upgrade pip --user` <BR>
<BR> <BR> <BR>
3-2. **(필수) Pillow Package 설치** <BR> <BR>
`pip install Pillow` <BR>
or <BR>
`python -m pip install Pillow` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 두 코드 중 하나 선택) <BR>
`pip install Pillow --user` <BR>
or <BR>
`python -m pip install Pillow --user` <BR>
<BR> <BR> <BR>
Windows 환경 사용자는 `00. Install_required_Python_packages.bat` 을 실행하여 필요 패키지를 한 번에 설치할 수 있습니다.

<BR>

## ⏩ 사용 방법

### 1. 아틀라스 이미지와 JSON 파일 준비

- **아틀라스 이미지**: `.png` 형식으로 된 이미지 파일입니다. 이 이미지에는 여러 개의 작은 스프라이트가 배치되어 있습니다.
- **JSON 파일**: 각 스프라이트의 좌표와 크기를 정의하는 파일입니다. JSON 파일은 아틀라스 이미지와 연관된 메타데이터를 포함하고 있어야 합니다.

<BR>

### 2. 프로그램 실행

1. 이 코드를 실행하면 GUI 창이 열리고, 순차적으로 아래와 같은 파일 선택 대화상자가 표시됩니다.
   - **원본 PNG 파일**: 스프라이트 아틀라스 이미지 파일을 선택합니다.
   - **JSON 파일**: 스프라이트 메타데이터가 포함된 JSON 파일을 선택합니다.
   - **저장 경로**: 추출된 스프라이트 파일을 저장할 디렉토리를 선택합니다.

2. 선택한 파일을 바탕으로 프로그램이 스프라이트를 추출하고, 각 스프라이트는 PNG 파일로 저장됩니다.

<BR>

### 3. 중복 파일 처리

만약 저장하려는 파일이 이미 존재할 경우, 다음과 같은 두 가지 옵션을 제공합니다:
- **덮어쓰기**: 기존 파일을 덮어씁니다.
- **파일 이름 끝에 숫자 추가**: 파일 이름에 숫자를 추가하여 중복을 방지합니다.

사용자는 이 두 가지 중 하나를 선택할 수 있습니다.

<BR>

### 4. 작업 완료 후

작업이 완료되면 추출된 스프라이트 수가 출력되고, 프로그램은 다시 시작할지 여부를 묻습니다.

<BR>

## 📝 코드 설명

### `extract_sprites` 함수

이 함수는 주어진 아틀라스 이미지에서 스프라이트를 추출하고, 지정된 디렉토리에 저장합니다.

- **입력값**:
  - `atlas_image_path`: 스프라이트 아틀라스 이미지 파일 경로.
  - `json_file_path`: 스프라이트 메타데이터 JSON 파일 경로.
  - `save_directory`: 추출된 스프라이트를 저장할 디렉토리 경로.

- **동작**:
  - 먼저, JSON 파일과 PNG 파일이 존재하는지 확인합니다.
  - JSON 파일을 읽고, `mSprites` 키에서 스프라이트 정보(이름, 위치, 크기)를 가져옵니다.
  - 각 스프라이트를 잘라서 PNG 형식으로 저장합니다.
  - 저장 전에 중복 파일 처리를 위한 옵션을 사용자에게 요청합니다.

### `Tkinter`를 사용한 GUI

- **파일 선택**: 사용자에게 파일을 선택할 수 있도록 `askopenfilename`과 `askdirectory` 함수를 사용하여 GUI 파일 선택 대화상자를 제공합니다.
- **파일 경로**: 선택된 파일 경로는 변수에 저장되고, 그 경로를 바탕으로 이미지와 JSON 파일을 읽고 저장합니다.

### 오류 처리

- 파일이 존재하지 않거나 잘못된 형식의 파일이 주어질 경우, 사용자에게 오류 메시지를 출력하고 작업을 중지합니다.
- JSON 파일에서 `mSprites` 키가 존재하지 않으면 경고 메시지를 출력합니다.

<BR>

## ⚖️ 라이센스

이 프로젝트는 [GNU Lesser General Public License v2.1](LICENSE)에 따라 라이선스가 부여됩니다.

<BR> <BR> <BR>
