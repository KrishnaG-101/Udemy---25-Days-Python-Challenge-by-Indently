# Using asyncio to check website status.

import asyncio
from asyncio import TimeoutError
import requests
from requests import Response
from dataclasses import dataclass

@dataclass
class WebsiteResponse:
    url : str
    status : int | None
    reason : str
    response_time : float


def normalize_url(url : str) -> str:
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"
    return url

async def get_website_response(url : str) -> WebsiteResponse:
    # Will raise a Timeout Error:
    if url == "www.fail-website.com" or url == "www.amazon.com" or url == "www.microsoft.com":
        await asyncio.sleep(10)
    
    try:
        headers : dict[str, str] = {'Accept-Encoding': 'gzip, deflate'}
        response : Response = await asyncio.to_thread(requests.get, normalize_url(url), headers=headers)
        
        return WebsiteResponse(
            url,
            response.status_code,
            response.reason,
            response.elapsed.total_seconds()
        )
    except Exception as error:
        return WebsiteResponse(url, None, str(error.__class__), -1)

async def check_websites(urls : list[str], timeout : float = 10) -> None:
    tasks = [get_website_response(url) for url in urls]
    responsive_urls : list[str] = list()
    # unresponsive_urls : list[str] = list()
    
    try:
        for completed_task in asyncio.as_completed(tasks, timeout=timeout):
            website_response : WebsiteResponse = await completed_task
            responsive_urls.append(website_response.url)
            
            if website_response.status is not None:
                print(f"{website_response.url:<20}: ✅ ONLINE ({website_response.status} {website_response.reason} {website_response.response_time:.2f}s)")
            else:
                print(f"Could not retrieve information for: \"{website_response.url}\" (reason: {website_response.reason})")
        
    except TimeoutError:
        print("\nTimeout reached - The following websites took too long to respond:")
        # We can also convert to a set and find the difference and return it, if we don't want to loop.
        # print(set(urls).difference(set(responsive_urls)))
        for url in urls:
            if url not in responsive_urls:
                print(url)
        print()

async def main() -> None:
    urls: list[str] = [
        'www.indently.io',
        'www.apple.com',
        'www.facebook.com',
        'nonexistent-website-404.com',
        'www.instagram.com',
        'www.reddit.com',
        'www.wikipedia.org',
        'www.fail-website.com',
        'www.amazon.com',
        'www.linkedin.com',
        'www.microsoft.com',
        'www.github.com',
    ]
    
    print(f"\nChecking {len(urls)} websites...")
    await check_websites(urls)
    print("Done\n")


if __name__ == "__main__":
    asyncio.run(main=main())