import axios from "axios";
const api = {
  getData: () => axios.get("http://localhost:5000/articles"),
};

export default api;
