class student:
    def __init__(self,name,tel,sex):
        self.name=name
        self.tel=tel
        self.sex=sex

list=[]
while True:
    name=input("이름을 입력하세요 : ")
    if(name=="그만"):
        for i in list:
            print("이름은 " +i.name+" , 전화번호는"+i.tel+", 성별은"+ i.sex+"입니다.")
        break
    tel=input("전화번호를 입력하세요 : ")
    sex=input("성별을 입력하세요(male이나 female로 작성해주세요) : ")
    if(sex!="male" and sex!="female"):
        sex="unknown"
    member=student(name,tel,sex)
    list.append(member)
    for i in list:
        print("이름은 " +i.name+" , 전화번호는"+i.tel+", 성별은"+ i.sex+"입니다.")
        

    