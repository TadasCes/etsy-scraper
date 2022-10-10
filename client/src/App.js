import { Routes, Route } from "react-router-dom";
import Home from "./components/Home/Home";
import { ShopListings } from "./components/ShopListings/ShopListings";
import { ShopSales } from "./components/ShopSales/ShopSales";
import { ListingDetails } from "./components/ShopListings/ListingDetails";
import ShopInfo from "./components/ShopInfo/ShopInfo";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/shop/:shopName" element={<ShopInfo />}>
        <Route path="/shop/:shopName/listings" element={<ShopListings />} />
        <Route
          path="/shop/:shopName/listings/:listingId"
          element={<ListingDetails />}
        />
        <Route path="/shop/:shopName/sales" element={<ShopSales />} />
      </Route>
    </Routes>
  );
}

export default App;
