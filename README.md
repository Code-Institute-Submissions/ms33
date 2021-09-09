# Purpose of this ReadMe.md file
a) To provide pertinent information about the structure of this MileStone3 Project for Anthony K.
<br />
b) Data Centric Development
<br />
c) Scratch-off lottery ticket database. It identifies game names, and allows users to add more games, and ending sales dates.
<br />
d) This app is going through a major overhaul as coding became faulty. Renewing via reliable source reference: Code Institute learning modules.
<br />
e) Removing from private repo
<br />
f) base.html = Parent template (contains all main references to the other files for css and JavaScript, that will be used across the entire application.)(purpose: no replication...Framework philosophy(Flask, Django, etc.)).
    
# Core Technologies used in this project
Python3, Flask, MongoDB, Jinja, AWS

## Additional Technologies utilized
 JQuery, MaterializeCSS

### Removed Technologies
ReactJS

#### References
Code Institute: https://codeinstitute.net/<br />
Python3: https://www.python.org/<br />
GitHub: https://github.com/<br />
GitPod: https://gitpod.io/workspaces<br />
MongoDB: https://www.mongodb.com/<br />
Flask: https://flask.palletsprojects.com/en/2.0.x/<br />
Heroku: https://dashboard.heroku.com/apps<br />
JQuery: https://code.jquery.com/<br />
MaterializeCSS: https://materializecss.com/<br />


## Deployment
bash: python3 app.py
Dependencies: dnspython, pymongo.
"requires": 
            obtained in requirements.txt

### pip3 install (update requirements.txt)
freeze --local > requirements.txt

### Deprecated during development
coll.delete
coll.insert

changed to coll.delete_one or delete_many
changed to coll.insert_one or insert.many

## MongoDB CRUD functionality ++ database Query = at command prompt type: python3 mongo.py
##### Pep8 compliance - no long lines
### two dictionaries array
#### fill in the value below to add multiple records
## add the below code into mongo.py
#### To create multiple records use this:
new_doc = [{
    "title": "game_name",
    "price": "1,2,3,5,10",
    "prize": "dollarAmt",
    "county": "nearestCounty",
    "date": "05/19/2021",
    "address": "street",
    "city": "where_purchased",
    "retailer": "store_name"
}, {
    "title": "game_name",
    "price": "1,2,3,5,10",
    "prize": "dollarAmt",
    "county": "nearestCounty",
    "date": "05/19/2021",
    "address": "street",
    "city": "where_purchased",
    "retailer": "store_name"
}]

coll.insert_many(new_doc)


#### To Read/search/find records that match the key:value pair:
documents = coll.find({"price": "10"})

#### To Read/search/find all records:
documents = coll.find()

#### To Delete one record that match the key:value pair:
coll.delete_one({"price": "10"})

#### To Delete all records that match the key:value pair:
coll.delete_many({"price": "10"})

#### Updates one record with the price of 1 dollar and changes its prize to 5000 dollars
coll.update_one({"price": "1"}, {"$set": {"prize": "5000"}})


## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `yarn build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
