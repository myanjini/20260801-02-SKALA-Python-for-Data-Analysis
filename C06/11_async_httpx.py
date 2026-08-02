"""httpx로 여러 JSON API를 비동기 호출합니다."""

import asyncio

import httpx


async def fetch_json(
    client: httpx.AsyncClient,
    name: str,
    url: str,
) -> dict[str, object]:
    """URL의 JSON 응답 또는 오류 정보를 반환합니다."""

    try:
        response = await client.get(url)
        response.raise_for_status()
        return {
            "name": name,
            "status": "success",
            "data": response.json(),
        }
    except httpx.HTTPError as error:
        return {
            "name": name,
            "status": "error",
            "error": str(error),
        }


async def main() -> None:
    """여러 API 요청을 하나의 클라이언트로 실행합니다."""

    targets = [
        ("서비스A", "https://example.com/api/a"),
        ("서비스B", "https://example.com/api/b"),
    ]

    timeout = httpx.Timeout(10.0)

    async with httpx.AsyncClient(timeout=timeout) as client:
        results = await asyncio.gather(
            *(fetch_json(client, name, url) for name, url in targets)
        )

    for result in results:
        print(result["name"], result["status"])


if __name__ == "__main__":
    asyncio.run(main())
aaaaa