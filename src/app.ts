import express, { Application } from 'express'

class App {
    private app:Application = express();
    private port:string;
    constructor(props:{port:string}) {
        this.port = props.port
    }

    startServer() {
        this.app.listen(this.port, () => {
            console.log(`Server listening on port ${this.port} `)
        })
    }
}

export default App