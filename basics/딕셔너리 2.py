foods={  "떡볶이" : "오뎅", "짜장면" : "단무지", "라면" : "김치",
     "피자" : "피클", "맥주" : "땅콩", "치킨" : "치킨무", "삼겹살" : "상추"};

while(True) :
    myfood=input(str(list(foods.keys()))+ "중 좋아하는 것은? ")
    ##여기서 myfood 가 사용자 입력값으로 들어감
    ##또한 list(foods.keys()여기서 딕셔너리의 키들을 보여줌
    if myfood in foods:   ##얘는 이제 myfood입력한값이 food에 있는지 검
        print(" <%s>궁합 음식은 <%s> 입니다." %(myfood, foods.get(myfood)))
    elif myfood=="끝":
        break;
    else:
        print("그런 음식이 없네요")
         
