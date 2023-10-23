import pyautogui
import pyperclip
import time
import sidoogungoo
import config


pyautogui.PAUSE = 0.3


class CorpSingo:

    width_rat  = config.width_rat
    height_rat = config.height_rat

    button_loc_dic  = {
                        "next"                   : (1280 * width_rat, 1110 * height_rat),
                        "htx_singo_info_get"     : (1330 * width_rat, 360 * height_rat),
                        "htx_singo_info_load"    : (1120 * width_rat, 540 * height_rat),
                        "post_no"                : (555 * width_rat, 660 * height_rat),

                        "sido"      : (645 * width_rat, 310 * height_rat),
                        "sigungoo"  : (810 * width_rat, 310 * height_rat),
                        "addr_load" : (1125 * width_rat, 310 * height_rat),

                        "low_donglee"   : (1125 * width_rat, 700 * height_rat),
                        "certification" : (1400 * width_rat, 460 * height_rat),
                        "check_cert"    : (770 * width_rat, 675 * height_rat),

                        "submit": (1410 * width_rat, 1110 * height_rat)
                       }
    
    input_loc_dic   = {
                        "htx_reg_no" : (555 * width_rat, 540 * height_rat),
                        "corp_no"    : (555 * width_rat, 575 * height_rat),

                        "singo_user_rrno"        : (500 * width_rat, 255 * height_rat),
                        "singo_user_hpno"        : (500 * width_rat, 300 * height_rat),
                        "singo_user_nm"          : (1100 * width_rat, 255 * height_rat),
                        "singo_user_pw"          : (1100 * width_rat, 300 * height_rat),
                        "singo_user_rrno_half"   : (565 * width_rat, 255 * height_rat),
                       
                        "target_rrno"    : (500 * width_rat, 460 * height_rat),
                        "target_nm"      : (1100 * width_rat, 460 * height_rat),
                        "target_corp_nm" : (500 * width_rat, 575 * height_rat),

                        "load_name" : (920 * width_rat, 310 * height_rat),
                        "load_num"  : (510 * width_rat, 350 * height_rat)
                       }
    
    chk_loc_dic  = {
                        "back_num_chk": (770 * width_rat, 455 * height_rat)
                    }

    sido_sel_loc      = (550 * width_rat, 371 * height_rat)
    sigungoo_sel_loc  = (710 * width_rat, 371 * height_rat)
    sido_len        = 29 * height_rat
    sigungoo_len    = 28.5 * height_rat
    

    def __init__(self, singo_input_data: dict):
        
        self.htx_reg_no     = singo_input_data.get("HTX_REG_NO"     , "") if singo_input_data.get("HTX_REG_NO")     != None else ""
        self.tot_htax_amt   = singo_input_data.get("TOT_HTAX_AMT"   , "") if singo_input_data.get("TOT_HTAX_AMT")   != None else ""
        self.corp_no        = singo_input_data.get("CORP_NO"        , "") if singo_input_data.get("CORP_NO")        != None else ""
        self.corp_nm        = singo_input_data.get("CORP_NM"        , "") if singo_input_data.get("CORP_NM")        != None else ""
        self.user_nm        = singo_input_data.get("USER_NM"        , "") if singo_input_data.get("USER_NM")        != None else ""
        self.hp_no          = singo_input_data.get("HP_NO"          , "") if singo_input_data.get("HP_NO")          != None else ""
        self.corp_addr      = singo_input_data.get("CORP_ADDR"      , "") if singo_input_data.get("CORP_ADDR")      != None else ""
        self.corp_lb_addr   = singo_input_data.get("CORP_LB_ADDR"   , "") if singo_input_data.get("CORP_LB_ADDR")   != None else ""


    def click_next_bt(self):
        # main 페이지 다음 버튼 클릭

        pyautogui.click(CorpSingo.button_loc_dic.get("next"))


    def click_submit_bt(self):
        # 제출버튼 클릭

        pyautogui.moveTo(CorpSingo.button_loc_dic.get("submit"))


    def write_htx_singo_Info(self):
        # 홈택스신고정보가져오기

        # [홈택스신고정보가져오기] 버튼 클릭
        pyautogui.click(CorpSingo.button_loc_dic.get("htx_singo_info_get"))
        time.sleep(1)

        # 홈택스접수번호 입력
        pyautogui.click(CorpSingo.input_loc_dic.get("htx_reg_no"))
        pyautogui.write(self.htx_reg_no)
        
        #사업자번호 입력
        pyautogui.click(CorpSingo.input_loc_dic.get("corp_no"))
        pyautogui.write(self.corp_no)

        #[조회] 버튼 클릭
        pyautogui.click(CorpSingo.button_loc_dic.get("htx_singo_info_load"))

    def write_basic_info(self):
        # 신고인 정보, 특별징수의무자 인적사항 입력

        #주민/법인 등록번호 뒷번호 보이기
        pyautogui.click(CorpSingo.chk_loc_dic.get("back_num_chk"))
        time.sleep(0.1)


        # 특별징수의무자>상호
        pyperclip.copy(self.corp_nm)
        pyautogui.click(CorpSingo.input_loc_dic.get("target_corp_nm"))

        pyautogui.hotkey('ctrl', 'v')

        # 신고인 정보>주민번호
        pyautogui.doubleClick(CorpSingo.input_loc_dic.get("target_rrno"))
        pyautogui.hotkey('ctrl', 'c')

        rrno = pyperclip.paste()

        pyautogui.click(CorpSingo.input_loc_dic.get("singo_user_rrno"))
        pyautogui.hotkey('ctrl', 'v')


        # 신고인정보>이름 
        pyperclip.copy(self.user_nm)
        pyautogui.click(CorpSingo.input_loc_dic.get("singo_user_nm"))

        pyautogui.hotkey('ctrl', 'v')


        #신고인정보>전화번호
        pyautogui.click(CorpSingo.input_loc_dic.get("singo_user_hpno"))
        pyautogui.write(self.hp_no.replace("-", ""))


        #신고인정보>비밀번호
        pyperclip.copy(rrno[0:6])
        pyautogui.click(CorpSingo.input_loc_dic.get("singo_user_pw"))
        pyautogui.hotkey('ctrl', 'v')

    
    def check_cert(self):
        # 실명인증

        pyautogui.click(CorpSingo.button_loc_dic.get("certification"))
        time.sleep(1)

        pyautogui.click(CorpSingo.button_loc_dic.get("check_cert"))
        

    def write_corp_addr(self):
        # 사업장주소 검색 & 입력

        # [우편번호검색] 클릭
        pyautogui.click(CorpSingo.button_loc_dic.get("post_no"))
        time.sleep(1)


        # 시도 위치, 시군구 위치, 도로명, 건물본번
        sidoo_loc_idx, gungoo_loc_idx, load_name, load_num = sidoogungoo.get_sidoo_gungoo_loc_idx(self.corp_addr)


        # 시도 선택
        pyautogui.click(CorpSingo.button_loc_dic.get("sido"))

        x, y = CorpSingo.sido_sel_loc
        pyautogui.click(x, y + CorpSingo.sido_len * sidoo_loc_idx)
        

        # 시군구 선택
        pyautogui.click(CorpSingo.button_loc_dic.get("sigungoo"))

        x, y = CorpSingo.sigungoo_sel_loc
        pyautogui.click(x, y + CorpSingo.sigungoo_len * gungoo_loc_idx)


        # 도로명 입력
        pyperclip.copy(load_name)
        pyautogui.click(CorpSingo.input_loc_dic.get("load_name"))

        pyautogui.hotkey('ctrl', 'v')


        # 건물 본번 입력
        load_first_num = load_num.split("-")[0]
        pyperclip.copy(load_first_num)
        pyautogui.click(CorpSingo.input_loc_dic.get("load_num"))

        pyautogui.hotkey('ctrl', 'v')


        # 조회 버튼 클릭
        pyautogui.click(CorpSingo.button_loc_dic.get("addr_load"))


        # 상세 주소 여러개인 경우 여기서 종료
        if '-' in load_num:
            return
        

        # 상세 주소 첫 번째 조회되는 것 클릭
        pyautogui.doubleClick(720, 570)
        time.sleep(1)


        #--OCR 기능--#

        # 상세 주소 클릭
        #addr_loc_idx = sidoogungoo.get_addr_loc_idx(load_num)
        #pyautogui.doubleClick(720, 570 + 35 * addr_loc_idx)
        #time.sleep(1)


        # 법정동리 선택
        #pyautogui.click(CorpSingo.button_loc_dic.get("low_donglee"))
        #time.sleep(1)

        #low_donglee_idx = sidoogungoo.get_low_donglee_loc_idx(self.low_donglee)
        #pyautogui.click((1125, 758 + 30 * low_donglee_idx))
        #time.sleep(1)


        return


    def singo(self):

        self.click_next_bt()

        try:
            self.write_htx_singo_Info()
        except Exception as e:
            print("===== ", e, " =====")
            print("===== 사업자 번호 또는 홈택스 접수번호를 확인해주세요. =====\n")
            return
        
        
        try:
            self.write_basic_info()
        except Exception as e:
            print("===== ", e, " =====")
            print("===== 신고인 정보를 확인해주세요 =====\n")
            return


        try:
            self.check_cert()
        except Exception as e:
            print("===== ", e, " =====")
            print("===== 사장님 정보를 확인해주세요 =====\n")
            return


        try:
            self.write_corp_addr()
        except Exception as e:
            print("===== ", e, " =====")
            print("===== 사업장 주소를 확인해주세요 =====")
            print("===== 도로명 주소가 없다면 직접 입력해주세요 =====\n")
            return


        #self.click_next_bt()
        #self.click_next_bt()
        #self.click_submit_bt()

        


    
