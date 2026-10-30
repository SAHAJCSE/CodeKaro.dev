import path from "path";
import { fileURLToPath } from "url";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  build: {
    rollupOptions: {
      input: {
        index: "src/main.jsx",
        "auth-client": "src/auth-client.ts",
        "dashboard-skyline": "src/dashboard-skyline.tsx",
        "testimonials-entry": "src/testimonials-entry.tsx",
        "not-found-entry": "src/not-found-entry.tsx",
      },
      output: {
        entryFileNames: "assets/[name].js",
        chunkFileNames: "assets/[name]-[hash].js",
        assetFileNames: "assets/[name].[ext]",
      },
    },
  },
  server: {
    host: "0.0.0.0",
    port: 3000,
    open: false,
    hmr: false,
  },
});
