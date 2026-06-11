import math

# 함수 1 : 별 정보 입력
def input_stars():
    stars = []  # 2차원 리스트

    count = int(input("관측한 별의 개수를 입력하세요 : "))

    for i in range(count):
        print(f"[{i+1}번째 별 정보 입력]")
        name = input("별 이름 : ")
        flux = float(input("별 밝기(Flux) : "))

        stars.append([name, flux])

    return stars


# 함수 2 : 등급(Magnitude) 계산
def calculate_magnitude(flux, reference_flux=1000):

    magnitude = -2.5 * math.log10(flux / reference_flux)

    return round(magnitude, 2)


# 함수 3 : 등급 판정
def classify_magnitude(magnitude):

    if magnitude <= 0:
        return "1등급 수준 (매우 밝음)"

    elif magnitude <= 2:
        return "2등급 수준"

    elif magnitude <= 4:
        return "3~4등급 수준"

    elif magnitude <= 6:
        return "5~6등급 수준"

    else:
        return "육안 관측 어려움"


# 함수 4 : 가장 밝은 별 찾기
def find_brightest_star(stars):

    brightest = stars[0]

    for star in stars:
        if star[1] > brightest[1]:
            brightest = star

    return brightest


# 함수 5 : 결과 출력
def print_report(stars):

    print("")
    print("=" * 70)
    print("               별 밝기 및 등급 분석 보고서")
    print("=" * 70)

    total_flux = 0

    for star in stars:

        name = star[0]
        flux = star[1]

        total_flux += flux

        magnitude = calculate_magnitude(flux)

        grade = classify_magnitude(magnitude)

        print(f"별 이름 : {name}")
        print(f"밝기(Flux) : {flux}")
        print(f"겉보기 등급(Magnitude) : {magnitude}")
        print(f"등급 분류 : {grade}")

    average = total_flux / len(stars)

    brightest = find_brightest_star(stars)

    print("" + "=" * 70)
    print("종합 분석")
    print("=" * 70)

    print(f"입력된 별 개수 : {len(stars)}개")
    print(f"평균 밝기 : {average:.2f}")
    print(f"가장 밝은 별 : {brightest[0]}")
    print(f"가장 밝은 별의 Flux : {brightest[1]}")

    print("=" * 70)


# 메인 프로그램
print("★ 별 밝기 및 등급 분석 프로그램 ★")

stars = input_stars()

if len(stars) > 0:
    print_report(stars)
else:
    print("입력된 별 정보가 없습니다.")