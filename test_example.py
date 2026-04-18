from playwright.sync_api import APIRequestContext, Playwright
import pytest

@pytest.fixture(scope="session")
def api_request(playwright: Playwright):
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield request
    request.dispose()

def test_GET_게시글(api_request: APIRequestContext):
    response = api_request.get("/posts/1")

    # 상태코드 확인
    assert response.status == 200

    # 응답 데이터 확인
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    print(f"제목: {data['title']}")

def test_POST_게시글(api_request: APIRequestContext):
    response = api_request.post("/posts", data={
        "title": "테스트 게시글",
        "body": "내용입니다",
        "userId": 1
    })

    # 상태코드 확인 (201 = 생성 성공)
    assert response.status == 201

    data = response.json()
    assert data["title"] == "테스트 게시글"
    print(f"생성된 ID: {data['id']}")