const mongoose = require('mongoose');

module.exports = () => {
  // MongoDB connection
  mongoose.connect("mongodb://mongo:27017/simpleapp", {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    })
    .then(() => {
      console.log("Connection successful...");
    })
    .catch((err) => {
      console.log(err);
    }); 
};