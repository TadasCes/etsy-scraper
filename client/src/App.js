import "./style.css";
import { Button, TextField, Box, Typography } from "@mui/material";
import { useGetSalesData } from "./hooks/useGetSalesData";

function App() {
  const { shopName, setShopName, getProductData, errorMessage, data } =
    useGetSalesData();

  return (
    <div className="App">
      <header className="App-header">
        <Box display="flex" flexDirection="column" sx={{ marginTop: "20px" }}>
          <TextField
            label="Shop namee:  "
            value={shopName}
            onChange={(e) => setShopName(e.target.value)}
          />
          <Button type="submit" variant="contained" onClick={getProductData}>
            Search
          </Button>
        </Box>
        <Typography variant="h5" sx={{ marginTop: "20px" }}>
          Shop name: {shopName}
        </Typography>
        {errorMessage !== "" && (
          <Typography className="error-message">{errorMessage}</Typography>
        )}
        <Typography>{JSON.stringify(data)}</Typography>
        {/* {!loading && <ProductGrid data={data} />} */}
      </header>
    </div>
  );
}

export default App;
