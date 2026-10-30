import React from "react";
import ReactDOM from "react-dom/client";
import { NotFound } from "@/components/ui/not-found-2";
import "./styles/tailwind.css";

const mountEl = document.getElementById("not-found-root");
if (mountEl) {
  ReactDOM.createRoot(mountEl).render(
    <React.StrictMode>
      <NotFound />
    </React.StrictMode>
  );
}
