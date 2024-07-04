# 간단한 프롬프트 게시판을 만들어보겠습니다.
# 다음과 같은 기능을 가진 게시판을 만들어보세요.
# 1. 사용자로부터 입력을 받아 입력된 내용을 리스트에 저장합니다.
# 2. 게시판에 저장된 내용이 없으면 "게시글이 없습니다."를 출력합니다.
# 3. 게시판에 저장된 내용이 있으면 게시판에 저장된 내용을 출력합니다.
# 4. 게시판에 저장된 내용은 다음과 같이 출력합니다.
#    1. 제목: 제목 내용
#    2. 작성자: 작성자 내용
#    3. 내용: 본문 내용
# 5. 게시판에 저장된 내용은 다음과 같이 입력받습니다.
#    1. 제목을 입력하세요.
#    2. 작성자를 입력하세요.
#    3. 글 내용을 입력하세요.
# 6. 게시판에 저장된 내용은 딕셔너리로 저장합니다.
#    1. {'제목': '제목 내용', '작성자': '작성자 내용', '내용': '본문 내용'}
# 7. 게시판의 각 기능은 다음과 같이 입력받아 동작합니다.
#    1. write: 게시판에 글을 작성합니다.
#    2. list: 게시판에 저장된 글 목록을 제목과 작성자로 출력합니다.
#    3. read: 게시판에 저장된 글 번호를 입력받아 출력합니다.
#    4. find: 게시판에 저장된 글을 찾습니다.
#    5. exit: 게시판을 종료합니다.

# 주의) todo 부분을 수정하여 각 기능을 완성하세요.

# 게시판을 저장할 리스트를 생성합니다.

board = []

# 게시판의 각 기능을 정의합니다.
def write():
    # 글을 작성합니다.
    title = input("제목을 입력하세요: ")
    author = input("작성자를 입력하세요: ")
    content = input("글 내용을 입력하세요: ")
    # todo: 딕셔너리로 저장된 글을 리스트에 저장합니다.
    print("게시글이 작성되었습니다.")


def list():
    # 게시판에 저장된 글 목록을 제목과 작성자로 출력합니다.
    if not board:
        print("게시글이 없습니다.")
    else:
        print("게시글 목록")
        print("==========")
        for idx, post in enumerate(board):
            # todo: 게시판에 저장된 글을 출력합니다. idx는 현재 글 번호를 의미합니다.
        print("==========")

def read():
    # 게시판에 저장된 글 번호를 입력받아 출력합니다.
    idx = int(input("글 번호를 입력하세요: "))
    if 1 <= idx <= len(board):
        post = board[idx - 1]
        # todo: 게시판에 저장된 글을 출력합니다.
    else:
        print("글 번호를 잘못 입력하셨습니다.")

def find():
    # 게시판에 저장된 글을 찾습니다.
    keyword = input("검색할 내용을 입력하세요: ")
    search_list = []
    for post in board:
        if keyword in post['제목'] or keyword in post['내용']:
            search_list.append(post)
    print("검색 결과")
    print("==========")
    if search_list:
        for idx, post in enumerate(search_list):
            print(f"{idx + 1}. 제목: {post['제목']} 작성자: {post['작성자']}")
    else:
        print("검색 결과가 없습니다.")
    print("==========")

def exit():
    # 게시판을 종료합니다.
    print("게시판을 종료합니다.")
    return True

# 게시판의 각 기능을 실행합니다.
while True:
    command = input("명령어를 입력하세요(write, list, read, find, exit): ")
    if command == 'write':
        write()
    elif command == 'list':
        list()
    elif command == 'read':
        read()
    elif command == 'find':
        find()
    elif command == 'exit':
        if exit():
            break
    else:
        print("잘못된 명령어입니다.")
    