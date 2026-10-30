import React, { useState, useMemo } from "react"
import ReactDOM from "react-dom/client"
import ContributionSkyline, {
  type ContributionDay,
  type PaletteName,
} from "@/components/ui/contribution-skyline"
import "./styles/tailwind.css"

function loadUserContributionDays(): ContributionDay[] | undefined {
  try {
    const rawUser = localStorage.getItem("oops_session") || localStorage.getItem("ck_user")
    const user = rawUser ? JSON.parse(rawUser) : null
    if (!user || !user.id) return undefined

    const prefix = `oops_sub:${user.id}:`
    const days: ContributionDay[] = []
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i)
      if (k && k.startsWith(prefix)) {
        const items = JSON.parse(localStorage.getItem(k) || "[]")
        for (const it of items) {
          if (it && it.time) {
            const d = new Date(it.time)
            if (!isNaN(d.getTime())) {
              const iso = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`
              days.push({ date: iso, count: 1 })
            }
          }
        }
      }
    }
    return days.length >= 5 ? days : undefined
  } catch {
    return undefined
  }
}

const PALETTE_OPTIONS: { id: PaletteName; label: string }[] = [
  { id: "ember", label: "Ember" },
  { id: "github", label: "GitHub" },
  { id: "grape", label: "Grape" },
  { id: "ocean", label: "Ocean" },
  { id: "mono", label: "Mono" },
]

function DashboardSkylineSection() {
  const [palette, setPalette] = useState<PaletteName>("ember")
  const userData = useMemo(() => loadUserContributionDays(), [])

  return (
    <div className="w-full">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2.5">
          <span
            className="inline-flex h-8 w-8 items-center justify-center rounded-lg border text-sm"
            style={{
              background: "rgba(255, 107, 74, 0.1)",
              borderColor: "rgba(255, 107, 74, 0.25)",
              color: "var(--coral, #ff6b4a)",
            }}
            aria-hidden="true"
          >
            <svg
              viewBox="0 0 24 24"
              width="17"
              height="17"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z" />
            </svg>
          </span>
          <div>
            <h2
              className="m-0 text-[16px] font-bold tracking-tight"
              style={{ color: "var(--text-main, #f3f3f7)" }}
            >
              Contribution Skyline
            </h2>
            <p
              className="m-0 text-[12px]"
              style={{ color: "var(--text-sub, #8d8f9d)" }}
            >
              Interactive 2D heat map &amp; 3D isometric practice skyline
            </p>
          </div>
        </div>

        <div
          className="inline-flex items-center gap-1 rounded-lg border p-1"
          style={{
            background: "var(--bg-sunken, #0f1014)",
            borderColor: "var(--border-subtle, rgba(255,255,255,0.08))",
          }}
          role="group"
          aria-label="Skyline color palette"
        >
          {PALETTE_OPTIONS.map((opt) => {
            const active = palette === opt.id
            return (
              <button
                key={opt.id}
                type="button"
                onClick={() => setPalette(opt.id)}
                aria-pressed={active}
                className="cursor-pointer rounded-md border-0 px-2.5 py-1 text-[11.5px] font-medium transition-colors"
                style={{
                  background: active ? "var(--text-main, #f3f3f7)" : "transparent",
                  color: active ? "var(--bg-card, #15161b)" : "var(--text-sub, #8d8f9d)",
                }}
              >
                {opt.label}
              </button>
            )
          })}
        </div>
      </div>

      <ContributionSkyline
        data={userData}
        defaultView="3d"
        palette={palette}
        unit="submission"
        unitPlural="submissions"
      />
    </div>
  )
}

const mountEl = document.getElementById("dashboard-skyline-root")
if (mountEl) {
  ReactDOM.createRoot(mountEl).render(
    <React.StrictMode>
      <DashboardSkylineSection />
    </React.StrictMode>
  )
}
