import axios from "axios";
import { useState } from "react";

export const useGetSalesData = () => {
  const [shopName, setShopName] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  const getProductData = () =>
    axios
      .get(`${process.env.REACT_APP_PORT}/${shopName}`)
      .then((res) => {
        setLoading(false);
        setData(res.data);
        setErrorMessage("");
        return res;
      })
      .catch((err) => {
        setErrorMessage(err.response.data.message);
      });

  return { shopName, setShopName, getProductData, errorMessage, loading, data };
};
