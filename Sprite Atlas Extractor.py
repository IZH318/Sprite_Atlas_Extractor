import json  # JSON 파일을 처리하기 위한 모듈
from PIL import Image  # 이미지 처리를 위한 PIL 라이브러리
import os  # 운영 체제와 상호작용하기 위한 모듈
from tkinter import Tk  # Tkinter GUI를 위한 기본 창 모듈
from tkinter.filedialog import askopenfilename, askdirectory  # 파일 선택 대화상자를 열기 위한 함수들

def extract_sprites(atlas_image_path, json_file_path, save_directory):
    json_exists = os.path.exists(json_file_path)
    png_exists = os.path.exists(atlas_image_path)

    # 파일 존재 여부 체크
    if not json_exists and not png_exists:
        print(" [오류] 현재 경로에서 *.json 파일과 *.png 파일을 찾을 수 없습니다. 올바른 파일명을 입력하세요.\n\n")
        return False
    elif not json_exists:
        print(" [오류] 현재 경로에서 *.json 파일을 찾을 수 없습니다. 올바른 파일명을 입력하세요.\n\n")
        return False
    elif not png_exists:
        print(" [오류] 현재 경로에서 *.png 파일을 찾을 수 없습니다. 올바른 파일명을 입력하세요.\n\n")
        return False

    # JSON 파일 로드
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(" [오류] 올바르지 않은 *.json 파일입니다. 정상적인 파일인지 확인하세요.\n\n")
        return False

    # 'mSprites' 키 확인
    if 'mSprites' not in data:
        print(" [경고] 입력한 *.json 파일에 'mSprites' 키가 없습니다. 올바른 파일 명을 다시 입력하십시오.\n\n")
        return False

    # 원본 이미지 열기
    try:
        atlas_image = Image.open(atlas_image_path)
    except Exception as e:
        print(f" [오류] 이미지를 열 수 없습니다: {e}")
        return False

    # 중복 파일 이름 처리 선택
    overwrite_choice = None
    for sprite in data['mSprites']:
        sprite_name = sprite['name']
        x = sprite['x']
        y = sprite['y']
        width = sprite['width']
        height = sprite['height']
        sprite_image = atlas_image.crop((x, y, x + width, y + height))

        save_name = os.path.join(save_directory, f"{sprite_name}.png") if save_directory else f"{sprite_name}.png"
        
        if os.path.exists(save_name):
            if overwrite_choice is None:
                while True:
                    print(f" [경고] 존재하는 파일이 발견 되었습니다. 처리 방식을 선택하십시오.")
                    overwrite_choice = input(" [선택] 모든 파일 덮어쓰기(1) 또는 모든 파일 이름 끝에 숫자 추가(2): ").strip()
                    
                    if overwrite_choice in ['1', '2']:
                        break
                    else:
                        print(" [오류] 잘못된 선택입니다. 다시 선택하십시오.")
                    print()

            if overwrite_choice == '1':
                pass
            elif overwrite_choice == '2':
                counter = 1
                while os.path.exists(save_name):
                    save_name = os.path.join(save_directory, f"{sprite_name}_{counter}.png")
                    counter += 1

        sprite_image.save(save_name)

        if overwrite_choice == '1':
            print()
            print(f" [정보] Sprite name: {sprite_name}")
            print(f" [정보] 저장(덮어쓰기): {save_name}")
        elif overwrite_choice == '2':
            print()
            print(f" [정보] Sprite name: {sprite_name}")
            print(f" [정보] 저장(숫자 추가): {save_name}")
        else:
            print()
            print(f" [정보] Sprite name: {sprite_name}")
            print(f" [정보] 저장: {save_name}")

    print(f"\n\n\n [안내] 총 {len(data['mSprites'])}개의 스프라이트가 분리되었습니다.")
    return True

if __name__ == "__main__":
    while True:
        print("\n 스프라이트 아틀라스(Sprite Atlas) 추출 도구\n")

        root = None
        try:
            print(" [안내] 원본 *.png 파일 지정\n")
            
            root = Tk()
            root.title("원본 *.png 파일 지정")
            root.geometry("300x0")
            root.resizable(False, False)
            atlas_image_path = askopenfilename(parent=root, title="원본 *.png 파일 지정", filetypes=[("PNG files", "*.png")])
            if atlas_image_path:
                current_directory = os.path.dirname(atlas_image_path)  # 선택된 PNG 파일의 경로
                root.destroy()
            else:
                print(" [오류] *.png 파일이 선택되지 않았습니다. 다시 시작합니다.\n")
                if root and root.winfo_exists():
                    root.destroy()
                continue

            print(" [안내] 원본 *.png 파일의 개별 스프라이트 메타데이터가 포함된 *.json 파일 지정\n")
            root = Tk()
            root.title("원본 *.json 파일 지정")
            root.geometry("300x0")
            root.resizable(False, False)
            json_file_path = askopenfilename(parent=root, title="원본 *.png 파일의 개별 스프라이트 메타데이터가 포함된 *.json 파일 지정", filetypes=[("JSON files", "*.json")], initialdir=current_directory)
            if json_file_path:
                root.destroy()
            else:
                print(" [오류] *.json 파일이 선택되지 않았습니다. 다시 시작합니다.\n")
                if root and root.winfo_exists():
                    root.destroy()
                continue

            print(" [안내] 파일 저장 경로를 지정하십시오.\n")
            root = Tk()
            root.title("파일 저장 경로 선택")
            root.geometry("300x0")
            root.resizable(False, False)

            # 폴더 선택 대화상자 열기
            save_directory = askdirectory(parent=root, title="파일 저장 경로 지정", initialdir=current_directory)  # PNG 경로를 기본값으로 설정
            if save_directory:
                root.destroy()
            else:
                print(" [오류] 저장 경로가 선택되지 않았습니다. 다시 시작하십시오.\n")
                if root and root.winfo_exists():
                    root.destroy()
                continue

            if extract_sprites(atlas_image_path, json_file_path, save_directory):
                while True:
                    restart = input("\n [안내] 작업이 성공적으로 완료되었습니다. 다시 시작하시겠습니까? (y/n): ").strip().lower()
                    if restart in ['y', 'n']:
                        break
                    else:
                        print(" [오류] 잘못된 선택입니다. y 또는 n을 입력하십시오.")
                if restart == 'y':
                    print("\n")
                elif restart == 'n':
                    break
        except Exception as e:
            print(f" [오류] 작업 중 오류가 발생했습니다: {e}.")
            print(f" [안내] 처음부터 다시 시작합니다.\n\n")
            # root가 존재하는 경우에만 destroy 호출
            try:
                if root and root.winfo_exists():
                    root.destroy()
            except Exception as inner_e:
                print(f" [오류] Tkinter 창 처리 중 오류 발생: {inner_e}.")
                print(f" [안내] 처음부터 다시 시작합니다.\n\n")
