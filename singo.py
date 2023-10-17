import pyautogui
import pyperclip
import time
import sidoogungoo

class CorpSingo:

    button_loc_dic  = {
                        "next"                   : (1280, 1110),
                        "htx_singo_info_get"     : (1330, 360),
                        "htx_singo_info_load"    : (1120, 540),
                        "post_no"                : (555, 660),

                        "sido"      : (645, 310),
                        "sigungoo"  : (810, 310),
                        "addr_load" : (1125, 310),

                        "low_donglee"   : (1125, 700),
                        "certification" : (1400, 460),
                        "check_cert"    : (770, 675),

                        "submit": (1410, 1110)
                       }
    
    input_loc_dic   = {
                        "htx_reg_no" : (555, 540),
                        "corp_no"    : (555, 575),

                        "singo_user_rrno"        : (500, 255),
                        "singo_user_hpno"        : (500, 300),
                        "singo_user_nm"          : (1100, 255),
                        "singo_user_pw"          : (1100, 300),
                        "singo_user_rrno_half"   : (565, 255),
                       
                        "target_rrno"    : (500, 460),
                        "target_nm"      : (1100, 460),
                        "target_corp_nm" : (500, 575),

                        "load_name" : (920, 310),
                        "load_num"  : (510, 350)
                       }
    
    
    sido_sel_loc      = (550, 371)
    sigungoo_sel_loc  = (710, 371)

    sido_len        = 29
    sigungoo_len    = 28.5
    

    def __init__(self, singo_input_data: dict):
        
        self.htx_reg_no     = singo_input_data.get("HTX_REG_NO"     , "")
        self.tot_htax_amt   = singo_input_data.get("TOT_HTAX_AMT"   , "")
        self.corp_no        = singo_input_data.get("CORP_NO"        , "")
        self.corp_nm        = singo_input_data.get("CORP_NM"        , "")
        self.user_nm        = singo_input_data.get("USER_NM"        , "")
        self.hp_no          = singo_input_data.get("HP_NO"          , "")
        self.corp_addr      = singo_input_data.get("CORP_ADDR"      , "")
        self.corp_lb_addr   = singo_input_data.get("CORP_LB_ADDR"   , "")


    def click_next_bt(self):
        # main 페이지 다음 버튼 클릭

        pyautogui.click(CorpSingo.button_loc_dic.get("next"))
        time.sleep(0.5)


    def click_submit_bt(self):
        # 제출버튼 클릭

        pyautogui.moveTo(CorpSingo.button_loc_dic.get("submit"))
        time.sleep(0.5)


    def write_htx_singo_Info(self):
        # 홈택스신고정보가져오기

        # [홈택스신고정보가져오기] 버튼 클릭
        pyautogui.click(CorpSingo.button_loc_dic.get("htx_singo_info_get"))
        time.sleep(1)

        # 홈택스접수번호 입력
        pyautogui.click(CorpSingo.input_loc_dic.get("htx_reg_no"))
        time.sleep(0.5)
        pyautogui.write(self.htx_reg_no)
        time.sleep(0.5)
        
        #사업자번호 입력
        pyautogui.click(CorpSingo.input_loc_dic.get("corp_no"))
        time.sleep(0.5)
        pyautogui.write(self.corp_no)
        time.sleep(0.5)

        #[조회] 버튼 클릭
        pyautogui.click(CorpSingo.button_loc_dic.get("htx_singo_info_load"))
        time.sleep(0.5)


    def write_basic_info(self):
        # 신고인 정보, 특별징수의무자 인적사항 입력


        # 특별징수의무자>상호
        pyperclip.copy(self.corp_nm)
        pyautogui.click(CorpSingo.input_loc_dic.get("target_corp_nm"))
        time.sleep(0.5)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)


        # 신고인 정보>주민번호
        pyautogui.doubleClick(CorpSingo.input_loc_dic.get("target_rrno"))
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)

        pyautogui.click(CorpSingo.input_loc_dic.get("singo_user_rrno"))
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)


        # 신고인정보>이름 
        pyperclip.copy(self.user_nm)
        pyautogui.click(CorpSingo.input_loc_dic.get("singo_user_nm"))
        time.sleep(0.5)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)


        #신고인정보>전화번호
        pyautogui.click(CorpSingo.input_loc_dic.get("singo_user_hpno"))
        time.sleep(0.5)
        pyautogui.write(self.hp_no)


        #신고인정보>비밀번호
        pass_d = CorpSingo.input_loc_dic.get("singo_user_rrno")[0] - CorpSingo.input_loc_dic.get("singo_user_rrno_half")[0]

        pyautogui.moveTo(CorpSingo.input_loc_dic.get("singo_user_rrno_half"))
        pyautogui.drag(pass_d, 0, duration=1.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)

        pyautogui.click(CorpSingo.input_loc_dic.get("singo_user_pw"))
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

    
    def check_cert(self):
        # 실명인증

        pyautogui.click(CorpSingo.button_loc_dic.get("certification"))
        time.sleep(1)

        pyautogui.click(CorpSingo.button_loc_dic.get("check_cert"))
        time.sleep(0.5)
        

    def write_corp_addr(self):
        # 사업장주소 검색 & 입력

        # [우편번호검색] 클릭
        pyautogui.click(CorpSingo.button_loc_dic.get("post_no"))
        time.sleep(1)


        # 시도 위치, 시군구 위치, 도로명, 건물본번
        sidoo_loc_idx, gungoo_loc_idx, load_name, load_num = sidoogungoo.get_sidoo_gungoo_loc_idx(self.corp_addr)


        # 시도 선택
        pyautogui.click(CorpSingo.button_loc_dic.get("sido"))
        time.sleep(0.5)

        x, y = CorpSingo.sido_sel_loc
        pyautogui.click(x, y + CorpSingo.sido_len * sidoo_loc_idx)
        time.sleep(0.5)
        

        # 시군구 선택
        pyautogui.click(CorpSingo.button_loc_dic.get("sigungoo"))
        time.sleep(0.5)

        x, y = CorpSingo.sigungoo_sel_loc
        pyautogui.click(x, y + CorpSingo.sigungoo_len * gungoo_loc_idx)
        time.sleep(0.5)


        # 도로명 입력
        pyperclip.copy(load_name)
        pyautogui.click(CorpSingo.input_loc_dic.get("load_name"))
        time.sleep(0.5)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)


        # 건물 본번 입력
        load_first_num = load_num.split("-")[0]
        pyperclip.copy(load_first_num)
        pyautogui.click(CorpSingo.input_loc_dic.get("load_num"))
        time.sleep(0.5)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)


        # 조회 버튼 클릭
        pyautogui.click(CorpSingo.button_loc_dic.get("addr_load"))
        time.sleep(0.5)


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
        self.write_htx_singo_Info()
        self.write_basic_info()
        self.check_cert()
        self.write_corp_addr()
        #self.click_next_bt()
        #self.click_next_bt()
        #self.click_submit_bt()

        


    
