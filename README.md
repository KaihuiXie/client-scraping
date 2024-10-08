## Scraper Guide

---
### Install Tampermonkey
Use `Edge` or `Chrome` browsers
- Click the three dots on the top right of the browser
- Find `Extensions`
- Click `Manage Extensions`
- Go to either `Get extensions for Microsoft Edge` or `Chrome Web Store`
- Search `Tampermonkey` and download
---

### Import Tampermonkey Scripts

- In `Extensions` click `Tampermonkey` (you can pin it for quicker access)
- In the dropdown menu, click `Dashboard`
- Go to `Utilities`
- Under `Import from file` click `Choose File` and import the zip file `1688_scraper_scripts.zip` under dir `tampermonkey scripts`
---

### Create Database
Use `MySQL` as an example
- Open `MySQL Workbench`
- Create local connection with **hostname**: `localhost`(default port: `3306`), **user**: `contact_user`, **password**: `1688Contacts`
- Connect to database
- Run `createDB.sql` and `createtable.sql` under `sql queries` in MySQL workbench

(Optional) If you would like to use `root` user and separate `contact_user`:
- Open `MySQL Workbench`
- Create local connection with **hostname**: `localhost`(default port: `3306`), **user**: `root` with any password you like
- Connect to database
- run all three sql queries under `sql queries`
---

### Run the Scraper

Steps:
1. Run scraper app:
```bash 
python app.py
```
2. Open the browser with Tampermonkey and the scripts installed and go to `1688.com`(you might need to log in)
3. Go to `跨境服务/站内商机` (`air.1688.com`), select `美国` and the category you would like to scrape
4. Voila! It starts scraping! (product page and contact info page will pop up and close automatically) (TODO: dynamic recaptcha might make it fail, will be fixed)
5. If you would like to view all the scraped contacts, click on the `导出联系人到CSV` button on the bottom right and the CSV file will be downloaded to the default browser download directory