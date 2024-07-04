# 예외를 사용해서 함수가 예외를 발생시키는 경우 3번까지 재시도하세요.
# 3번째 시도에서도 예외가 발생하면 False를 리턴하세요.
# 한번이라도 성공하면 True를 리턴합니다.
# 주의 ) 코드는 todo 부분만 수정하세요.

def task(work):
    if "no" in work:
        raise Exception("no")
    return

def question_10(func, args_list):
    error_count = 0
    while error_count < 3:
        try:
            func(args_list.pop(0))
        except:
            error_count += 1
            pass
        else:
            # -------------------------------
            # todo : 여기에 코드를 작성하세요.
            
            # -------------------------------
            pass
    return False


print(question_10(task, ["no", "no", "yes"]))