import React from "react";
import ReactDOM from "react-dom/client";
import { SnackbarProvider } from "notistack";

import { BrowserRouter } from "react-router-dom";
import App from "./App";
import { IconButton } from "@mui/material";
import { Close } from "@mui/icons-material";
import { useSnackbars } from "./hooks/useSnacbars";

function SnackbarCloseButton({ snackbarKey }) {
  const { closeSnackbar } = useSnackbars();

  return (
    <IconButton onClick={() => closeSnackbar(snackbarKey)}>
      <Close style={{ color: "white" }} />
    </IconButton>
  );
}

const Snackbars = ({ children }) => {
  return (
    <SnackbarProvider
      maxSnack={3}
      preventDuplicate={true}
      anchorOrigin={{ vertical: "bottom", horizontal: "right" }}
      action={(snackbarKey) => (
        <SnackbarCloseButton snackbarKey={snackbarKey} />
      )}
    >
      {children}
    </SnackbarProvider>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Snackbars children={<App />} />
    </BrowserRouter>
  </React.StrictMode>
);
