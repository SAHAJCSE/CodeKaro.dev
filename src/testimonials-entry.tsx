import React from "react";
import ReactDOM from "react-dom/client";
import { StaggerTestimonials } from "@/components/ui/stagger-testimonials";
import { FeaturesBento } from "@/components/ui/features-bento";
import { FaqSection } from "@/components/ui/faq-accordion";
import "./styles/tailwind.css";

const featuresMountEl = document.getElementById("features-bento-root");
if (featuresMountEl) {
  ReactDOM.createRoot(featuresMountEl).render(
    <React.StrictMode>
      <FeaturesBento />
    </React.StrictMode>
  );
}

const faqsMountEl = document.getElementById("faqs-root");
if (faqsMountEl) {
  ReactDOM.createRoot(faqsMountEl).render(
    <React.StrictMode>
      <FaqSection />
    </React.StrictMode>
  );
}

const mountEl = document.getElementById("stagger-testimonials-root");
if (mountEl) {
  ReactDOM.createRoot(mountEl).render(
    <React.StrictMode>
      <StaggerTestimonials />
    </React.StrictMode>
  );
}
