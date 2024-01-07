require("dotenv").config();
import axios from 'axios'


class PythonService {

    async sendData(data:string) {
       try {
        const response = await axios.post(process.env.FLASK_SERVER_URL as string, data);
            return {
                success: true,
                data:response
            }
       } catch(err) {
            return {
                success: false,
                data: err
            }
       }
       
    }

}

export default PythonService