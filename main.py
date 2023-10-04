# 지방세 신고 대상 엑셀 파일을 읽어서 순서대로 실행

import openpyxl
import singo


# 필요한 초기 정보 입력
file_path = input("===== 대상자 파일 입력:") + ".xlsx"
start_num = int(input("===== 시작 행 번호 입력: ").replace(" ", ""))
end_num = int(input("===== 마지막 행 번호 입력: ").replace(" ", ""))


# 엑셀 항목의 첫 번째 시트에 접근
try:
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
except Exception as e:
    print(e)
    print("===== 파일 제목과 시트를 확인해주세요 =====")


# 카테고리는 1번째 row에 존재
cate_tp = ws[1]


# 신고 상태 항목 추가
singo_status_col = len(cate_tp) + 1
ws.cell(row = 1, column = singo_status_col, value = "지방세 신고 상태")
wb.save(file_path)

singo_status_dic = {"1": "신고완료", "2": "신고미완료", "3": "종료"}


# 각 카테고리의 위치 저장
cate_idx_dic = {}
for idx in range(0, len(cate_tp)):
    cate_idx_dic[cate_tp[idx].value.replace(" ", "")] = idx


# 엑셀에 있는 정보로 지방세 신고 실행
for row_num in range(start_num, end_num + 1):

    print("\n===== 신고를 시작합니다 =====\n")

    target_tp = ws[row_num]

    target = singo.CorpSingo({

        "USER_NM":      target_tp[cate_idx_dic.get("이름")].value,
        "HP_NO":        target_tp[cate_idx_dic.get("연락처")].value.replace("-", ""),
        "CORP_NM":      target_tp[cate_idx_dic.get("사업장명")].value,
        "CORP_NO":      target_tp[cate_idx_dic.get("사업자번호")].value,
        "CORP_ADDR":    target_tp[cate_idx_dic.get("도로명주소")].value,
        "CORP_LB_ADDR": target_tp[cate_idx_dic.get("지번주소")].value,
        "HTX_REG_NO":   target_tp[cate_idx_dic.get("홈택스접수번호")].value,
        "TOT_HTAX_AMT": target_tp[cate_idx_dic.get("원천세신고금액")].value

    })

    target.singo()

    print("\n===== 제가 할 수 있는 것은 다 완료 했어요 :) =====\n===== 신고 정보를 확인하고 어드민에 저장해 주세요! =====\n")
    print("이름: "              , target.user_nm)
    print("연락처: "            , target.hp_no)
    print("사업장명: "          , target.corp_nm)
    print("사업자번호: "        , target.corp_no)
    print("도로명주소: "        , target.corp_addr)
    print("도로명주소: "        , target.corp_lb_addr)
    print("홈택스접수번호: "    , target.htx_reg_no)
    print("원천세신고금액: "    , target.tot_htax_amt)
    input("\n=====[[ Enter ]]=====\n")


    
    singo_status = input("1. 신고 완료! 다음 신고 시작!.\n2. 신고 미완료'^' 하지만 다음 신고 시작...\n3. 여기서 종료(__)\n").replace(" ", "")
    ws.cell(row = row_num, column = singo_status_col, value = singo_status_dic.get(singo_status, ""))
    wb.save(file_path)
    
    if singo_status == "3":
            print("===== 신고를 종료합니다. =====")
            break
    
    input("\n===== !!!!!!!신고 상태를 입력 하기 전에 지방세 프로그램을 재 실행해주세요!!!!!!! =====\n===== 다음 신고 준비 되었나요? =====\n=====[[ Enter ]]=====\n")


  

