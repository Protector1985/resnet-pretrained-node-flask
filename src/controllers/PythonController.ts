import express, { Router, Request, Response } from "express";
import PythonService from "../services/PythonService";


class PythonController extends PythonService {
    private basepath:string = "/ai"
    public router:Router = express.Router()

    constructor() {
        super()
        this.initRoutes()
    }

    initRoutes() {
        this.router.post(this.basepath + "/sendData", this.submitToFlask)
    }

    //BELOW HAS TO BE ERROR FUNCTION otherwise this.sendData is undefined due to context
    submitToFlask = async (req:Request, res:Response) => {
        const resp = await this.sendData(req.body)
        console.log(resp)
        if(resp.success) {
            res.send("OK")
        } else {
            res.send("Error")
        }
        
    }
    
}

export default PythonController;