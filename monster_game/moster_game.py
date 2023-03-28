import random
import time


# Player class
class Player:
    def __init__(self, name, hp, mp, power):
        self.name = name
        self.hp_max = hp
        self.hp = hp
        self.mp_max = mp
        self.mp = mp
        self.power = power

    # 플레이어의 일반 공격
    def attack(self):
        print("일반 공격 돌입!!")
        time.sleep(0.7)
        attack = random.randint(self.power-10, self.power+10)
        print(f"당신은 {attack}의 피해를 입혔다!")
        return attack

    # 플레이어의 마법 공격
    def magic_attack(self):
        print("마법 공격 돌입!")
        time.sleep(0.7)
        attack = random.randint(self.power-30, self.power+30)
        self.mp = self.mp - 1
        print(f"당신은 {attack}의 피해를 입혔다!")
        return attack

    # 플레이어가 공격 받았을 시
    def damage(self, attack):
        self.hp = self.hp - attack
        print(f"당신은 {attack}만큼의 피해를 입었습니다!")

    # 플레이어의 현재 HP, MP 확인
    def status_check(self):
        print("===========================")
        print(f"현재 hp : {self.hp} / {self.hp_max}")
        print(f"현재 mp : {self.mp} / {self.mp_max}")
        print("===========================")


# Monster class
class Monster():
    def __init__(self, type, hp, power):
        self.type = type
        self.hp = hp
        self.hp_max = hp
        self.power = power

    # 몬스터의 공격
    def attack(self):
        print("몬스터의 공격 돌입!!")
        time.sleep(0.7)
        attack = random.randint(self.power-20, self.power+20)
        print(f"{self.type}는 {attack}의 피해를 입혔다!")
        return int(attack)

    # 몬스터가 공격 받았을 시
    def damage(self, attack):
        self.hp = self.hp - attack
        print(f"{self.type}는 {attack}만큼의 피해를 입었습니다!")

    # 몬스터의 현재 HP, MP 확인
    def status_check(self):
        print("===========================")
        print(f"{self.type}의 현재 hp : {self.hp} / {self.hp_max}")
        print("===========================")


# Player 인스턴스 생성
p = Player(name=input("이름을 입력하세요: "), hp=random.randint(300, 500), mp=10, power=random.randint(30, 60)
           )

# Monster를 list에서 랜덤으로 추첨 후 Monster 인스턴스 생성
monster_list = [
    Monster(type="용용이", hp=100, power=20),
    Monster(type="칼칼이", hp=200, power=25),
    Monster(type="빵빵이", hp=300, power=30),
    Monster(type="쌩쌩이", hp=400, power=35),
    Monster(type="펑펑이", hp=500, power=40)
]
m = random.choice(monster_list)

# 전투 돌입 전
time.sleep(0.5)
print(f"당신의 이름은 {p.name}. 기본 스탯 hp:{p.hp}, mp:{p.mp}, 힘:{p.power}")
time.sleep(0.5)
print("매칭 된 몬스터는...")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(f"{m.type}가 나타났다!! hp: {m.hp}")
time.sleep(1)
print("전투를 시작합니다!!")
time.sleep(0.5)

# 전투 돌입
while (True):
    attack_type = int(
        input("공격 방식을 숫자로 입력해주세요! 1. 일반 공격 / 2. 마법 공격(mp 1 소모) / 3. 포기하기 : "))
    # 플레이어의 일반 공격
    if attack_type == 1:
        p_attack = p.attack()
        time.sleep(0.5)
        m.damage(p_attack)
        time.sleep(1)
        m_attack = m.attack()
        time.sleep(0.5)
        p.damage(m_attack)
        time.sleep(1)
        p.status_check()
        time.sleep(0.5)
        m.status_check()
        time.sleep(1)
    # 플레이어의 마법 공격 (마나가 남아있을 시)
    elif attack_type == 2 and p.mp > 0:
        p_attack = p.magic_attack()
        time.sleep(0.5)
        m.damage(p_attack)
        time.sleep(1)
        m_attack = m.attack()
        time.sleep(0.5)
        p.damage(m_attack)
        time.sleep(1)
        p.status_check()
        time.sleep(0.5)
        m.status_check()
        time.sleep(1)
    # 플레이어의 마법 공격 (마나가 전부 소진됐을 시)
    elif attack_type == 2 and p.mp <= 0:
        time.sleep(0.5)
        print("mp가 전부 소진되어 마법 공격이 불가능합니다!! 일반 공격을 실행해주세요")
        time.sleep(0.5)
    # 플레이어가 포기를 원할 때
    elif attack_type == 3:
        give_up = input("정말로 포기하시겠습니까? (y/n): ")
        if give_up == "y":
            time.sleep(0.5)
            print(f"당신은 {m.type}로부터 도망쳤습니다!")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(1)
            print("당신이 도망친 자리를 시작으로...")
            time.sleep(1)
            print(f"{m.type}는 모든 것을 파괴하기 시작합니다...")
            time.sleep(1)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(1)
            print("축하합니다! 당신 덕분에 이 세계는 더 빠르게 멸망될 수 있었습니다")
            time.sleep(1)
            print("===========================")
            print("[숨겨진 칭호]")
            print(f"{m.type}와 함께 세계를 멸망시킨 자 : {p.name}")
            print("===========================")
            break
        elif give_up == "n":
            time.sleep(1)
            print("당신은 도망치지 않기를 선택했습니다!!")
            time.sleep(1)
            print("훌륭한 용사의 자세군요! 전투로 다시 들어갑니다.")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
        else:
            time.sleep(1)
            print("틀렸습니다! 답 하나 제대로 고르시지 못하는건가요?")
            time.sleep(1)
            print("■■■■■는 당신을 다시 강제로 전투로 밀어넣습니다...")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
    # 등록되지 않은 공격 방식을 선택했을 시
    else:
        time.sleep(0.5)
        print("유효한 전투 타입이 아닙니다! 다시 입력해주세요.")
        time.sleep(0.5)

    # 플레이어 패배
    if p.hp < 0:
        time.sleep(1)
        print("===========================")
        print("이런... 당신의 hp가 0이 되었군요!!")
        print(f"당신은 {m.type}에게 패배했습니다!!")
        print("===========================")
        break
    # 플레이어 승리
    if m.hp < 0:
        time.sleep(1)
        print("===========================")
        print(f"세상에!! {m.type}의 hp가 0이 되었군요!!")
        print(f"당신은 {m.type}를 쓰러트렸습니다!")
        print("===========================")
        break
