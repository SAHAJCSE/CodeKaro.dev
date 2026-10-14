const problemList = document.querySelector("#problem-list");
const searchInput = document.querySelector("#problem-search");
const editor = document.querySelector("#code-editor");
const runButton = document.querySelector("#run-button");
const saveButton = document.querySelector("#save-button");
const output = document.querySelector("#console-output");
const lineNumbers = document.querySelector("#line-numbers");
const dirtyIndicator = document.querySelector("#dirty-indicator");
const saveStatus = document.querySelector("#save-status");
const visibleCount = document.querySelector("#visible-count");
let problems = [];
let currentProblem = null;
let savedCode = "";
let requestVersion = 0;
let runStartedAt = 0;

async function requestJson(url, options) {
  const response = await fetch(url, options);
  const result = await response.json();
  if (!response.ok) throw new Error(result.error || `Request failed (${response.status}).`);
  return result;
}

function escapeHtml(value) {
  return value.replace(/[&<>"']/g, character => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  })[character]);
}

function inlineMarkdown(text) {
  return escapeHtml(text)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>");
}

function renderMarkdown(markdown) {
  const lines = markdown.split(/\r?\n/);
  const html = [];
  let paragraph = [];
  let listType = null;
  let tableRows = [];
  let inCode = false;
  let codeLines = [];

  const flushParagraph = () => {
    if (paragraph.length) {
      html.push(`<p>${paragraph.map(inlineMarkdown).join("<br>")}</p>`);
      paragraph = [];
    }
  };
  const flushList = () => {
    if (listType) {
      html.push(`</${listType}>`);
      listType = null;
    }
  };
  const flushTable = () => {
    if (tableRows.length) {
      const rows = tableRows.filter(row => !/^\|?[\s|:-]+\|?$/.test(row.trim()));
      if (rows.length) {
        const cells = row => row.trim().replace(/^\||\|$/g, "").split("|").map(cell => cell.trim());
        const header = cells(rows[0]);
        html.push("<table><thead><tr>" + header.map(cell => `<th>${inlineMarkdown(cell)}</th>`).join("") + "</tr></thead><tbody>");
        for (const row of rows.slice(1)) {
          html.push("<tr>" + cells(row).map(cell => `<td>${inlineMarkdown(cell)}</td>`).join("") + "</tr>");
        }
        html.push("</tbody></table>");
      }
      tableRows = [];
    }
  };

  for (const line of lines) {
    if (line.trim().startsWith("```")) {
      flushParagraph();
      flushList();
      flushTable();
      if (inCode) {
        html.push(`<pre><code>${escapeHtml(codeLines.join("\n"))}</code></pre>`);
        codeLines = [];
      }
      inCode = !inCode;
      continue;
    }
    if (inCode) {
      codeLines.push(line);
      continue;
    }

    const trimmed = line.trim();
    if (trimmed.startsWith("|")) {
      flushParagraph();
      flushList();
      tableRows.push(trimmed);
      continue;
    }
    flushTable();
    const heading = /^(#{1,3})\s+(.+)$/.exec(trimmed);
    if (heading) {
      flushParagraph();
      flushList();
      const level = heading[1].length;
      html.push(`<h${level}>${inlineMarkdown(heading[2])}</h${level}>`);
      continue;
    }
    const listItem = /^[-*]\s+(.+)$/.exec(trimmed);
    if (listItem) {
      flushParagraph();
      if (listType !== "ul") {
        flushList();
        html.push("<ul>");
        listType = "ul";
      }
      html.push(`<li>${inlineMarkdown(listItem[1])}</li>`);
      continue;
    }
    if (!trimmed) {
      flushParagraph();
      flushList();
      continue;
    }
    if (trimmed.startsWith("*Source:")) continue;
    paragraph.push(trimmed);
  }
  flushParagraph();
  flushList();
  flushTable();
  if (inCode) html.push(`<pre><code>${escapeHtml(codeLines.join("\n"))}</code></pre>`);
  return html.join("\n");
}

function renderProblemList() {
  const query = searchInput.value.trim().toLowerCase();
  const filtered = problems.filter(problem =>
    problem.title.toLowerCase().includes(query) ||
    problem.id.includes(query) ||
    problem.summary.toLowerCase().includes(query)
  );
  visibleCount.textContent = query ? `${filtered.length} shown` : "";
  if (!filtered.length) {
    problemList.innerHTML = '<div class="empty-list">No matching problems.</div>';
    return;
  }
  problemList.innerHTML = filtered.map(problem => `
    <button class="problem-item${problem.id === currentProblem ? " selected" : ""}" data-problem="${escapeHtml(problem.id)}">
      <span class="problem-number">${String(problems.indexOf(problem) + 1).padStart(2, "0")}</span>
      <span class="problem-item-text"><span class="problem-title">${escapeHtml(problem.title)}</span><span class="problem-slug">${escapeHtml(problem.id)}</span></span>
    </button>
  `).join("");
}

function updateDirtyState() {
  const dirty = editor.value !== savedCode;
  dirtyIndicator.hidden = !dirty;
  saveButton.disabled = !currentProblem || !dirty;
  runButton.disabled = !currentProblem;
  saveStatus.textContent = dirty ? "Unsaved changes" : (currentProblem ? "Saved" : "");
}

function updateLineNumbers() {
  const count = editor.value.split("\n").length;
  lineNumbers.textContent = Array.from({ length: count }, (_, index) => index + 1).join("\n");
  lineNumbers.scrollTop = editor.scrollTop;
}

function updateCursorPosition() {
  const beforeCursor = editor.value.slice(0, editor.selectionStart);
  const lines = beforeCursor.split("\n");
  document.querySelector("#cursor-position").textContent =
    `Ln ${lines.length}, Col ${lines[lines.length - 1].length + 1}`;
}

function showMessage(message, isError = false) {
  output.innerHTML = `<div class="result-banner ${isError ? "failed" : ""}">${escapeHtml(message)}</div>`;
  document.querySelector("#run-duration").textContent = "";
}

async function selectProblem(problemId) {
  const version = ++requestVersion;
  currentProblem = problemId;
  renderProblemList();
  editor.disabled = true;
  runButton.disabled = true;
  saveButton.disabled = true;
  document.querySelector("#welcome-state").hidden = true;
  document.querySelector("#problem-description").hidden = true;
  document.querySelector("#breadcrumb-title").textContent = "Loading…";
  document.querySelector("#problem-id").textContent = "";
  showMessage("Loading problem…");
  try {
    const problem = await requestJson(`/api/problems/${encodeURIComponent(problemId)}`);
    if (version !== requestVersion) return;
    document.querySelector("#breadcrumb-title").textContent = problem.title;
    document.querySelector("#problem-id").textContent = problem.id;
    const description = document.querySelector("#problem-description");
    description.innerHTML = renderMarkdown(problem.readme);
    description.hidden = false;
    const localSaved = localStorage.getItem(`oops_code_${problemId}`);
    const codeToShow = (localSaved !== null) ? localSaved : problem.solution;
    editor.value = codeToShow;
    savedCode = codeToShow;
    editor.disabled = false;
    updateDirtyState();
    updateLineNumbers();
    updateCursorPosition();
    output.innerHTML = '<div class="console-placeholder"><span class="terminal-icon">›_</span><span>Run your code to see test results here.</span></div>';
  } catch (error) {
    if (version !== requestVersion) return;
    showMessage(error.message, true);
  }
}

async function saveSolution(runAfterSave = false) {
  if (!currentProblem) return;
  const problemId = currentProblem;
  const version = requestVersion;
  const source = editor.value;
  runButton.disabled = true;
  saveButton.disabled = true;
  saveStatus.textContent = runAfterSave ? "Running…" : "Saving…";
  if (runAfterSave) {
    runStartedAt = performance.now();
    output.innerHTML = '<div class="console-placeholder"><span class="terminal-icon">›_</span><span>Compiling and running tests…</span></div>';
    document.querySelector("#run-duration").textContent = "";
  }
  try {
    localStorage.setItem(`oops_code_${problemId}`, source);
    const result = await requestJson(`/api/problems/${encodeURIComponent(problemId)}/${runAfterSave ? "run" : "save"}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code: source }),
    });
    if (version !== requestVersion || currentProblem !== problemId) return;
    if (editor.value === source) savedCode = source;
    updateDirtyState();
    if (runAfterSave) {
      const duration = ((performance.now() - runStartedAt) / 1000).toFixed(2);
      document.querySelector("#run-duration").textContent = `${duration}s`;
      const passed = result.passed;
      output.innerHTML = `<div class="result-banner ${passed ? "accepted" : "failed"}">${passed ? "✓ ACCEPTED" : "× NOT ACCEPTED"}</div><pre class="result-output">${escapeHtml(result.output || result.error || "The judge returned no output.")}</pre>`;
      if (result.error) output.querySelector(".result-output").textContent += `\n${result.error}`;
    }
  } catch (error) {
    if (version !== requestVersion || currentProblem !== problemId) return;
    showMessage(error.message, true);
    saveStatus.textContent = "Save failed";
  } finally {
    if (version === requestVersion && currentProblem === problemId) updateDirtyState();
  }
}

problemList.addEventListener("click", event => {
  const button = event.target.closest("[data-problem]");
  if (!button || button.dataset.problem === currentProblem) return;
  if (editor.value !== savedCode && !window.confirm("You have unsaved changes. Discard them and open another problem?")) return;
  selectProblem(button.dataset.problem);
});
searchInput.addEventListener("input", renderProblemList);
editor.addEventListener("input", () => {
  updateDirtyState();
  updateLineNumbers();
  updateCursorPosition();
});
editor.addEventListener("scroll", () => { lineNumbers.scrollTop = editor.scrollTop; });
editor.addEventListener("click", updateCursorPosition);
editor.addEventListener("keyup", updateCursorPosition);
editor.addEventListener("keydown", event => {
  if (event.key === "Tab") {
    event.preventDefault();
    const start = editor.selectionStart;
    const end = editor.selectionEnd;
    editor.setRangeText("    ", start, end, "end");
    editor.dispatchEvent(new Event("input"));
  }
  if (event.key === "Enter" && (event.ctrlKey || event.metaKey)) {
    event.preventDefault();
    saveSolution(true);
  }
});
saveButton.addEventListener("click", () => saveSolution());
runButton.addEventListener("click", () => saveSolution(true));
document.querySelector("#refresh-button").addEventListener("click", loadProblems);
document.addEventListener("keydown", event => {
  if (event.key === "/" && document.activeElement !== searchInput && document.activeElement !== editor) {
    event.preventDefault();
    searchInput.focus();
  }
  if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "s") {
    event.preventDefault();
    if (!saveButton.disabled) saveSolution();
  }
});

async function loadProblems() {
  problemList.innerHTML = '<div class="empty-list">Loading problems…</div>';
  try {
    const result = await requestJson("/api/problems");
    problems = result.problems;
    document.querySelector("#problem-count").textContent = problems.length;
    renderProblemList();
    if (problems.length && !currentProblem) selectProblem(problems[0].id);
  } catch (error) {
    problemList.innerHTML = `<div class="empty-list">${escapeHtml(error.message)}</div>`;
  }
}

loadProblems();
