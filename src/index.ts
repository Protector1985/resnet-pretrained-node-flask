import App from "./app";
require("dotenv").config();

const port = process.env.NODE_JS_PORT as string

try {

   const application = new App({
        port,
    })
    
    application.startServer();

} catch(err) {
    console.log(err)
}