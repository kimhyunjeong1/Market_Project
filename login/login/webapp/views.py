from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from dbapp.models import Users  # dbapp에서 Users 모델 임포트
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password


def main(request):
    return render(request, "webapp/main.html")


def my_page(request):
    return render(request, "webapp/my_page.html")


def product_sale(request):
    return render(request, "webapp/product_sale.html")


def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # 사용자 정보 조회
        try:
            user = Users.objects.get(user_userid=username)  # 사용자 ID로 검색
            # 비밀번호 확인
            if check_password(password, user.password):
                login(request, user)  # 로그인 처리
                messages.success(request, "로그인 성공!")
                return redirect("main")  # 성공적으로 로그인한 후 리디렉션할 URL
            else:
                messages.error(request, "아이디 또는 비밀번호가 잘못되었습니다.")
                return redirect("sign_in")  # 로그인 페이지로 리디렉션
        except Users.DoesNotExist:
            messages.error(request, "아이디 또는 비밀번호가 잘못되었습니다.")
            return redirect("sign_in")  # 로그인 페이지로 리디렉션

    return render(request, "webapp/sign_in.html")


def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password_confirm = request.POST["password_confirm"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        detail_address = request.POST["detail_address"]
        extra_address = request.POST["extra_address"]
        postcode = request.POST["postcode"]

        # 비밀번호 확인
        if password != password_confirm:
            messages.error(request, "비밀번호가 일치하지 않습니다.")
            return redirect("sign_up")

        # 주소 합치기
        full_address = f"{address}, {detail_address}, {extra_address}".strip(", ")

        # 사용자 생성
        try:
            user = Users(
                user_userid=username,
                user_email=email,
                user_name=name,
                user_address=full_address,
                user_phoneNum=phone,
            )
            user.set_password(password)  # 비밀번호 해시화
            user.full_clean()  # 모델 검증
            user.save()

            messages.success(request, "회원가입이 완료되었습니다.")
            return redirect("sign_in")
        except ValidationError as e:
            messages.error(
                request, f"입력값에 오류가 있습니다: {', '.join(e.messages)}"
            )
            return redirect("sign_up")
        except Exception as e:
            messages.error(request, f"오류가 발생했습니다: {str(e)}")
            return redirect("sign_up")

    return render(request, "webapp/sign_up.html")
