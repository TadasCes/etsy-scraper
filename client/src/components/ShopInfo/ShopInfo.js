import "../../style.css";
import { Box, Typography, Grid } from "@mui/material";
import { useLocation } from "react-router";

export const ShopInfo = () => {
  const { state } = useLocation();

  return (
    <Grid container>
      {state.shopInfoData.listings.map((listing) => {
        return (
          <Grid item key={listing.link}>
            <Typography>{listing.title}</Typography>
            <Typography>{listing.price}</Typography>
            <a href={listing.link}>
              <Box
                component="img"
                sx={{
                  height: 233,
                  width: 350,
                  maxHeight: { xs: 233, md: 167 },
                  maxWidth: { xs: 350, md: 250 },
                }}
                src={listing.img}
              />
            </a>
          </Grid>
        );
      })}
    </Grid>
  );
};

export default ShopInfo;
