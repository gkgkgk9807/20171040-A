name = input("당신의 닉네임을 입력해주세요")
print(name," 님 반갑습니다. {0} HP100으로 게임을 시작합니다.".format(name))
print(" 갑자기 고블린이 기습해왔다 ! ")
print("1.싸운다  2.도망친다")
num = int(input("선택 : "))
if num == 1:
    print("전투에서 승리했다!")

    list_a = ["포션" , "검" , "쓰레기"]

    print("골드 를 획득했다!")

    list_a.append("골드")

    print("당신의 인벤토리 : ",list_a,"가 있습니다.")

    print("레벨업! 당신의 스테이터스를 확인하세요")

    player={"hp":"110","mp":"60","pw":"15","df":"8"}

    for key, value in player.items():
        print(key, ":",value)


elif num == 2:
    print(" 이런... 패배했다... ")
else:
    print(" 고민하다가... 당했다... ")
    