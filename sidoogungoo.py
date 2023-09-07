#시도군구 모듈
import pyautogui
import re
from PIL import Image
import pytesseract


sidoo_idx_dic = { 
                    "강원특별자치도": 0, "경기도": 1, "경상남도": 2, 
                    "경상북도": 3,  "광주광역시": 4, "대구광역시": 5, 
                    "대전광역시": 6, "부산광역시": 7, "서울특별시": 8,
                    "세종특별자치시": 9, "울산광역시": 10, "인천광역시": 11,
                    "전라남도": 12, "전라북도": 13,"제주특별자치도": 14,   
                    "충청남도": 15,   "충청북도": 16
                }


sigungoo_list_dic = { 
                        0: ["강릉시", "고성군", "동해시", "삼척시", "속초시", "양구군", "양양군",
                            "영월군", "원주시", "인제군", "정선군", "철원군", "춘천시", "태백시",
                            "평창군", "홍천군", "화천군", "횡성군"],

                        1: ["가평군", "고양시 덕양구", "고양시 일산동구", "고양시 일산서구", "과천시",
                            "광명시", "광주시", "구리시", "군포시", "김포시", "남양주시", "동두천시", 
                            "부천시", "성남시 분당구", "성남시 수정구", "성남시 중원구", "수원시 권선구",
                            "수원시 영통구", "수원시 장안구", "수원시 팔달구", "시흥시", "안산시 단원구",
                            "안산시 상록구", "안성시", "안양시 동안구", "안양시 만안구", "양주시",
                            "양평군", "여주시", "연천군", "오산시", "용인시 기흥구", "용인시 수지구",
                            "용인시 처인구", "의왕시", "의정부시", "이천시", "파주시", "평택시",
                            "평택시 송탄출장소", "평택시 안중출장소", "포천시", "하남시", "화성시", "화성시 동부출장소", "화성시 동탄출장소"],

                        2: ["거제시", "거창군", "고성군", "김해시", "남해군", "밀양시", "사천시", "산청군",
                            "양산시", "의령군", "진주시", "창녕군", "창원시 마산합포구", "창원시 마산회원구",
                            "창원시 성산구", "창원시 의창구", "창원시 진해구", "통영시", "하동군", "함안군",
                            "함양군", "합천군"],

                        3: ["경산시", "경주시", "고령군", "구미시", "김천시", "문경시", "봉화군", "상주시", "성주군",
                            "안동시", "영덕군", "영양군", "영주시", "영천시", "예천군", "울릉군", "울진군", "의성군",
                            "청도군", "청송군", "칠곡군", "포항시 남구", "포항시 북구"],

                        4: ["광산구", "남구", "동구", "북구", "서구"],

                        5: ["군위군", "남구", "달서구", "달성군", "동구", "북구", "서구", "수성구", "중구"],

                        6: ["대덕구", "동구", "서구", "유성구", "중구"],

                        7: ["강서구", "금정구", "기장군", "남구", "동구", "동래구", "부산진구", "북구", 
                            "사상구", "사하구", "서구", "수영구", "연제구", "영도구", "중구", "해운대구"],
                        
                        8: ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구",
                            "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구",
                            "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"],

                        10: ["남구", "동구", "북구", "울주군", "중구"],

                        11: ["강화군", "계양구", "남동구", "동구", "미추홀구", "부평구", "서구", "연수구", "웅진군", "중구"],

                        12: ["강진군", "고흥군", "곡성군", "광양시", "구례군", "나주시", "담양군", "목포시", "무안군", "보성군", "순천시",
                             "신안군", "여수시", "영광군", "영암군", "완도군", "장성군", "장흥군", "진도군", "함평군", "해남군", "화순군"],

                        13: ["고창군", "군산시", "김제시", "남원시", "무주군", "부안군", "순창군", "완주군", 
                             "익산시", "임실군", "장수군", "전주시 덕진구", "전주시 완산구", "정읍시", "진안군"],

                        14: ["서귀포시", "제주시"],

                        15: ["계룡시", "공주시", "금산군", "논산시", "당진시", "보령시", "부여군",
                             "서산시", "서천군", "아산시", "예산군", "천안시 동남구", "천안시 서북구",
                             "청양군", "태안군", "홍성군"],

                        16: ["괴산군", "단양군", "보은군", "영동군", "옥천군", "음성군", "제천시",
                             "증평군", "진천군", "청주시 상당구", "청주시 서원구", "청주시 청원구", "청주시 흥덕구", "충주시"]
                        }


def get_sidoo_gungoo_loc_idx(addr):

    addr_unit_list = addr.split(" ")

    sidoo, gungoo = addr_unit_list[0], addr_unit_list[1]

    sidoo_loc_idx   = sidoo_idx_dic.get(sidoo, -1) # 예외처리 필요


    # 세종특별자치 예외처리
    if sidoo_loc_idx == 9:
        return 9, 0, addr_unit_list[1], re.sub(r"[^0-9-]", "", addr_unit_list[2].split("(")[0])
    
    
    gungoo_idx = 1
    if gungoo not in sigungoo_list_dic.get(sidoo_loc_idx):
        gungoo += " " + addr_unit_list[2]
        gungoo_idx += 1

    gungoo_loc_idx = sigungoo_list_dic.get(sidoo_loc_idx, []).index(gungoo) # 예외처리 필요


    # 구 다음 요소가 읍, 면으로 끝나는 경우 도로명은 구의 위치 + 2
    goo_next_str    = addr_unit_list[gungoo_idx + 1]
    load_name_idx   = gungoo_idx + 2 if (goo_next_str.endswith("읍") or goo_next_str.endswith("면")) else gungoo_idx + 1


    load_name   = addr_unit_list[load_name_idx]
    load_num    = re.sub(r"[^0-9-]", "", addr_unit_list[load_name_idx + 1].split("(")[0])

    return sidoo_loc_idx, gungoo_loc_idx, load_name, load_num


def get_addr_loc_idx(load_num):

    # 캡쳐
    left, top, width, height = 348, 460, 850, 442

    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save("addr_list.png")

    # ocr로 텍스트 받아오기
    text = pytesseract.image_to_string(Image.open("addr_list.png"), lang='kor')
    print(text)
    
    # 주소목록
    addr_list = [re.sub(r"[^0-9-]", "", addr.split(" (")[0].split(" ")[-1]) for addr in text.split("\n") if re.search(r"\d+", addr)]

    print("주소목록\n", addr_list)


    # 예외처리
    if load_num not in addr_list:
        return -1

    return addr_list.index(load_num)


def get_low_donglee_loc_idx(low_donglee):

    # 캡쳐
    left, top, width, height = 1025, 675, 290, 400

    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save("low_donglee.png")

    # ocr로 텍스트 받아오기
    text = pytesseract.image_to_string(Image.open("low_donglee.png"), lang='kor')

    # 법정동리목록
    low_donglee_list = [re.sub(r"\s+", "", low_donglee).split(")")[0] + ")" for low_donglee in text.split("\n") if re.sub(r"\s+", "", low_donglee) != "" and re.sub(r"\s+", "", low_donglee) != "[법정동리선택]"]
    print("법정동리 목록\n", low_donglee_list)

    for idx in range(0, len(low_donglee_list)):
        if low_donglee in low_donglee_list[idx]:
            return idx
    
    return -1
