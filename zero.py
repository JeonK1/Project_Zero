#아침에 비오는지 체크하는 기능 에러있음
from selenium import webdriver #외부
import pyowm #외부
import datetime
import pytz #외부
import os
import random
import re
import sqlite3
import sys
import threading
import time

class Zero:
    def printZero(self):
        print(' .    .')
        print('$&-  @&')
        print('e&&&@&&')
        print(' &&&&&@')
        print(' &&&&&#')
        print(' &&&&@i    &&%')
        print(' ?@&&@-    o &&')
        print(' &&&@&&&      &$')
        print(' &&&&&&&&i     @')
        print(' &&&@&&&&@`   -&')
        print(' =&&&&&&&&@   &')
        print('  &&&&&&&&@; &%')
        print('  &&&&&&@&@&O@')
        print('  @&&&&&&&&&&')
        print('  &@#&&&@&&@O    ####')
        print('  @@+&&&@&&&       #')
        print('  e&_&&&&&&&      #    ##  ###  ###')
        print('  -&:&&&&&@&      #   # #  #   #  #')
        print('  &&#&&&&&@e     #    ### #    #  #')
        print('  & &@&&&&#     ####  ### #    ###')
	########### 채팅 인식	###########
    def chkChat(self, order):
        if(self.chkAssign_add(order)==True):
            self.assignAdd() #과제 정보 추가 질의 이동
        elif(self.chkAssign_mod(order)==True):
            self.assignModDead()
        elif(self.chkAssignUpd_to(order)>=1): # 0(non), (update to 1~3 lv)
            self.assignUpdateLv(self.chkAssignUpd_to(order))
        elif(self.chkAssign_del(order)==True):
            self.assignDel()
        elif(self.chkTest_add(order)==True):
            self.testAdd()
        elif(self.chkTest_mod(order)==True):
            self.testMod()
        elif(self.chkTest_del(order)==True):
            self.testDel()
        elif(self.chkAssign_Info(order)==True):
            self.assignShow()
        elif(self.chkTest_Info(order)==True):
            self.testShow()
        elif(self.chkAssignSummary(order)==True):
            self.assignSummary()
        elif(self.chkTestSummary(order)==True):
            self.testSummary()
        elif(self.chkLinkReserv_add(order)==True):
            self.linkAdd()
        elif(self.chkLinkReserv_del(order)==True):
            self.linkDel()
        elif(self.chkLinkReserv_use(order)==True):
            linkName=input('링크명: ')
            self.linkUse(linkName)
        elif(self.chkAll_Info(order)==True):
            self.summaryShow()
        elif(self.chkNowTime(order)==True):
            self.printTime()
        elif(self.chkZeroOFF(order)==True):
            self.zeroOFF()
        elif(self.chkComOFF(order)==True):
            self.comOFF()
        elif(self.chkTemp(order)>0):
            self.printTemp(self.chkTemp(order))
        elif(self.chkClimate(order)>0):
            self.printClimate(self.chkClimate(order))
        elif(self.chkAlarm(order)==True):
            self.setAlarm()
    def chkAssign_add(self, order): #'과제정보 추가' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(과제)[a-zA-Z가-힣\s]*(등록|추가|생기|생겼|나왔)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
            print('\'chkAssign_add\' match!')
#            self.assignAdd() #과제 정보 추가 질의 이동
        else:
            return False
#            print('\'chkAssign_add\' not match')
    def chkAssign_mod(self, order): #'과제정보 수정' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(과제)[a-zA-Z가-힣\s]*(수정|바꾸|바꿔|변동|변경)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
            print('\'chkAssign_mod\' match!')
#            self.assignModDead() #과제 정보 수정 질의 이동
        else:
            return False
#            print('\'chkAssign_mod\' not match')
    def chkAssignUpd_to(self, order):  # '과제 (? > 진행중|완료|제출완료)' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(과제)[a-zA-Z가-힣\s]*(시작|진행)[a-zA-Z가-힣\s]*')
        chkHdler3 = re.compile('^[a-zA-Z가-힣\s]*(과제)[a-zA-Z가-힣\s]*(제출)[a-zA-Z가-힣\s]*')
        chkHdler2 = re.compile('^[a-zA-Z가-힣\s]*(과제)[a-zA-Z가-힣\s]*(끝|다했|완료|마쳤)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return 1
            print('\'chkAssignPro_to1\' match! ')
#            self.assignUpdateLv(1)
        elif(chkHdler3.match(order)):
            return 3
            print('\'chkAssignPro_to3\' match! ')
#            self.assignUpdateLv(3)
        elif(chkHdler2.match(order)):
            return 2
            print('\'chkAssignPro_to2\' match! ')
#            self.assignUpdateLv(2)
        else:
            return -1
#            print('\'chkAssignPro_to\' not match! ')
    def chkAssign_del(self, order): #'과제정보 삭제' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(과제)[a-zA-Z가-힣\s]*(삭제|제거|마감|없|사라|취소|지워)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
            print('\'chkAssign_del\' match!')
#            self.assignDel() #과제 정보 삭제 질의 이동
        else:
            return False
#            print('\'chkAssign_del\' not match')
    def chkTest_add(self, order): #'시험정보 추가' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(시험)[a-zA-Z가-힣\s]*(등록|추가|생기|생겼|나왔)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
#			print('\'chkTest_add\' match!')
#			self.testAdd() #시험정보 추가 질의 이동
        else:
            return False
#            print('\'chkTest_add\' not match')
    def chkTest_mod(self, order): #'시험정보 수정' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(시험)[a-zA-Z가-힣\s]*(수정|바꾸|바꿔|변동|변경)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
#            print('\'chkTest_mod\' match!')
#            self.testMod() #시험정보 수정 질의 이동
        else:
            return False
#            print('\'chkTest_mod\' not match')
    def chkTest_del(self, order): #'시험정보 삭제' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(시험)[a-zA-Z가-힣\s]*(삭제|제거|마감|없|사라|취소|지워)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
#            print('\'chkTest_del\' match!')
#            self.testDel() #시험정보 삭제 질의 이동
        else:
            return False
#            print('\'chkTest_del\' not match')
    def chkAssign_Info(self, order): #'과제정보 확인' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(과제)[a-zA-Z가-힣\s]*(확인|뭐 있|뭐있|뭐 남았|보여|보기|리스트)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
#            print('\'chkAssign_Info\' match!')
#            self.assignShow() #과제정보 출력
        else:
            return False
#            print('\'chkAssign_Info\' not match')
    def chkTest_Info(self, order): #'시험정보 확인' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(시험)[a-zA-Z가-힣\s]*(확인|뭐 있어|뭐 남았|보여|리스트)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
#            print('\'chkTest_Info\' match!')
#            self.testShow() #시험정보 출력
        else:
            return False
#            print('\'chkTest_Info\' not match')
    def chkAssignSummary(self, order):
        order = order.strip()
        chkHdler1 = re.compile('^(과제)$')
        if(chkHdler1.match(order)):
            return True
#            print('\'chkAssign_Info\' match!')
            self.assignShow() #과제정보 출력
        else:
            return False
    def chkTestSummary(self, order):
        chkHdler1 = re.compile('^(시험)$')
        if(chkHdler1.match(order)):
            return True
#            print('\'chkTest_Info\' match!')
            self.testShow() #시험정보 출력
        else:
            return False
    def chkLinkReserv_add(self, order): #'링크 추가' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(링크|예약어)[a-zA-Z가-힣\s]*(등록|추가)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
#            print('\'chkLinkReserv_add\' match!')
#            self.linkAdd() #링크 정보 추가 질의 이동
        else:
            return False
#            print('\'chkLinkReserv_add\' not match')
    def chkLinkReserv_del(self, order): #'링크 삭제' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(링크|예약어)[a-zA-Z가-힣\s]*(삭제|제거|지워|없애)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
#            print('\'chkLinkReserv_del\' match!')
#            self.linkDel() #링크 정보 삭제 질의 이동
        else:
            return False
#            print('\'chkLinkReserv_add\' not match')
    def chkLinkReserv_use(self, order):
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(링크|예약어)[a-zA-Z가-힣\s]*(사용|이동|쓰기)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
#            print('\'chkLinkReserv_use\' match!')
#            self.linkUse() #링크 연결 이동
        else:
            return False
#            print('\'chkLinkReserv_use\' not match')
    def chkAll_Info(self, order): #'종합 정보 확인' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^[a-zA-Z가-힣\s]*(공지)[a-zA-Z가-힣\s]*(보고|확인|알려)[a-zA-Z가-힣\s]*')
        chkHdler2 = re.compile('^(내가 알아야할)[a-zA-Z가-힣\s]*')
        chkHdler3 = re.compile('^(공지|전체요약|전체 요약)$')
        if(chkHdler1.match(order)):
            return True
#            print('\'chkAll_Info\' match!')
#            self.summaryShow() #종합정보 출력
        elif(chkHdler2.match(order)):
            return True
#            print('\'chkAll_Info\' match!')
#            self.summaryShow() #종합정보 출력
        elif(chkHdler3.match(order)):
            return True
#            print('\'chkAll_Info\' match!')
#            self.summaryShow() #종합정보 출력
        else:
            return False
#            print('\'chkAll_Info\' not match')
    def chkYes(self, order): #'예' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^(y|ok|yes)$', re.I)
        chkHdler2 = re.compile('^(ㅇ|ㅇㅇ|그렇게|응|예|네)[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
#            print('\'Yes\' match!')
        elif(chkHdler2.match(order)):
            return True
#            print('\'Yes\' match')
        else:
            return False
#            print('\'Yes\' not match')
    def chkNo(self, order): #'아니오' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^(n|no)$', re.I)
        chkHdler2 = re.compile('^(ㄴ|ㄴㄴ|아니|안돼|안되|하지마|싫어)\s?[a-zA-Z가-힣\s]*')
        if(chkHdler1.match(order)):
            return True
#            print('\'No\' match!')
        elif(chkHdler2.match(order)):
            return True
#            print('\'No\' match!')
        else:
            return False
#            print('\'No\' not match')
    def chkNowTime(self, order):
        order = order.strip()
        chkHdler1 = re.compile('^(현재 시간|현재시간|시간|현재 시각|현재시각|시각)$')
        chkHdler2 = re.compile('^[a-zA-Z가-힣\s]*(몇 시|몇시)[a-zA-Z가-힣]*')
        if(chkHdler1.match(order)):
            return True
#            print('\'chkNowTime\' match!')
#            self.printTime() #현재 시간
        elif(chkHdler2.match(order)):
            return True
#            print('\'chkNowTime\' match!')
#            self.printTime() #현재 시간
        else:
            return False
#            print('\'chkNowTime\' not match!')
    def chkZeroOFF(self, order): #'프로그램종료' 판단함수
        order = order.strip()
        chkHdler1 = re.compile('^(제로|zero)[a-zA-Z가-힣\s]*(잘가|잘있어|퇴근|꺼|종료)[a-zA-Z가-힣\s]*', re.I)
        chkHdler2 = re.compile('^(프로그램)[a-zA-Z가-힣\s]*(꺼|종료)[a-zA-Z가-힣\s]*')
        chkHdler3 = re.compile('^(퇴근|종료|quit|off)$', re.I)
        if(chkHdler1.match(order)):
            return True
#            print('\'ZeroOFF\' match!')
#            self.zeroOFF()
        elif(chkHdler2.match(order)):
            return True
#            print('\'ZeroOFF\' match!')
#            self.zeroOFF()
        elif(chkHdler3.match(order)):
            return True
#            print('\'ZeroOFF\' match!')
#            self.zeroOFF()
        else:
            return False
            print('\'ZeroOFF\' not match')
    def chkComOFF(self, order): #'컴퓨터종료' 판단함수
        order = order.strip()
        chkHdler = re.compile('^(컴|컴퓨터)[a-zA-Z가-힣\s]*(꺼|종료)[a-zA-Z가-힣\s]*')
        if(chkHdler.match(order)):
            return True
#            print('\'ComOFF\' match!')
#            self.comOFF()
        else:
            return False
#            print('\'ComOFF\' not match')
    def chkClimate(self, order):
        order = order.strip()
        chkHdler1_1 = re.compile('^[a-zA-Z가-힣\s]*(오늘)[a-zA-Z가-힣\s]*(날씨)[a-zA-Z가-힣\s]*')
        chkHdler1_2 = re.compile('^(지금 날씨|지금날씨)$')
        chkHdler1_3 = re.compile('^[a-zA-Z가-힣\s]*(지금|현재)[a-zA-Z가-힣\s]*(날씨)[a-zA-Z가-힣\s]*')
        chkHdler2 = re.compile('^[a-zA-Z가-힣\s]*(내일)[a-zA-Z가-힣\s]*(날씨)[a-zA-Z가-힣\s]*')
        #chkHdler1 :  오늘 날씨 출력
        #chkHdler2 :  내일 날씨 출력
        if(chkHdler1_1.match(order)):
            return 1
#            print('\'chkClimate_Today\' match')
#            self.printClimate(TODAY)
        elif(chkHdler1_2.match(order)):
            return 1
#            print('\'chkNowClimate\' match!')
#            self.printNowClimate(TODAY)
        elif(chkHdler1_3.match(order)):
            return 1
#            print('\'chkNowClimate\' match!')
#            self.printNowClimate(TODAY)
        elif(chkHdler2.match(order)):
            return 2
#            print('\'chkClimate_Tomorrow\' match')
#            self.printClimate(TOMORROW)
        else:
            return -1
#            print('\'chkClimate\' not match')
    def chkTemp(self, order):
        order = order.strip()
        chkHdler1_1 = re.compile('^[a-zA-Z가-힣\s]*(오늘)[a-zA-Z가-힣\s]*(온도|추|더|춥|덥|쌀쌀|따뜻|따스|따듯)[a-zA-Z가-힣\s]*')
        chkHdler1_2 = re.compile('^[a-zA-Z가-힣\s]*(지금|현재)[a-zA-Z가-힣\s]*(온도)[a-zA-Z가-힣\s]*')
        chkHdler2 = re.compile('^[a-zA-Z가-힣\s]*(내일)[a-zA-Z가-힣\s]*(온도|추|더|춥|덥|쌀쌀|따뜻|따스|따듯)[a-zA-Z가-힣\s]*')
        #chkHdler1 : 오늘 최고/최저온도 확인
        #chkHdler2 : 내일 최고/최저온도 확인
        if(chkHdler1_1.match(order)):
            return 1
#            print('\'chkTemp_Today\' match!')
#            self.printTemp(TODAY) #오늘 최고/최저 온도
        elif(chkHdler1_2.match(order)):
            return 1
#            print('\'chkTemp_Tomorrow\' match!')
#            self.printTemp(TODAY)
        elif(chkHdler2.match(order)):
            return 2
#            print('\'chkTemp_Tomorrow\' match!')
#            self.printTemp(TOMORROW)
        else:
            return -1
#            print('\'chkTemp\' not match')
    def chkCancel(self, order):
        order=order.strip()
        chkHdler1=re.compile('(취소|나가기)')
        if(chkHdler1.match(order)):
            return True
        else:
            return False
    def chkAlarm(self, order):
        order=order.strip()
        chkHdler1=re.compile('(알람설정|알람 설정)')
        if(chkHdler1.match(order)):
            return True
        else:
            return False
 	######### Database 관리	#########
		##### 과제 Database #####
    def assignAdd(self): #과제 추가
        assignName=input('과제 이름 : ').lower()
        if(self.chkCancel(assignName)==True):
            return -1
        subName=input('과목 이름 : ').lower()
        if(self.chkCancel(subName)==True):
            return -1
        subGroup=input('과목 분류(전공|교양) : ')
        if(self.chkCancel(subGroup)==True):
            return -1
        while(subGroup!='전공' and subGroup!='교양'):
            print('잘못된 입력값입니다.')
            subGroup=input('과목 분류(전공|교양) : ')
            if(self.chkCancel(subGroup)==True):
                return -1
        deadDate=input('마감날짜(ex-2010-01-01) : ')
        if(self.chkCancel(deadDate)==True):
            return -1
        while(self.isDate(deadDate)==False):
            if(deadDate==''): #입력값 없으면 NULL
                break
            print('잘못된 형식입니다.')
            deadDate=input('마감날짜(ex-2010-01-01) : ')
            if(self.chkCancel(deadDate)==True):
                return -1
        deadTime=input('마감시간(ex-13:00) : ')
        if(self.chkCancel(deadTime)==True):
            return -1
        while(self.isTime(deadTime)==False):
            if(deadTime==''): #입력값 없으면 NULL
                break
            print('잘못된 형식입니다.')
            deadTime=input('마감시간(ex-13:00) : ')
            if(self.chkCancel(deadTime)==True):
                return -1
        submitWay=input('제출방식(온라인|오프라인) : ')
        if(self.chkCancel(submitWay)==True):
            return -1
        while(submitWay!='온라인' and submitWay!='오프라인'):
            print('잘못된 입력값입니다.')
            submitWay=input('제출방식(온라인|오프라인) : ')
            if(self.chkCancel(submitWay)==True):
                return -1
        progress=0 # 0(1도안함), 1(진행중), 2(완료), 3(제출완료)
        print("-------------------------------------")
        print("**과제 등록**")
        print("과제이름: "+assignName)
        print("과목이름: "+subName+"("+subGroup+")")
        print("마감기한: "+deadDate+" "+deadTime)
        print("-------------------------------------")
        if(self.askIsOK()==0):
            return -1
        #DB연결
        DBName = 'mySchedule.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #db파일에서 myAssign이 없으면 만들어주기
        SQLquery = "create table if not exists myAssign("
        SQLquery += "assignName TEXT NOT NULL, "
        SQLquery += "subName TEXT NOT NULL, "
        SQLquery += "subGroup TEXT NOT NULL, "
        SQLquery += "deadDate TEXT, "
        SQLquery += "deadTime TEXT, "
        SQLquery += "submitWay TEXT NOT NULL, "
        SQLquery += "progress INTEGER NOT NULL, "
        SQLquery += "PRIMARY KEY (assignName)"
        SQLquery += ");"
        myDBCur.execute(SQLquery)
        #db파일에 입력받은 값 삽입
        SQLquery = "insert into myAssign(assignName, subName, subGroup, deadDate, deadTime, submitWay, progress) values(?,?,?,?,?,?,?);"
        myDBCur.execute(SQLquery, (assignName, subName, subGroup, deadDate, deadTime, submitWay, progress) )
        print("삽입완료")
        myDB.commit()
        myDB.close()
    def assignModDead(self): #과제 마감기한 변경
        DBName = 'mySchedule.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #db파일에서 myAssign이 없으면 만들어주기
        SQLquery = "create table if not exists myAssign("
        SQLquery += "assignName TEXT NOT NULL, "
        SQLquery += "subName TEXT NOT NULL, "
        SQLquery += "subGroup TEXT NOT NULL, "
        SQLquery += "deadDate TEXT, "
        SQLquery += "deadTime TEXT, "
        SQLquery += "submitWay TEXT NOT NULL, "
        SQLquery += "progress INTEGER NOT NULL, "
        SQLquery += "PRIMARY KEY (assignName)"
        SQLquery += ");"
        myDBCur.execute(SQLquery)
        #과제이름 나열
        assignList = myDBCur.execute("select assignName, subName from myAssign;")
        print('=== 현재 등록된 과제명 ===')
        for assignName in assignList:
            print(assignName[0]+"("+assignName[1]+")")
        print('=========================')
        modName = input("마감날짜 및 시간을 변경하고 싶은 과제이름 : ").lower()
        if(self.chkCancel(modName)==True):
            return -1
        while(self.findInList(assignList, modName)==False):
            print('테이블 내에 없는 과제이름입니다.')
            modName = input("마감날짜 및 시간을 변경하고 싶은 과제이름 : ").lower()
            if(self.chkCancel(modName)==True):
                return -1
        #새로운 마감날짜 받기
        answers = myDBCur.execute("select deadDate from myAssign where assignName=(?);", (modName,))
        for ans in answers:
            beforeDate=ans[0]
        dataInputMessage=beforeDate+"(enter=이전값)"+" >> "
        afterDate=input(dataInputMessage)
        if(self.chkCancel(afterDate)==True):
            return -1
        while(self.isDate(afterDate)==False):
            if(afterDate==''):
                afterDate=beforeDate
                break
            print('잘못된 형식입니다.')
            afterDate=input(dataInputMessage)
            if(self.chkCancel(afterDate)==True):
                return -1
        #새로운 마감시간 받기
        answers = myDBCur.execute("select deadTime from myAssign where assignName=(?);", (modName,))
        for ans in answers:
            beforeTime=ans[0]
        dataInputMessage=beforeTime+"(enter=이전값)"+" >> "
        afterTime=input(dataInputMessage)
        if(self.chkCancel(afterTime)==True):
            return -1
        while(self.isTime(afterTime)==False):
            if(afterTime==''):
                afterTime=beforeTime
                break
            print('잘못된 형식입니다.')
            afterTime=input(dataInputMessage)
            if(self.chkCancel(afterTime)==True):
                return -1
        print("-------------------------------------")
        print("**마감기한 변경**")
        print(beforeDate+" "+beforeTime+" >> "+afterDate+ " "+afterTime)
        print("-------------------------------------")
        if(self.askIsOK()==0):
            return -1
        #새로운 마감날짜, 마감시간 update
        myDBCur.execute("update myAssign set deadDate=(?), deadTime=(?) where assignName=(?)", (afterDate, afterTime, modName,))
        print("변경완료")
        myDB.commit()
        myDB.close()
    def assignUpdateLv(self, lv): #과제 진행상태 변경(lv은 진행상태(1~3))
        if(lv==1):
            state="진행중인"
        elif(lv==2):
            state="완료한"
        elif(lv==3):
            state="제출완료한"
        else:
            print("보낸 인자값이 잘못되었습니다.")
            return -1
        DBName = 'mySchedule.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #db파일에서 myAssign이 없으면 만들어주기
        SQLquery = "create table if not exists myAssign("
        SQLquery += "assignName TEXT NOT NULL, "
        SQLquery += "subName TEXT NOT NULL, "
        SQLquery += "subGroup TEXT NOT NULL, "
        SQLquery += "deadDate TEXT, "
        SQLquery += "deadTime TEXT, "
        SQLquery += "submitWay TEXT NOT NULL, "
        SQLquery += "progress INTEGER NOT NULL, "
        SQLquery += "PRIMARY KEY (assignName)"
        SQLquery += ");"
        myDBCur.execute(SQLquery)
        #과제이름 리스트 출력
        assignList = myDBCur.execute("select assignName, subName from myAssign;")
        zeroMent="어떤 과제가 "+state+" 과제인가요?"
        print(zeroMent)
        print('=== 현재 등록된 과제명 ===')
        for assignName in assignList:
            print(assignName[0]+"("+assignName[1]+")")
        print('=========================')
        inputMessage=state+" 과제 이름 : "
        updName = input(inputMessage)
        if(self.chkCancel(updName)==True):
            return -1
        while(self.findInList(assignList, updName)==False):
            print('테이블 내에 없는 과제 이름입니다.')
            updName = input(inputMessage)
            if(self.chkCancel(updName)==True):
                return -1
        myDBCur.execute("update myAssign set progress=(?) where assignName=(?);", (lv, updName,))
        print("업데이트 완료")
        myDB.commit()
        myDB.close()
    def assignDel(self): #과제 삭제
        DBName = 'mySchedule.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #db파일에서 myAssign이 없으면 만들어주기
        SQLquery = "create table if not exists myAssign("
        SQLquery += "assignName TEXT NOT NULL, "
        SQLquery += "subName TEXT NOT NULL, "
        SQLquery += "subGroup TEXT NOT NULL, "
        SQLquery += "deadDate TEXT, "
        SQLquery += "deadTime TEXT, "
        SQLquery += "submitWay TEXT NOT NULL, "
        SQLquery += "progress INTEGER NOT NULL, "
        SQLquery += "PRIMARY KEY (assignName)"
        SQLquery += ");"
        myDBCur.execute(SQLquery)
        #과제이름 리스트 출력
        assignList = myDBCur.execute("select assignName, subName from myAssign;")
        print('=== 현재 등록된 과제명 ===')
        for assignName in assignList:
            print(assignName[0]+"("+assignName[1]+")")
        print('=========================')
        delName = input("삭제하고싶은 과제이름 : ")
        if(self.chkCancel(delName)==True):
            return -1
        while(self.findInList(assignList, delName)==False):
            print('테이블 내에 없는 과제 이름입니다.')
            delName = input("삭제하고싶은 과제이름 : ")
            if(self.chkCancel(delName)==True):
                return -1
        print("-------------------------------------")
        print("**과제 삭제**")
        print("과제명: "+delName)
        print("-------------------------------------")
        if(self.askIsOK()==0):
            return -1
        myDBCur.execute("delete from myAssign where assignName=(?);", (delName,))
        print("삭제완료")
        myDB.commit()
        myDB.close()
        ##### 시험 Database #####
    def testAdd(self): #시험 추가
        testName=input('시험 이름 : ').lower()
        if(self.chkCancel(testName)==True):
            return -1
        subName=input('과목 이름 : ').lower()
        if(self.chkCancel(subName)==True):
            return -1
        subGroup=input('과목 분류(전공|교양) : ')
        if(self.chkCancel(subGroup)==True):
            return -1
        while(subGroup!='전공' and subGroup!='교양'):
            print('잘못된 입력값입니다.')
            subGroup=input('과목 분류(전공|교양) : ')
            if(self.chkCancel(subGroup)==True):
                return -1
        testDate=input('시험날짜(ex-2010-01-01) : ')
        if(self.chkCancel(testDate)==True):
            return -1
        while(self.isDate(testDate)==False):
            print('잘못된 형식입니다.')
            deadDate=input('시험날짜(ex-2010-01-01) : ')
            if(self.chkCancel(deadDate)==True):
                return -1
        testTime=input('시험시간(ex-13:00) : ')
        if(self.chkCancel(testTime)==True):
            return -1
        while(self.isTime(testTime)==False):
            print('잘못된 형식입니다.')
            testTime=input('시험시간(ex-13:00) : ')
            if(self.chkCancel(testTime)==True):
                return -1
        testPlace=input('시험장소 : ')
        if(self.chkCancel(testPlace)==True):
            return -1
        print("-------------------------------------")
        print("**시험정보 추가**")
        print("시험이름: "+testName)
        print("과목이름: "+subName+"("+subGroup+")")
        print("시험일자: "+testDate+" "+testTime)
        print("시험장소: "+testPlace)
        print("-------------------------------------")
        if(self.askIsOK()==0):
            return -1
        #DB연결
        DBName = 'mySchedule.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #db파일에서 myTest이 없으면 만들어주기
        myDBCur.execute("create table if not exists myTest(testName TEXT NOT NULL, subName TEXT NOT NULL, subGroup TEXT NOT NULL, testDate TEXT, testTime TEXT, testPlace TEXT, PRIMARY KEY (testName));")
        #db파일에 입력받은 값 삽입
        myDBCur.execute("insert into myTest(testName, subName, subGroup, testDate, testTime, testPlace) values(?,?,?,?,?,?);", (testName, subName, subGroup, testDate, testTime, testPlace,))
        print("삽입완료")
        myDB.commit()
        myDB.close()
    def testMod(self): #시험 정보 변경
        DBName = 'mySchedule.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #db파일에서 myTest이 없으면 만들어주기
        myDBCur.execute("create table if not exists myTest(testName TEXT NOT NULL, subName TEXT NOT NULL, subGroup TEXT NOT NULL, testDate TEXT, testTime TEXT, testPlace TEXT, PRIMARY KEY (testName));")
        #시험이름 나열
        testList = myDBCur.execute("select testName, subName from myTest;")
        print('=== 현재 등록된 시험명 ===')
        for testName in testList:
            print(testName[0]+"("+testName[1]+")")
        print('=========================')
        modName = input("시험정보를 변경하고 싶은 시험이름 : ").lower()
        while(self.findInList(testList, modName)==False):
            print('테이블 내에 없는 시험이름입니다.')
            modName = input("시험정보를 변경하고 싶은 시험이름 : ").lower()
        #새로운 시험정보 받기
        answers = myDBCur.execute("select testDate from myTest where testName=(?);", (modName,))
        for ans in answers:
            beforeDate=ans[0]
        dataInputMessage=beforeDate+"(enter=이전값)"+" >> "
        afterDate=input(dataInputMessage)
        if(self.chkCancel(afterDate)==True):
            return -1
        while(self.isDate(afterDate)==False):
            if(afterDate==''):
                afterDate=beforeDate
                break
            print('잘못된 형식입니다.')
            afterDate=input(dataInputMessage)
            if(self.chkCancel(afterDate)==True):
                return -1
        #새로운 시험시간 받기
        answers = myDBCur.execute("select testTime from myTest where testName=(?);", (modName,))
        for ans in answers:
            beforeTime=ans[0]
        dataInputMessage=beforeTime+"(enter=이전값)"+" >> "
        afterTime=input(dataInputMessage)
        if(self.chkCancel(afterTime)==True):
            return -1
        while(self.isTime(afterTime)==False):
            if(afterTime==''):
                afterTime=beforeTime
                break
            print('잘못된 형식입니다.')
            afterTime=input(dataInputMessage)
            if(self.chkCancel(afterTime)==True):
                return -1
        #새로운 시험장소 받기
        answers = myDBCur.execute("select testPlace from myTest where testName=(?);", (modName,))
        for ans in answers:
            beforePlace=ans[0]
        afterPlace=input(beforePlace+"(enter=이전값)"+" >> ")
        if(self.chkCancel(afterPlace)==True):
            return -1
        if(afterPlace==''):
            afterPlace=beforePlace
        print("-------------------------------------")
        print("**시험정보 수정**")
        print("시험일자: "+beforeDate+" "+beforeTime+" >> "+afterDate+" "+afterTime)
        print("시험장소: "+beforePlace+" >> "+afterPlace)
        print("-------------------------------------")
        if(self.askIsOK()==0):
            return -1
        #새로운 마감날짜, 마감시간 update
        myDBCur.execute("update myTest set testDate=(?), testTime=(?), testPlace=(?) where testName=(?);", (afterDate, afterTime, afterPlace, modName,))
        print("변경완료")
        myDB.commit()
        myDB.close()
    def testDel(self): #시험 삭제
        DBName = 'mySchedule.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #db파일에서 myTest이 없으면 만들어주기
        myDBCur.execute("create table if not exists myTest(testName TEXT NOT NULL, subName TEXT NOT NULL, subGroup TEXT NOT NULL, testDate TEXT, testTime TEXT, testPlace TEXT, PRIMARY KEY (testName));")
        #시험이름 리스트 출력
        testList = myDBCur.execute("select testName, subName from myTest;")
        print('=== 현재 등록된 시험명 ===')
        for testName in testList:
            print(testName[0]+"("+testName[1]+")")
        print('=========================')
        delName=input("삭제하고싶은 시험이름 : ")
        if(self.chkCancel(delName)==True):
            return -1
        while(self.findInList(testList, delName)==False):
            print('테이블 내에 없는 시험이름입니다.')
            delName=input("삭제하고싶은 시험이름 : ")
            if(self.chkCancel(delName)==True):
                return -1
        print("-------------------------------------")
        print("**시험정보삭제**")
        print("시험이름: "+delName)
        print("-------------------------------------")
        if(self.askIsOK()==0):
            return -1
        myDBCur.execute("delete from myTest where testName=(?);", (delName,))
        print("삭제완료")
        myDB.commit()
        myDB.close()
		##### 링크 Database #####
    def linkAdd(self):
        linkName = input('링크 예약어 명 : ').lower()
        if(self.chkCancel(linkName)==True):
            return -1
        linkURL = input('링크 주소 : ')
        if(self.chkCancel(linkURL)==True):
            return -1
        #DB연결
        DBName = 'myLinkList.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #없다면 new table 생성
        SQLquery = "create table if not exists myLink("
        SQLquery += "word TEXT NOT NULL, "
        SQLquery += "link TEXT NOT NULL, "
        SQLquery += "PRIMARY KEY (word)"
        SQLquery += ");"
        myDBCur.execute(SQLquery)
        #데이터 삽입
        myDBCur.execute("insert into myLink(word, link) values(?,?);", (linkName, linkURL))
        print("삽입완료")
        myDB.commit()
        myDB.close()
    def linkDel(self):
        #DB연결
        DBName = 'myLinkList.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #없다면 new table 생성
        SQLquery = "create table if not exists myLink("
        SQLquery += "word TEXT NOT NULL, "
        SQLquery += "link TEXT NOT NULL, "
        SQLquery += "PRIMARY KEY (word)"
        SQLquery += ");"
        myDBCur.execute(SQLquery)
        #link 리스트 출력
        wordList = myDBCur.execute("select word from myLink")
        print('=== 현재 등록된 링크명 ===')
        for word in wordList:
            print(word[0])
        print('=========================')
        #제거할 단어값 입력
        delWord = input("제거할 링크 예약어 : ")
        if(self.chkCancel(delWord)==True):
            return -1
        while(self.findInList(wordList, delWord)==False):
            print("테이블 내에 없는 예약어입니다.")
            delWord = input("제거할 링크 예약어 : ")
            if(self.chkCancel(delWord)==True):
                return -1
        myDBCur.execute("delete from myLink where word=(?);",(delWord,))
        print("제거완료")
        myDB.commit()
        myDB.close()
    def linkUse(self, inputWord):
        if(self.chkCancel(inputWord)==True):
            return -1
        inputWord = inputWord.strip()
        #DB연결
        DBName = 'myLinkList.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #없다면 new table 생성
        SQLquery = "create table if not exists myLink("
        SQLquery += "word TEXT NOT NULL, "
        SQLquery += "link TEXT NOT NULL, "
        SQLquery += "PRIMARY KEY (word)"
        SQLquery += ");"
        myDBCur.execute(SQLquery)
        ansCnt = myDBCur.execute("select count(link) from myLink where word=(?);", (inputWord,))
        for answerCnt in ansCnt:
            linkCnt=answerCnt[0]
        if(linkCnt==0):
            print("예약어에 해당하는 값이 없습니다.")
            return -1
        elif(linkCnt>1):
            print("예약어에 해당하는 값이 2개가 넘습니다. 소스코드확인 바랍니다.")
            return -1
        ans = myDBCur.execute("select link from myLink where word=(?);", (inputWord,))
        for answer in ans:
            tLink=answer[0]  #targetLink 얻음
        myDriver = webdriver.Chrome("C:\Download\chromedriver.exe")
        myDriver.get(tLink)
        ##### Database Show #####
    def assignShow(self): #과제세부정보 보여주기
        #DB연결
        DBName = 'mySchedule.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #db파일에서 myAssign이 없으면 만들어주기
        SQLquery = "create table if not exists myAssign("
        SQLquery += "assignName TEXT NOT NULL, "
        SQLquery += "subName TEXT NOT NULL, "
        SQLquery += "subGroup TEXT NOT NULL, "
        SQLquery += "deadDate TEXT, "
        SQLquery += "deadTime TEXT, "
        SQLquery += "submitWay TEXT NOT NULL, "
        SQLquery += "progress INTEGER NOT NULL, "
        SQLquery += "PRIMARY KEY (assignName)"
        SQLquery += ");"
        myDBCur.execute(SQLquery)
        #db파일에서 assignName리스트 출력 및 출력희망하는 과제이름 입력받기
        results = myDBCur.execute("select assignName, subName from myAssign")
        print('=== 현재 등록된 과제명 ===')
        for result in results:
            print(result[0]+"("+result[1]+")")
        print('=========================')
        assignName=input("확인하고 싶은 과제이름 : ")
        if(self.chkCancel(assignName)==True):
            return -1
        resultNumber = myDBCur.execute("select count(assignName) from myAssign where assignName=(?);", (assignName,))
        for resultNum in resultNumber:
            resultCnt=resultNum[0]
        while(resultCnt==0):
            print("테이블에 해당 과제이름이 존재하지 않습니다.")
            assignName=input("확인하고 싶은 과제이름 : ")
            resultNumber = myDBCur.execute("select count(assignName) from myAssign where assignName=(?);",(assignName,))
            for resultNum in resultNumber:
                resultCnt = resultNum[0]
            if(self.chkCancel(assignName)==True):
                return -1
        #과제정보 출력
        results = myDBCur.execute("select assignName, subName, subGroup, deadDate, deadTime, submitWay, progress from myAssign")
        for result in results:
            #result[0] : assignName
            #result[1] : subName
            #result[2] : subGroup
            #result[3] : deadDate
            #result[4] : deadTime
            #result[5] : submitWay
            #result[6] : progress
            if(result[6]==0):
                progressStat="1도안함"
            elif(result[6]==1):
                progressStat="진행중임"
            elif(result[6]==2):
                progressStat="과제완료"
            elif(result[6]==3):
                progressStat="제출완료"
            else:
                print("어라? 왜 progress에 0~3이 아닌 값이 있지??")
                return ;
            print("=================================================")
            print("제목 : "+result[0])
            print("과목 : "+result[1]+"["+result[2]+"]")
            print("마감기한 : "+result[3]+" "+result[4])
            print("제출방식 : "+result[5])
            print("진행상태 : "+progressStat)
            print("=================================================")
    def testShow(self): #시험세부정보 보여주기
        #DB연결
        DBName = 'mySchedule.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #db파일에서 myTest이 없으면 만들어주기
        myDBCur.execute("create table if not exists myTest(testName TEXT NOT NULL, subName TEXT NOT NULL, subGroup TEXT NOT NULL, testDate TEXT, testTime TEXT, testPlace TEXT, PRIMARY KEY (testName));")
        #db파일에서 assignName리스트 출력 및 출력희망하는 시험이름 입력받기
        results = myDBCur.execute("select testName, subName from myTest")
        print('=== 현재 등록된 시험명 ===')
        for result in results:
            print(result[0]+"("+result[1]+")")
        print('=========================')
        testName=input("확인하고 싶은 시험이름 : ")
        if(self.chkCancel(testName)==True):
            return -1
        resultNumber = myDBCur.execute("select count(testName) from myTest where testName=(?);",(testName,))
        for resultNum in resultNumber:
            resultCnt=resultNum[0]
        while(resultCnt==0):
            print("테이블에 해당 시험이름이 존재하지 않습니다.")
            testName=input("확인하고 싶은 시험이름 : ")
            resultNumber = myDBCur.execute("select count(testName) from myTest where testName=(?);", (testName,))
            for resultNum in resultNumber:
                resultCnt = resultNum[0]
            if(self.chkCancel(testName)==True):
                return -1
        #시험정보 출력
        results = myDBCur.execute("select testName, subName, subGroup, testDate, testTime, testPlace from myTest where testName=(?);",(testName,))
        for result in results:
            #result[0] : testName
            #result[1] : subName
            #result[2] : subGroup
            #result[3] : testDate
            #result[4] : testTime
            #result[5] : testPlace
            print("=================================================")
            print("제목 : "+result[0])
            print("과목 : "+result[1]+"["+result[2]+"]")
            print("시험일자 : "+result[3]+" "+result[4])
            print("시험장소 : "+result[5])
            print("=================================================")
    def summaryShow(self):
        self.assignSummary()
        print()
        self.testSummary()
    def assignSummary(self):
        #DB연결
        DBName = 'mySchedule.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #db파일에서 myAssign이 없으면 만들어주기
        SQLquery = "create table if not exists myAssign("
        SQLquery += "assignName TEXT NOT NULL, "
        SQLquery += "subName TEXT NOT NULL, "
        SQLquery += "subGroup TEXT NOT NULL, "
        SQLquery += "deadDate TEXT, "
        SQLquery += "deadTime TEXT, "
        SQLquery += "submitWay TEXT NOT NULL, "
        SQLquery += "progress INTEGER NOT NULL, "
        SQLquery += "PRIMARY KEY (assignName)"
        SQLquery += ");"
        myDBCur.execute(SQLquery)
        #db파일에서 myAssign 값 받기
        results = myDBCur.execute("select deadDate, progress, assignName from myAssign")
        print("=========== 과제 정보 요약 ===========")
        print("No      D-day      진행상태      과제")
        no=1 #No값 미리 초기화
        for result in results:
            #result[0]:deadDate // result[1]:progress // result[2]:assignName
            #D-day 구하기
            deadDate=result[0].split("-")
            dDate = datetime.date(int(deadDate[0]), int(deadDate[1]), int(deadDate[2]))
            tDate = datetime.datetime.today()
            dDay = int(str(dDate-tDate.date()).split(" ")[0])
            #progress 대입
            if(result[1]==0):
                progressStat="1도안함"
            elif(result[1]==1):
                progressStat="진행중임"
            elif(result[1]==2):
                progressStat="과제완료"
            elif(result[1]==3):
                progressStat="제출완료"
            else:
                print("어라? 왜 progress에 0~3이 아닌 값이 있지??")
                return -1
            #assignName 구해주기
            myAssignName=result[2]
            #출력하기
            menuBar=str(no)+"       "+str(dDay)+"     "+progressStat+"      "+myAssignName
            print(menuBar)
            no=no+1
        print("======================================")
    def testSummary(self):
        #DB연결
        DBName = 'mySchedule.db'
        myDBPath = os.path.dirname(os.path.abspath(__file__))+DBName
        myDB = sqlite3.connect(myDBPath)
        myDBCur = myDB.cursor()
        #db파일에서 myTest이 없으면 만들어주기
        myDBCur.execute("create table if not exists myTest(testName TEXT NOT NULL, subName TEXT NOT NULL, subGroup TEXT NOT NULL, testDate TEXT, testTime TEXT, testPlace TEXT, PRIMARY KEY (testName));")
        #db파일에서 myTest값 받기
        results = myDBCur.execute("select testDate, testName from myTest")
        no=1
        print("======= 시험 정보 요약 =======")
        print("No      D-day      시험")
        for result in results:
            #result[0]:testDate // result[1]:testName
            testDate=result[0].split("-")
            dDate = datetime.date(int(testDate[0]), int(testDate[1]), int(testDate[2]))
            tDate = datetime.datetime.today()
            dDay = int(str(dDate-tDate.date()).split(" ")[0])
            myTestName=result[1]
            menuBar=str(no)+"      "+str(dDay)+"      "+myTestName
            print(menuBar)
            no=no+1
        print("==============================")
	############ 기 타 ##############
    def isDate(self, text): #Date형식이 맞는지 확인
        chkHdler = re.compile('^[0-9]{4}(-)[0-9]{2}(-)[0-9]{2}$')
        if(chkHdler.match(text)):
            return True
        else:
            return False
    def isTime(self, text): #Time형식이 맞는지 확인
        chkHdler = re.compile('^[0-9]{2}(:)[0-9]{2}$')
        if(chkHdler.match(text)):
            return True
        else:
            return False
    def findInList(self, mylist, val): #list에 val이 있는지 찾기
        for list in mylist:
            print('list: ',end='')
            print(list[0])
            print('val: ', end='')
            print(val)
            if(list[0]==val):
                return True
            else:
                return False
    def printTime(self):
        dt = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
        nowTimeString=str(dt.hour)+'시 '+str(dt.minute)+'분 '+str(dt.second)+'초'
        print(nowTimeString)
    def comOFF(self):
        print("**컴퓨터를 종료합니다**")
        if(self.askIsOK()==0):
            return -1
        os.system("shutdown -s -t 0")
    def zeroOFF(self):
        print("**Zero 프로그램을 종료합니다**")
        if(self.askIsOK()==0):
            return -1
        sys.exit()
    ########### 날씨, 온도 ##########
    def printClimate(self, when): #오늘(0) or 내일(1)의 기상상태
        API_Key = 'f0718a30e815fe62179c2848b8c3bd23'
        myOwm = pyowm.OWM('f0718a30e815fe62179c2848b8c3bd23')
        CityID = 1835848 # Korea/Seoul
        if(when==1): #오늘 최고/최저
            cityInfo = myOwm.weather_at_id(CityID)
            cityWeaInfo = cityInfo.get_weather()
            when_word='오늘'
        elif(when==2): #내일 최고/최저
            cityInfo = myOwm.daily_forecast_at_id(CityID)
            cityWeaInfo = cityInfo.get_weather_at(pyowm.timeutils.tomorrow())
            when_word='내일'
        cityWeaInfo_STAT = cityWeaInfo.get_status()
        print(when_word+'날씨 : '+cityWeaInfo_STAT)
    def printTemp(self, when): #오늘(0) or 내일(1)의 최고/최저온도
        API_Key = 'f0718a30e815fe62179c2848b8c3bd23'
        myOwm = pyowm.OWM('f0718a30e815fe62179c2848b8c3bd23')
        CityID = 1835848 # Korea/Seoul
        if(when==1): #오늘 최고/최저
            cityInfo = myOwm.weather_at_id(CityID)
            cityWeaInfo = cityInfo.get_weather()
            when_word='오늘'
            cityWeaInfo_TEMP = cityWeaInfo.get_temperature(unit='celsius') #celsius:섭씨
            tempMax=str(round(cityWeaInfo_TEMP['temp_max']))
            tempMin=str(round(cityWeaInfo_TEMP['temp_min']))
        elif(when==2): #내일 최고/최저
            cityInfo = myOwm.daily_forecast_at_id(CityID)
            cityWeaInfo = cityInfo.get_weather_at(pyowm.timeutils.tomorrow())
            when_word='내일'
            cityWeaInfo_TEMP = cityWeaInfo.get_temperature(unit='celsius') #celsius:섭씨
            tempMax=str(round(cityWeaInfo_TEMP['max']))
            tempMin=str(round(cityWeaInfo_TEMP['min']))
        print(when_word+'최고기온 : '+tempMax)
        print(when_word+'최저기온 : '+tempMin)
    def askIsOK(self): #OK(1), No(0), error(-1)
        while(1):
            ans = input("계속 진행하시겠습니까?")
            if(self.chkYes(ans)==True):
                return 1
            elif(self.chkNo(ans)==True):
                return 0
            else:
                print('무슨 말인지 잘 모르겠습니다')
    def greeting(self):
        API_Key = 'f0718a30e815fe62179c2848b8c3bd23'
        dt = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
        nowTime = dt.hour
        print("================ 확 인 사 항 ================")
        self.summaryShow()
        print("============================================")
        print("zero: ",end='')
        if(nowTime>=5 and nowTime<=7): #Case 이른 아침
            greetingMent=[
                '오늘은 무슨일로 이리 일찍 일어나셨나요',
                '졸려... 왜 벌써 깨우는데 ㅡㅡ;',
                '왠일이냐 이른 아침부터??'
                ]
            print(greetingMent[random.randrange(0,len(greetingMent))]) #대사 랜덤 출력
        elif(nowTime>=7 and nowTime<=11): #Case 아침
            greetingMent=[
                '아침은 먹었니?',
                '좋은 아침 ㅎㅎ! 밥먹어야지~',
                '아아ㅠ 다시 아침이 왔네'
                ]
            print(greetingMent[random.randrange(0,len(greetingMent))])
            myOwm = pyowm.OWM(API_Key)
            isNowRainy = myOwm.will_be_rainy_at(pyowm.timeutils.now())
            isNext3HRainy = myOwm.will_be_rainy_at(pyowm.timeutils.next_three_hours())
            if(isNowRainy==True or isNext3HRainy==True):
                print('오늘 비 오나본데? 우산 챙겨!')
        elif(nowTime>=11 and nowTime<=15): #Case 점심
                greetingMent=[
                    '점심은 먹었니?'
                    ]
                print(greetingMent[random.randrange(0,len(greetingMent))])
        elif(nowTime>=17 and nowTime<=21): #Case 저녁
            greetingMent=[
                '저녁은 먹었니?',
                '오늘 깜빡하고 저한테 말씀 안해주신거 있는건 아니죠?? 다시한번 확인해보세요!',
                '퇴근하고싶다..'
                ]
            print(greetingMent[random.randrange(0,len(greetingMent))])
        elif((nowTime>=21 and nowTime<=24) or nowTime>=0 and nowTime<=2): #Case 밤
            greetingMent=[
                '상쾌한 밤입니다 ㅎ',
                '역시 모든 일의 시작은 밤부터지!!',
                '밤은 나의 주 활동 시간이죠 !!ㅋ'
                ]
            if(datetime.datetime.today().weekday()==4 or datetime.datetime.today().weekday()==5): #금/토 전용 추가 멘트
                if(nowTime>=21):
                    temp='내일'
                else:
                    temp='오늘'
                greetingMent.append(temp+'은 주말 핰핰 같이 밤샐거지? ㅎ')
            print(greetingMent[random.randrange(0,len(greetingMent))])
        elif(nowTime>=2 and nowTime<=5): #Case 새벽
            greetingMent=[
                '공부하는거 때문에 아직도 밤새는거라면... 힘내요... ㅠ',
                '아.. 새벽이네.. 프로그램이라 잠이 필요없긴한데 그래도 자고싶다..'
                ]
            if(datetime.datetime.today().weekday()<4 or datetime.datetime.today().weekday()>5): #금/토 제외 추가 멘트
                greetingMent.append('내일 주말 아닌데; 어서 자는게 신상에 좋을껄...?')
            print(greetingMent[random.randrange(0,len(greetingMent))])
    def setAlarm(self):
        print('얼마 후로 알람을 설정해드릴까요?')
        alarmTime = input('input: ')
        if (alarmTime.count('뒤') == 1):  # 특정 시간 뒤 알람 설정
            plusSec = 0
            if (alarmTime.count('시') == 1):
                alarmTime = alarmTime.split('시')
                setHour = alarmTime[0]
                alarmTime = alarmTime[1]
                if (len(setHour) > 1 and setHour[-2].isdigit() == True):
                    setHour = int(setHour[-2] + setHour[-1])
                else:
                    setHour = int(setHour[-1])
                plusSec=plusSec+setHour*3600
            if (alarmTime.count('분') == 1):
                alarmTime = alarmTime.split('분')
                setMin = alarmTime[0]
                alarmTime = alarmTime[1]
                if (len(setMin) > 1 and setMin[-2].isdigit() == True):
                    setMin = int(setMin[-2] + setMin[-1])
                else:
                    setMin = int(setMin[-1])
                plusSec = plusSec + setMin * 60
            if (alarmTime.count('초') == 1):
                alarmTime = alarmTime.split('초')
                setSec = alarmTime[0]
                alarmTime = alarmTime[1]
                if (len(setSec) > 1 and setSec[-2].isdigit() == True):
                    setSec = int(setSec[-2] + setSec[-1])
                else:
                    setSec = int(setSec[-1])
                plusSec=plusSec+setSec
            print(plusSec)
            thread1 = threading.Thread(target=self.alarm, args=(plusSec,))
            thread1.start()
        else:  # 특정 시간에 알람 설정
            nowTime = datetime.datetime.now()
            tTime = datetime.datetime.now()
            if (alarmTime.count('시') == 1):
                alarmTime = alarmTime.split('시')
                setHour = alarmTime[0]
                alarmTime = alarmTime[1]
                if (len(setHour) > 1 and setHour[-2].isdigit() == True):
                    setHour = int(setHour[-2] + setHour[-1])
                else:
                    setHour = int(setHour[-1])
                tTime = tTime.replace(hour=setHour)
            if (alarmTime.count('분') == 1):
                alarmTime = alarmTime.split('분')
                setMin = alarmTime[0]
                alarmTime = alarmTime[1]
                if (len(setMin) > 1 and setMin[-2].isdigit() == True):
                    setMin = int(setMin[-2] + setMin[-1])
                else:
                    setMin = int(setMin[-1])
                tTime = tTime.replace(minute=setMin)
            else:
                tTime = tTime.replace(minute=0)
            if (alarmTime.count('초') == 1):
                alarmTime = alarmTime.split('초')
                setSec = alarmTime[0]
                alarmTime = alarmTime[1]
                if (len(setSec) > 1 and setSec[-2].isdigit() == True):
                    setSec = int(setSec[-2] + setSec[-1])
                else:
                    setSec = int(setSec[-1])
                tTime = tTime.replace(second=setSec)
            else:
                tTime = tTime.replace(second=0)
            plusTime = tTime - nowTime
            plusSec = plusTime.seconds
            if (nowTime > tTime):  # 하루 추가하는 케이스
                plusSec = 86400 - (nowTime - tTime).seconds  # 24시간-차이값
            print(plusSec)
            thread1 = threading.Thread(target=self.alarm, args=(plusSec,))
            thread1.start()
    def alarm(self, second):
        time.sleep(second)
        print()
        print('#### 알람 딸랑딸랑 ☏♬~ ####')
myCat=Zero()
myCat.printZero()
myCat.greeting()
while(1):
    message=input('input the message: ')
    myCat.chkChat(message)
