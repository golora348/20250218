import os  # 운영 체제와의 상호작용을 위한 모듈. 파일 및 디렉토리 작업을 수행
import json  # JSON 데이터 형식의 인코딩 및 디코딩을 위한 모듈. JSON 파일을 읽고 쓸 수 있음
import shutil  # 고급 파일 작업을 위한 모듈. 파일 복사, 이동 및 삭제 등 수행
from tkinter import Tk  # Tkinter GUI 애플리케이션을 위한 기본 클래스
from tkinter.filedialog import askopenfilename, askdirectory  # 파일 및 디렉토리 선택 대화상자를 제공하는 함수들

def select_base_directory():
    print("\n [INFO] Limbus Company Client '__data' 파일 검색 경로 지정 단계")

    while True:
        print(" [INFO] '__data' 파일 검색 경로를 어떻게 지정하시겠습니까?\n [1] 자동 (기본 경로 'C:\\Users\\(YourUsername)\\AppData\\LocalLow\\Unity\\ProjectMoon_LimbusCompany' 확인 후 지정)\n [2] 수동 (사용자가 직접 지정)")
        choice = input(" >>> ").strip()
        
        if choice == '1':
            search_path = r"C:\Users"  # 사용자 폴더가 위치한 기본 경로
            found = False
            
            # 모든 사용자 폴더 탐색
            for user_folder in os.listdir(search_path):
                app_data_path = os.path.join(search_path, user_folder, r"AppData\LocalLow\Unity\ProjectMoon_LimbusCompany")
                
                # 경로 존재 여부 확인
                if os.path.exists(app_data_path):
                    print(f"\n [INFO] '{app_data_path}' 경로를 찾았습니다.\n")
                    return app_data_path

            print(" [ERROR] '__data' 파일이 있는 경로를 찾을 수 없습니다.")
            continue

        elif choice == '2':
            while True:
                # 사용자에게 디렉토리 선택 대화상자 제공
                base_dir = askdirectory(title="Limbus Company Client '__data' 파일 검색 경로 지정")
                if base_dir:
                    print("\n [INFO] Limbus Company Client '__data' 파일 검색 경로: {}\n".format(base_dir))
                    return base_dir
                else:
                    while True:
                        retry_choice = input("\n [INFO] 경로가 지정되지 않았습니다. 다시 선택하시겠습니까? (Y/N)\n >>> ").strip().lower()
                        if retry_choice == 'y':
                            break
                        elif retry_choice == 'n':
                            print("\n [INFO] 프로그램을 종료합니다.")
                            exit(1)
                        else:
                            print("\n [ERROR] 입력이 올바르지 않습니다. 'Y' 또는 'N'을 입력하세요.")
        else:
            print("\n [ERROR] 입력이 올바르지 않습니다. '1' 또는 '2'를 입력하세요.\n")

def load_json():
    Tk().withdraw()  # Tkinter 창 숨기기
    print(" [INFO] 'catalog_S1.json' 파일 지정 단계")

    while True:
        print(" [INFO] 'catalog_S1.json' 파일을 어떻게 지정하시겠습니까?\n [1] 자동 (기본 경로 'C:\\Users\\(YourUserName)\\AppData\\LocalLow\\ProjectMoon\\LimbusCompany' 확인 후 지정)\n [2] 수동 (사용자가 직접 지정)")
        choice = input(" >>> ").strip()
        if choice == '1':
            search_path = r"C:\Users"  # 기본 사용자 폴더 경로
            target_file = "catalog_S1.json"
            found = False

            # 사용자 폴더 탐색 및 JSON 파일 검색
            for user_folder in os.listdir(search_path):
                app_data_path = os.path.join(search_path, user_folder, r"AppData\LocalLow\ProjectMoon\LimbusCompany")
                if os.path.exists(app_data_path):
                    for root, dirs, files in os.walk(app_data_path):
                        if target_file in files:
                            json_file_path = os.path.join(root, target_file)
                            print(f"\n [INFO] {json_file_path} 파일을 찾았습니다.\n")
                            with open(json_file_path, 'r', encoding='utf-8') as f:
                                return json.load(f)  # JSON 파일 로드
                            found = True
                            break

                if found:
                    break

            if not found:
                print(" [ERROR] catalog_S1.json 파일을 찾을 수 없습니다.")
                continue
        elif choice == '2':
            while True:
                # 파일 선택 대화상자를 통해 JSON 파일 선택
                json_file = askopenfilename(title="catalog_S1.json 파일 선택", filetypes=[("catalog_S1.json", "*.json")])
                if json_file:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        print(f"\n [INFO] {json_file} 파일을 로드했습니다.\n")
                        return json.load(f)
                else:
                    while True:
                        retry_choice = input("\n [INFO] catalog_S1.json 파일이 선택되지 않았습니다. 다시 선택하시겠습니까? (Y/N)\n >>> ").strip().lower()
                        if retry_choice == 'y':
                            break
                        elif retry_choice == 'n':
                            print("\n [INFO] 프로그램을 종료합니다.")
                            exit(1)
                        else:
                            print("\n [ERROR] 입력이 올바르지 않습니다. 'Y' 또는 'N'을 입력하세요.")
        else:
            print("\n [ERROR] 입력이 올바르지 않습니다. '1' 또는 '2'를 입력하세요.\n")

def find_data_files(base_dir):
    data_folders = []
    print(f" [INFO] {base_dir} 에서 '__data' 파일 찾는 중...")
    
    # 지정된 디렉토리에서 '__data' 파일 검색
    for root, dirs, files in os.walk(base_dir):
        if '__data' in files:
            data_folders.append(root)  # 발견된 경로 추가
            print(f" [INFO] '__data' 파일 경로: {root}")
    print()
    return data_folders

def find_matching_url(json_data, folder_name, index, total_files):
    urls = []

    def collect_urls(d):
        # JSON 데이터에서 URL 수집
        if isinstance(d, dict):
            for value in d.values():
                collect_urls(value)
        elif isinstance(d, list):
            for item in d:
                collect_urls(item)
        elif isinstance(d, str):
            if d.startswith("https://"):  # URL 형식 확인
                urls.append(d)

    collect_urls(json_data)  # JSON 데이터 탐색

    # 수집된 URL 중에서 폴더 이름과 일치하는 URL 찾기
    for url in urls:
        if folder_name in url:
            return url

    print(f" [INFO] {folder_name}에 매칭되는 URL이 catalog_S1.json 파일에 없습니다.\n")
    return None

def create_folders_and_copy(data_folder, url, base_dir, user_selected_folder, index, total_files):
    print(" [STATUS] 진행 상태: {}/{}".format(index, total_files))
    print(" [INFO] URL: {}".format(url))
    
    # URL에서 상대 경로 및 파일 이름 생성
    relative_path = url.replace("https://download.limbuscompany.site/", "")
    folder_name = os.path.dirname(relative_path)
    file_name = os.path.basename(relative_path)

    # 저장할 폴더 경로 설정
    save_folder = os.path.join(user_selected_folder, folder_name)
    try:
        os.makedirs(save_folder, exist_ok=True)  # 폴더 생성
        print(" [INFO] 폴더 생성: {}".format(save_folder.replace('/', '\\')))
    except OSError as e:
        print(f" [ERROR] '{save_folder}' 폴더를 생성하는 데 문제가 발생했습니다: {e}\n")
        return

    data_file_path = os.path.join(data_folder, '__data')  # 원본 파일 경로 설정
    new_file_path = os.path.join(save_folder, file_name)  # 복사할 새 파일 경로 설정
    
    # 원본 파일 존재 여부 확인
    if not os.path.isfile(data_file_path):
        print(f" [ERROR] 원본 파일 '{data_file_path}'를 찾을 수 없습니다.\n")
        return

    try:
        shutil.copy(data_file_path, new_file_path)  # 파일 복사
        print(" [INFO] 원본 경로: {}".format(data_folder.replace('/', '\\')))
        print(" [INFO] 처리 경로: {}\n".format(new_file_path.replace('/', '\\')))
    except PermissionError:
        print(f" [ERROR] '{new_file_path}'에 쓰기 권한이 없습니다.\n")
    except FileNotFoundError:
        print(f" [ERROR] 원본 파일 '{data_file_path}'를 찾을 수 없습니다.\n")
    except IsADirectoryError:
        print(f" [ERROR] '{new_file_path}'는 파일이 아닌 디렉토리입니다.\n")
    except shutil.Error as e:
        print(f" [ERROR] 파일 복사 중 문제 발생: {e}\n")
    except Exception as e:
        print(f" [ERROR] 파일 복사 중 예기치 않은 오류가 발생했습니다: {e}\n")

def main():
    print("\n ===== LimbusCompany File Mapper =====")
    
    Tk().withdraw()  # Tkinter 창 숨기기
    base_dir = select_base_directory()  # 기본 디렉토리 선택
    json_data = load_json()  # JSON 데이터 로드
    
    print(" [INFO] 처리 된 파일 저장 경로 지정 단계")
    while True:
        # 사용자에게 처리된 파일 저장 경로 선택 요청
        user_selected_folder = askdirectory(title="처리 된 파일 저장 경로 지정")
        if user_selected_folder:
            print(f" [INFO] 처리 된 파일 저장 경로를 '{user_selected_folder}'로 지정했습니다.\n")
            break
        else:
            while True:
                choice = input(" [INFO] 처리 된 파일 저장 위치가 선택되지 않았습니다. 다시 선택하시겠습니까? (Y/N)\n >>> ").strip().lower()
                if choice == 'y':
                    break
                elif choice == 'n':
                    print(" [INFO] 프로그램을 종료합니다.")
                    exit(1)
                else:
                    print("\n [ERROR] 입력이 올바르지 않습니다. 'Y' 또는 'N'을 입력하세요.\n")

    data_folders = find_data_files(base_dir)  # '__data' 파일 검색

    total_files = len(data_folders)  # 총 파일 수 계산
    for index, data_folder in enumerate(data_folders, start=1):
        folder_name = os.path.basename(data_folder)  # 폴더 이름 추출
        url = find_matching_url(json_data, folder_name, index, total_files)  # URL 매칭
        if url:
            create_folders_and_copy(data_folder, url, base_dir, user_selected_folder, index, total_files)  # 파일 복사

    input(" [INFO] 작업이 완료되었습니다. Enter 키를 눌러 창을 종료하십시오.\n >>> ")

if __name__ == "__main__":
    main()  # 프로그램 시작
