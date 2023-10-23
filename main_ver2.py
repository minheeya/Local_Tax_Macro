# 지방세 신고 대상 정보 객체를 복사/붙여넣기 해서 신고 실행

import pyperclip
import singo



input("===== obj 복사 해주세요. =====\n===== 복사를 완료 하셨나요? [ENTER]")

obj_str         = pyperclip.paste().replace("{", "").replace("}", "")
obj_cate_list   = obj_str.split("\r\n")


target_info_dic = {}
for obj_cate in obj_cate_list:
    
    if obj_cate.count(":") != 1:
        continue

    obj_cate  = obj_cate.replace('"', "")
    key, val  = obj_cate.split(": ")

    target_info_dic[key.replace(" ", "")] = val.replace(",", "")


target = singo.CorpSingo(target_info_dic)
target.singo()


print("\n===== 제가 할 수 있는 것은 다 완료 했어요 :) =====\n===== 신고 정보를 확인하고 저장해 주세요! =====\n")
print("이름: "              , target.user_nm)
print("연락처: "            , target.hp_no)
print("사업장명: "          , target.corp_nm)
print("사업자번호: "        , target.corp_no)
print("도로명주소: "        , target.corp_addr)
print("도로명주소: "        , target.corp_lb_addr)
print("홈택스접수번호: "    , target.htx_reg_no)
print("원천세신고금액: "    , target.tot_htax_amt)
print("\n=====================\n")
