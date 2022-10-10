import axios from "axios";
import { useNavigate } from "react-router";
import { useSnackbars } from "./useSnacbars";

export const useGetShopInfo = () => {
  const { errorSnackbar } = useSnackbars();
  let navigate = useNavigate();

  const getShopInfo = (shopName) => {
    axios
      .get(`${process.env.REACT_APP_PORT}/${shopName}`)
      .then((res) => {
        console.log(res.data[0]);
        navigate(`/shop/${shopName}`, {
          state: {
            shopInfoData: res.data[0],
          },
        });
        return res;
      })
      .catch((err) => {
        errorSnackbar(err.response.data.message);
      });
  };

  return { getShopInfo };
};
