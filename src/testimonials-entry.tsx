import React from "react";
import ReactDOM from "react-dom/client";
import { StaggerTestimonials } from "@/components/ui/stagger-testimonials";
import "./styles/tailwind.css";

const mountEl = document.getElementById("stagger-testimonials-root");
if (mountEl) {
  ReactDOM.createRoot(mountEl).render(
    <React.StrictMode>
      <StaggerTestimonials />
    </React.StrictMode>
  );
}
