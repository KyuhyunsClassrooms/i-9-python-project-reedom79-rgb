# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 
import math

# 함수 1: 별 정보 입력
def input_stars():
    stars = []  # 2차원 리스트

    count = int(input("입력할 별의 개수를 입력하세요: "))

    for i in range(count):
        print(f"\n{i+1}번째 별 정보 입력")
        name = input("별 이름: ")
        flux = float(input("밝기(Flux): "))

        stars.append([name, flux])

    return stars


# 함수 2: 밝기 등급 계산
def calculate_magnitude(flux, reference_flux=1000):
    magnitude = -2.5 * math.log10(flux / reference_flux)
    return round(magnitude, 2)


# 함수 3: 결과 출력
def print_results(stars):
    print("\n=== 별의 밝기 등급 계산 결과 ===")

    for star in stars:
        name = star[0]
        flux = star[1]

        mag = calculate_magnitude(flux)

        # 조건문 사용
        if mag < 1:
            level = "매우 밝음"
        elif mag < 3:
            level = "밝음"
        else:
            level = "어두움"

        print(f"\n별 이름: {name}")
        print(f"밝기(Flux): {flux}")
        print(f"등급(Magnitude): {mag}")
        print(f"판정: {level}")


# 프로그램 실행
stars = input_stars()
print_results(stars)