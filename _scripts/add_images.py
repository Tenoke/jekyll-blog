from selenium import webdriver
from pathlib import Path
from PIL import Image
import re
import hashlib
import time
exclude = ['mailto', '.xml', ' ', 'assets']

processed_urls = []

def get_links(filename, download=True):
    print(f'\033[1m{filename}\033[0m')
    with open(filename) as f:
        html = f.read()
    urls = re.findall('\<a.*?href="(.*?)"\>', html)
    for url in urls:
        if any([item in url for item in exclude]) or '/' not in url or len(url) < 2:
            print(f'skipping {url}')
            continue
        print(url)
        hashed = hashlib.sha256(url.encode('utf-8')).hexdigest()[:16]
        if url not in processed_urls and not any([str(hashed) in item for item in preloaded]) and download:
            driver_link = url
            if driver_link.startswith('/'):
                # driver_link = f'https://svilentodorov.xyz{url}'
                driver_link = f'http://0.0.0.0:8000{url}'
            driver.get(driver_link)
            driver.execute_script("return document.body.style.overflow = 'hidden';");
            time.sleep(2.75)
            img_path = f'_site/static/previews/{hashed}.png'
            driver.save_screenshot(img_path)
            Image.open(img_path).save(img_path,quality=15,optimize=True)

        processed_urls.append(url) ## moved this
        new_url = f'{url}"><span><img src="/static/previews/{hashed}.png"></span>'
        html = re.sub(pattern=f'(<a.*?href=")({url}">)', repl=f'\g<1>{new_url}', string=html)
        # html = html.replace(f'{url}">', new_url)
    with open(filename, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/google-chrome"
    driver = webdriver.Chrome(chrome_options=options)

    driver.set_window_size(900, 700)

    preloaded = [str(f) for f in Path('static/previews/').rglob('*.png')]
    print(preloaded)
    for filename in Path('_site/').rglob('*.html'):
        get_links(filename)
    driver.close()
