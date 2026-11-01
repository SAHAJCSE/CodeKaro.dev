// Code-Karo.dev Configuration
// Automatically detects environment, uses local/current origin by default,
// supports localStorage override ('oops_runner_url'), and allows URL parameter (?runner_url=https://...).

(function () {
  const originUrl =
    window.location.origin && window.location.origin !== "null"
      ? window.location.origin.replace(/\/+$/, "")
      : `${window.location.protocol}//${window.location.hostname}${window.location.port ? ":" + window.location.port : ""}`;

  const PROD_RUNNER_URL = originUrl;
  const LOCAL_RUNNER_URL = originUrl;

  let customUrl = null;
  try {
    const param = new URLSearchParams(window.location.search).get("runner_url");
    if (param) {
      customUrl = param.replace(/\/+$/, "");
      localStorage.setItem("oops_runner_url", customUrl);
    } else {
      const stored = localStorage.getItem("oops_runner_url");
      if (stored && !stored.includes("oops-judge.onrender.com")) {
        customUrl = stored.replace(/\/+$/, "");
      } else if (stored && stored.includes("oops-judge.onrender.com")) {
        localStorage.removeItem("oops_runner_url");
      }
    }
  } catch (e) {}

  window.CONFIG = {
    RUNNER_URL: customUrl || originUrl,
    PROD_RUNNER_URL: PROD_RUNNER_URL,
    LOCAL_RUNNER_URL: LOCAL_RUNNER_URL,
  };
})();
