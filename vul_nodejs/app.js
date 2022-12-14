// IMPORTS & CONFIG
const express = require("express");
const cookieSession = require("cookie-session");

const User = require("./models/user");
const Mongoose = require("mongoose");

const app = express();

app.use(express.json());

require('./startup/db')();
require('./startup/middleware')(app);

app.use(
  cookieSession({
    keys: ["0"],
    httpOnly: false
  })
  
);

// CHECK AUTH
const forbidden = (req, res, next) => {
  if (!req.session.user) {
    res.redirect('login');
    return;
  }
  next();
};

// ROUTES FOR SERVING THE FRONTEND FILES
app
  .get("/", (req, res) => {
    res.render("index");
  })

  .get("/login", (req, res) => {
    res.render("login", {error: ""});
  })

  .get("/register", (req, res) => {
    res.render("register", {error: ""});
  })

  .get("/search", forbidden, (req, res) => {
    res.render("search", {header: "", result: ""});
  })
  
  .get("/download", forbidden, (req, res) => {
    res.render("download", {error: ""});
  })

  .get("/images/download.jpg", (req, res) => {
    res.sendFile(__dirname + "/images/download.jpg");
  })

  .get("/admin/users", (req, res) => {
    res.send("Only accepting POST requests!");
  })

  .get("/change-password", forbidden, (req, res) =>{
    res.render("change.ejs", {error: "", username: req.session.user.username});
  })

// ROUTES FOR HANDLING THE POST & GET REQUESTS

// Login
app.post("/login", async (req, res) => {
    const { username, password } = req.body;

    if (!username || !password)
      return res.render("login", {error: "Please enter all the fields!"});
    else {
      let query = { 
		    username: req.body.username,
		    password: req.body.password 
	    }

      User.find(query, function (err, user) {
        if (err) {
              console.log(err);
        } else {
          if (user.length >= 1) {
            req.session.user = {
              username,
            };
            res.redirect("/home");
          }
          else
            res.render("login", {error: "Invalid username or password!"});
        }
      });
    }
  })

// Register
app.post("/register", async (req, res) => {
    const { username, password } = req.body;

    if (!username || !password)
      return res.render("register", {error: "Please enter all the fields!"});

    if (await User.findOne({ username }))
      return res.render("register", {error: "Username already taken!"});

    const lastuid = await User.findOne({},{'userid':1}).sort({'userid':-1});

    if (lastuid == null)
      uid = 1;
    else
      uid = lastuid.userid + 1;

    currentTime = new Date().toUTCString();

    const latestUser = new User({userid: uid, username, password: password, time: currentTime, role: "user"});

    latestUser
      .save()
      .then(() => {
        res.render("login", {error: "Account Registered, login with the credentials"});
      })
      .catch((err) => console.log(err));
  });

// Search User 
app.post("/search", forbidden, async(req, res) => {
  const {uname} = req.body;

  const userEntry = await User.findOne({username: uname});

  if (!userEntry) {
    header = "No result for " + uname + "!";
    res.render('search', {header: header, result: ""});
  }
  else {
    header = "Result for " + uname + ":";
    result = "UserID: " + userEntry.userid + "<br>Role: " + userEntry.role  + "<br>Username: " + userEntry.username + "<br>Registered at: " + userEntry.time;
    res.render('search', {header: header, result: result});
  }
});

// Download Image
app.post("/download", async (req, res) => {
  const {url} = req.body;
  if (!isValidUrl(url))
    res.render('download', {error: "Invalid URL!"})
  else {
    try{
      await downloadImage(url);
      User.updateOne({username: req.session.user.username}, 
        {$push: {urls :url}}, function (err) {
          if (err)
            console.log(err)
        });
      res.render('download', {error: "<img src='images/download.jpg' alt=''>"})
    }
    catch(e){
      console.log(e);
      res.render('download', {error: "Unable to fetch image!"})
    }
  }
  });

// Home
app.get("/home", forbidden, (req, res) => {
  if (req.session.user.username == "admin")
    var hidden = "";
  else
    var hidden = "hidden";
    
  res.render("home", { user: req.session.user.username, error: "", hidden: hidden});
});

// Logout
app.get("/logout", forbidden, (req, res) => {
  req.session.user = null;
  res.redirect("/login");
});

// Clear URL history
app.get("/download/clear", forbidden, (req, res) => {
  User.updateOne({username: req.session.user.username}, 
    {urls :[]}, function (err) {
      if (err)
        console.log(err)
    });
  res.render("download", {error: ""});
});

// Admin
app.get("/admin", (req, res) => {
  if(req.session.user) {
    if (req.session.user.username == "admin")
      res.render("admin", {error: "", data: ""});
    else
      res.send("You are not allowed to view this page.");
  }
  else
    res.render("login", {error: "", data: ""});
});

// Reset
app.get("/reset", async (req, res) => {
  clientIP = req.socket.remoteAddress.replace(/^.*:/, '');
  localIP = req.socket.localAddress.replace(/^.*:/, '');

  if(req.session.user)
    username = req.session.user.username;
  else
    username = "";

  if (clientIP != localIP && username != "admin")
    res.sendStatus(403);
  else {
    Mongoose.connection.db.dropCollection('users', function(err, result) {return true});
    addAdmin();
    res.send("Database cleared...");
  }
});

// Display user data
app.post("/admin/users", async (req, res) => {
  users = await User.find({});

  if(req.body.hidden == 'false')
    data = JSON.stringify(users, ["userid", "username", "password", "time", "role", "urls"], 4);
  else
    data = JSON.stringify(users, ["userid", "username", "time", "role", "urls"], 4);
  
    res.render("admin", {error: "", data: data});
});

// Change password
app.post("/change-password", forbidden, async (req, res) => {
  const {username, password} = req.body;

  if (await User.findOne({ username })) {
    User.updateOne({username: username}, 
      {$set: {password :password}}, function (err) {
        if (err)
          console.log(err)
        else
          res.render("change", {error: "Password changed...", username: req.session.user.username});
      });
    }
    else {
      var msg = "Unexpected error: no such user " + username;
      res.render("change", {error: msg, username: req.session.user.username});
    }
});

// SERVER CONFIGURATION
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server started listening on port: ${PORT}`);
  addAdmin();
});

// FUNCTION TO CHECK URL
const URL = require('url').URL

function isValidUrl(urlString) {
  try {
    new URL(urlString)
      return true
  } catch {
    return false
  }
} 

// FUNCTION TO DOWNLOAD IMAGE FROM URL
const fs = require('fs');
const fetch = require('node-fetch');
const e = require("express");

if (!fs.existsSync('./images')){
    fs.mkdirSync('./images');
}

async function downloadImage(url) {
  const response = await fetch(url);
  const buffer = await response.buffer();
  const path = './images/download.jpg';
  fs.writeFile(path, buffer, (err) => {
    if (err)
      console.log(err);
  });
}

// FUNCTION TO ADD THE ADMIN IF NOT PRESENT
async function addAdmin() {
  admin = await User.findOne({username: "admin"});

  if (JSON.stringify(admin).length <= 4) {
    currentTime = new Date().toUTCString();
    const latestUser = new User({userid: 1, username: "admin", password: "Qwerty@123", time: currentTime, role: "admin"});
    latestUser
        .save()
        .then(() => {
          return true;
        })
        .catch((err) => console.log(err));
  }
}