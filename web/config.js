// OOPS Judge Configuration
// Automatically detects environment (local development vs production Render URL),
// and allows overriding via URL parameter (?runner_url=https://...) for instant testing.

(function () {
  const isLocal =
    window.location.hostname === "localhost" ||
    window.location.hostname === "127.0.0.1";

  // Production Render runner URL (update if your Render service slug differs)
  const PROD_RUNNER_URL = "https://oops-judge-runner.onrender.com";
  const LOCAL_RUNNER_URL = window.location.port
    ? `${window.location.protocol}//${window.location.hostname}:${window.location.port}`
    : `${window.location.protocol}//${window.location.hostname}:8000`;

  window.CONFIG = {
    RUNNER_URL: isLocal ? LOCAL_RUNNER_URL : PROD_RUNNER_URL,
    PROD_RUNNER_URL: PROD_RUNNER_URL,
    LOCAL_RUNNER_URL: LOCAL_RUNNER_URL,
  };
})();
