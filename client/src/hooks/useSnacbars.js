import { useSnackbar } from "notistack";

export const useSnackbars = () => {
  const { enqueueSnackbar } = useSnackbar();

  const errorSnackbar = (message) => {
    enqueueSnackbar(message, {
      variant: "error",
    });
  };

  const successSnackbar = (message) => {
    enqueueSnackbar(message, {
      variant: "success",
    });
  };
  return { errorSnackbar, successSnackbar };
};
