import httpx

from starlette.datastructures import Headers
from pydantic import BaseModel


class HTTPClient:
    def __init__(self, base_url: str):
        self.client = httpx.AsyncClient(
            base_url=base_url,
            follow_redirects=True,
            timeout=httpx.Timeout(connect=10.0, read=120.0, write=120.0, pool=30.0)
        )

    async def __request(
        self,
        method: str,
        endpoint: str,
        *,
        params: dict = None,
        json_payload: dict | BaseModel = None,
        files=None,
        headers: dict | Headers = None,
        cookies: dict = None
    ):
        try:
            proxy_headers = {str(k).lower(): v for k, v in dict(headers).items()}
            proxy_headers.pop("content-length", None)
            proxy_headers.pop("host", None)
            if files is not None:
                proxy_headers.pop("content-type", None)

            json_data = None
            if json_payload is not None:
                if hasattr(json_payload, "model_dump"):
                    json_data = json_payload.model_dump()
                elif isinstance(json_payload, dict):
                    json_data = json_payload
                else:
                    raise ValueError("json_payload должен быть dict или Pydantic-моделью")

            request_args = {
                "method": method,
                "url": endpoint,
                "params": params,
                "headers": proxy_headers,
                "cookies": cookies,
            }
            if json_data is not None:
                request_args["json"] = json_data
            if files is not None:
                request_args["files"] = files

            response = await self.client.request(**request_args)
            response.raise_for_status()
            return response
        except httpx.RequestError as exc:
            print(f"Ошибка при запросе {exc.request.url!r}: {exc}")
            raise exc
        except httpx.HTTPStatusError as exc:
            print(f"HTTP статус {exc.response.status_code} для запроса {exc.request.url!r}")
            return exc.response

    async def get(self, endpoint: str, *, params=None, json_payload: dict | BaseModel = None, files=None, headers: dict | Headers = None, cookies: dict = None):
        response = await self.__request("GET", endpoint, params=params, json_payload=json_payload, files=files, headers=headers, cookies=cookies)
        return response.json()

    async def post(self, endpoint: str, *, params=None, json_payload: dict | BaseModel = None, files=None, headers: dict | Headers = None, cookies: dict = None):
        response = await self.__request("POST", endpoint, params=params, json_payload=json_payload, files=files, headers=headers, cookies=cookies)
        return response.json()

    async def put(self, endpoint: str, *, params=None, json_payload: dict | BaseModel = None, files=None, headers: dict | Headers = None, cookies: dict = None):
        response = await self.__request("PUT", endpoint, params=params, json_payload=json_payload, files=files, headers=headers, cookies=cookies)
        return response.json()

    async def patch(self, endpoint: str, *, params=None, json_payload: dict | BaseModel = None, files=None, headers: dict | Headers = None, cookies: dict = None):
        response = await self.__request("PATCH", endpoint, params=params, json_payload=json_payload, files=files, headers=headers, cookies=cookies)
        return response.json()

    async def delete(self, endpoint: str, *, params=None, json_payload: dict | BaseModel = None, files=None, headers: dict | Headers = None, cookies: dict = None):
        response = await self.__request("DELETE", endpoint, params=params, json_payload=json_payload, files=files, headers=headers, cookies=cookies)
        return response.json()