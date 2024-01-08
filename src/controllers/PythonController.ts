import express, { Router, Request, Response } from "express";
import PythonService from "../services/PythonService";
import multer, { Multer } from "multer";
import FormData from "form-data";

class PythonController extends PythonService {
  private basepath: string = "/ai";
  public router: Router = express.Router();
  private uploadEngine: Multer = multer({ storage: multer.memoryStorage() }); //storage engine - stores in memory

  constructor() {
    super();
    this.initRoutes();
  }

  initRoutes() {
    this.router.post(
      this.basepath + "/sendData",
      this.uploadEngine.single("image"),
      this.submitToFlask,
    );
  }

  //BELOW HAS TO BE ERROR FUNCTION otherwise this.sendData is undefined due to context
  submitToFlask = async (req: Request, res: Response) => {
    if (typeof req.file === "object") {
      const formData = new FormData();
      formData.append("file", req.file.buffer, {
        filename: req.file.originalname,
        contentType: req.file.mimetype,
      });
      const resp = await this.sendData(formData);
      if (resp.success) {
        res.send("OK");
      } else {
        res.send("Error");
      }
    } else {
      res.send("Wrong file format");
    }
  };
}

export default PythonController;
