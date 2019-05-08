import axios from 'axios'

class httpService {

    constructor() {
        this._axios = axios.create({
            baseURL: 'http://127.0.0.1:5000/'
        })
    }

    get(path) {
        return this._axios.get(path)
    }
}

export default new httpService();