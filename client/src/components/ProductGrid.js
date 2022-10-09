import {
  Grid,
  Typography,
  Card,
  CardMedia,
  CardContent,
  Link,
} from "@mui/material";
import axios from "axios";
import { useState, useEffect } from "react";

export default function ProductGrid({ data }) {
  const goToEtsyPage = (url) => {
    window.open(url);
  };

  const shortenTitle = (title) => {
    return title.slice(0, 80) + " ...";
  };

  return (
    <>
      <Grid
        container
        display="flex"
        justifyContent="space-between"
        sx={{ margin: "100px" }}
      >
        {data.map((product) => {
          return (
            <Grid
              key={product.name}
              item
              xs={12}
              md={6}
              lg={4}
              sx={{ margin: "24px 0", padding: "16px" }}
            >
              <Card sx={{ padding: "8px" }}>
                <CardMedia
                  component="img"
                  height="100"
                  image={product.image}
                  alt={product.image}
                  onClick={() => goToEtsyPage(product.link)}
                  sx={{ cursor: "pointer" }}
                />

                <CardContent>
                  <Typography
                    variant="body1"
                    sx={{ textAlign: "left", fontWeight: "bold" }}
                  >
                    {shortenTitle(product.name)}
                  </Typography>
                  <Typography variant="body1" sx={{ textAlign: "left" }}>
                    Products sold: {product.sold}
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          );
        })}
      </Grid>
    </>
  );
}
