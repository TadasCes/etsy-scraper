import "../../style.css";
import { Button, TextField, Box } from "@mui/material";
import { useGetShopInfo } from "../../hooks/useGetShopInfo";
import { useState } from "react";

function Home() {
  const [shopName, setShopName] = useState("");
  const { getShopInfo } = useGetShopInfo();

  return (
    <>
      <>
        <div className="Home">
          <Box display="flex" flexDirection="column" sx={{ marginTop: "20px" }}>
            <TextField
              label="Shop namee:  "
              value={shopName}
              onChange={(e) => setShopName(e.target.value)}
            />
            <Button
              type="submit"
              variant="contained"
              onClick={() => getShopInfo(shopName)}
            >
              Search
            </Button>
          </Box>
        </div>
      </>
    </>
  );
}

export default Home;
