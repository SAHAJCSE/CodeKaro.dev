import React, { useState, useMemo, useEffect } from "react"
import ReactDOM from "react-dom/client"
import { Check } from "lucide-react"
import ContributionSkyline, {
  type ContributionDay,
  type PaletteName,
} from "@/components/ui/contribution-skyline"
import AvatarPicker, {
  MorphingFace,
  avatarSeed,
  faceToSvgDataUri,
  type AvatarValue,
} from "@/components/ui/avatar-picker"
import { Skeleton } from "@/components/ui/skeleton"
import "./styles/tailwind.css"

interface StoredUserProfile {
  id: string
  username: string
  name: string
  email?: string
  variant: number
  seed: string
  totalSubmissions: number
  solvedCount: number
  streakCount: number
}

function readStoredUserProfile(): StoredUserProfile {
  try {
    const rawSession = localStorage.getItem("oops_session")
    const rawCkUser = localStorage.getItem("ck_user")
    const rawAvatar = localStorage.getItem("ck_avatar")

    const sessionUser = rawSession ? JSON.parse(rawSession) : null
    const ckUser = rawCkUser ? JSON.parse(rawCkUser) : null
    const avatarData = rawAvatar ? JSON.parse(rawAvatar) : null

    const user = sessionUser || ckUser || {}
    const displayName =
      avatarData?.displayName ||
      user.name ||
      user.username ||
      (user.email ? user.email.split("@")[0] : "CodeKaro Coder")
    const username =
      user.username ||
      (user.email ? user.email.split("@")[0] : displayName.toLowerCase().replace(/\s+/g, ""))
    const variant = typeof avatarData?.variant === "number" ? avatarData.variant : 0
    const seed = avatarData?.seed || avatarSeed(displayName, variant)
    const userId = user.id || user.uid || "guest"

    let totalSubmissions = 0
    let solvedCount = 0
    const submissionsByDay = new Map<string, number>()

    if (userId && userId !== "guest") {
      const subPrefix = `oops_sub:${userId}:`
      const statusPrefix = `oops_status:${userId}:`
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i)
        if (!k) continue
        if (k.startsWith(subPrefix)) {
          const items = JSON.parse(localStorage.getItem(k) || "[]")
          if (Array.isArray(items)) {
            totalSubmissions += items.length
            for (const it of items) {
              if (it?.time) {
                const d = new Date(it.time)
                if (!isNaN(d.getTime())) {
                  const key = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`
                  submissionsByDay.set(key, (submissionsByDay.get(key) || 0) + 1)
                }
              }
            }
          }
        } else if (k.startsWith(statusPrefix) && localStorage.getItem(k) === "solved") {
          solvedCount += 1
        }
      }
    }

    let streakCount = 0
    if (submissionsByDay.size > 0) {
      const today = new Date()
      today.setHours(0, 0, 0, 0)
      const fmt = (d: Date) =>
        `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`
      const cursor = new Date(today)
      if (!submissionsByDay.has(fmt(cursor))) {
        cursor.setDate(cursor.getDate() - 1)
      }
      while (submissionsByDay.has(fmt(cursor))) {
        streakCount += 1
        cursor.setDate(cursor.getDate() - 1)
      }
    } else {
      totalSubmissions = 77
      solvedCount = 47
      streakCount = 12
    }

    return {
      id: userId,
      username,
      name: displayName,
      email: user.email,
      variant,
      seed,
      totalSubmissions,
      solvedCount,
      streakCount,
    }
  } catch {
    return {
      id: "guest",
      username: "coder",
      name: "CodeKaro Coder",
      variant: 0,
      seed: avatarSeed("CodeKaro Coder", 0),
      totalSubmissions: 77,
      solvedCount: 47,
      streakCount: 12,
    }
  }
}

function loadUserContributionDays(): ContributionDay[] | undefined {
  try {
    const rawUser = localStorage.getItem("oops_session") || localStorage.getItem("ck_user")
    const user = rawUser ? JSON.parse(rawUser) : null
    const userId = user?.id || user?.uid
    if (!userId) return undefined

    const prefix = `oops_sub:${userId}:`
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

function DashboardProfileSection() {
  const initialProfile = useMemo(() => readStoredUserProfile(), [])
  const [avatarVal, setAvatarVal] = useState<AvatarValue>({
    displayName: initialProfile.name,
    variant: initialProfile.variant,
  })
  const [savedNotice, setSavedNotice] = useState(false)
  const [showPicker, setShowPicker] = useState(false)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    const timer = setTimeout(() => setIsLoading(false), 600)
    return () => {
      clearTimeout(timer)
    }
  }, [])

  const currentSeed = avatarSeed(avatarVal.displayName || "Coder", avatarVal.variant)
  const handleSlug =
    (avatarVal.displayName || initialProfile.username || "coder")
      .trim()
      .toLowerCase()
      .replace(/[^a-z0-9_]/g, "") || "coder"

  const persistProfile = (next: AvatarValue & { seed: string }) => {
    try {
      const dataUri = faceToSvgDataUri(next.seed)
      localStorage.setItem(
        "ck_avatar",
        JSON.stringify({
          displayName: next.displayName,
          variant: next.variant,
          seed: next.seed,
          avatar: dataUri,
        })
      )

      const rawSession = localStorage.getItem("oops_session")
      const sessionObj = rawSession ? JSON.parse(rawSession) : { id: initialProfile.id || "local_user" }
      sessionObj.name = next.displayName
      sessionObj.username = sessionObj.username || handleSlug
      sessionObj.avatar = dataUri
      sessionObj.picture = dataUri
      localStorage.setItem("oops_session", JSON.stringify(sessionObj))

      const rawCk = localStorage.getItem("ck_user")
      if (rawCk) {
        const ckObj = JSON.parse(rawCk)
        ckObj.name = next.displayName
        ckObj.avatar = dataUri
        ckObj.picture = dataUri
        localStorage.setItem("ck_user", JSON.stringify(ckObj))
      }

      window.dispatchEvent(new Event("storage"))
      setSavedNotice(true)
      setTimeout(() => setSavedNotice(false), 2400)
    } catch {
      // ignore storage errors
    }
  }

  if (isLoading) {
    return (
      <div className="grid grid-cols-1 gap-6 lg:grid-cols-12">
        <div className="lg:col-span-12">
          <div className="shadow-panel w-full space-y-5 rounded-lg bg-transparent p-4">
            <Skeleton className="h-32 w-full rounded-lg" />
            <div className="space-y-3">
              <Skeleton className="h-3 w-3/5 rounded-lg" />
              <Skeleton className="h-3 w-4/5 rounded-lg" />
              <Skeleton className="h-3 w-2/5 rounded-lg" />
            </div>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="grid grid-cols-1 items-start gap-6 lg:grid-cols-12">
      {/* Left: Combined Profile Overview & Key Stats */}
      <div
        className={`flex flex-col justify-between gap-6 ${
          showPicker ? "lg:col-span-7" : "lg:col-span-12"
        }`}
      >
        <div
          className="flex flex-wrap items-center justify-between gap-4 border-b pb-5"
          style={{ borderColor: "var(--border-card)" }}
        >
          <div className="flex items-center gap-4">
            <div
              className="relative h-20 w-20 shrink-0 overflow-hidden rounded-full border shadow-sm"
              style={{ borderColor: "var(--border-card)" }}
            >
              <MorphingFace seed={currentSeed} />
            </div>
            <div>
              <h1
                className="m-0 text-xl font-bold tracking-tight"
                style={{ color: "var(--text-main)" }}
              >
                {avatarVal.displayName.trim() || "CodeKaro Coder"}
              </h1>
              <p
                className="m-0 mt-1 font-mono text-base"
                style={{ color: "var(--text-sub)" }}
              >
                @{handleSlug}
              </p>
              {savedNotice && (
                <p className="m-0 mt-1.5 inline-flex items-center gap-1.5 text-sm font-medium text-[#8b5cf6]">
                  <Check className="size-4" /> Profile saved
                </p>
              )}
            </div>
          </div>

          <div className="flex items-center gap-2.5">
            <button
              type="button"
              onClick={() => setShowPicker((v) => !v)}
              aria-expanded={showPicker}
              className="inline-flex cursor-pointer items-center justify-center rounded-lg border px-4 py-2 text-sm font-semibold transition-opacity hover:opacity-90"
              style={{
                background: showPicker ? "#8b5cf6" : "var(--bg-sunken)",
                color: showPicker ? "#ffffff" : "var(--text-main)",
                borderColor: showPicker ? "#8b5cf6" : "var(--border-card)",
              }}
            >
              {showPicker ? "Hide Avatar" : "Edit Avatar"}
            </button>
            <a
              href="/practice"
              className="inline-flex items-center justify-center rounded-lg border px-4 py-2 text-sm font-semibold no-underline transition-opacity hover:opacity-90"
              style={{
                background: "var(--text-main)",
                color: "var(--bg-card)",
                borderColor: "var(--text-main)",
              }}
            >
              Practice IDE
            </a>
          </div>
        </div>

        {/* Profile Stats Grid (Equal medium-size text, no extra icons or extra captions) */}
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
          <div
            className="rounded-xl border p-4"
            style={{
              background: "var(--bg-sunken)",
              borderColor: "var(--border-card)",
            }}
          >
            <div
              className="text-sm font-medium"
              style={{ color: "var(--text-sub)" }}
            >
              Submissions
            </div>
            <div
              className="mt-1.5 text-xl font-semibold"
              style={{ color: "var(--text-main)" }}
            >
              {initialProfile.totalSubmissions.toLocaleString()}
            </div>
          </div>

          <div
            className="rounded-xl border p-4"
            style={{
              background: "var(--bg-sunken)",
              borderColor: "var(--border-card)",
            }}
          >
            <div
              className="text-sm font-medium"
              style={{ color: "var(--text-sub)" }}
            >
              Day Streak
            </div>
            <div
              className="mt-1.5 text-xl font-semibold"
              style={{ color: "var(--text-main)" }}
            >
              {initialProfile.streakCount} days
            </div>
          </div>

          <div
            className="rounded-xl border p-4"
            style={{
              background: "var(--bg-sunken)",
              borderColor: "var(--border-card)",
            }}
          >
            <div
              className="text-sm font-medium"
              style={{ color: "var(--text-sub)" }}
            >
              Problems Solved
            </div>
            <div
              className="mt-1.5 text-xl font-semibold"
              style={{ color: "var(--text-main)" }}
            >
              {initialProfile.solvedCount} / 41
            </div>
          </div>
        </div>
      </div>

      {/* Right: Interactive KokonutUI AvatarPicker (opens only when user clicks Edit Avatar) */}
      {showPicker && (
        <div className="lg:col-span-5">
          <AvatarPicker
            value={avatarVal}
            defaultValue={{
              displayName: initialProfile.name,
              variant: initialProfile.variant,
            }}
            title="Profile Avatar"
            description="Drag the coin sideways, tap to flip, or shuffle."
            submitLabel={savedNotice ? "Saved ✓" : "Save Avatar"}
            onChange={(next) => {
              setAvatarVal({
                displayName: next.displayName,
                variant: next.variant,
              })
            }}
            onComplete={(next) => {
              setAvatarVal({
                displayName: next.displayName,
                variant: next.variant,
              })
              persistProfile(next)
            }}
            className="max-w-full shadow-sm"
          />
        </div>
      )}
    </div>
  )
}

const PALETTE_OPTIONS: { id: PaletteName; label: string }[] = [
  { id: "mono", label: "Mono" },
  { id: "grape", label: "Purple" },
  { id: "github", label: "GitHub" },
  { id: "ocean", label: "Ocean" },
  { id: "ember", label: "Ember" },
]

function DashboardSkylineSection() {
  const [palette, setPalette] = useState<PaletteName>("mono")
  const [isLoading, setIsLoading] = useState<boolean>(true)
  const userData = useMemo(() => loadUserContributionDays(), [])

  useEffect(() => {
    const timer = setTimeout(() => setIsLoading(false), 750)
    const onStateChange = (e: Event) => {
      const custom = e as CustomEvent<{ state?: string }>
      if (custom.detail?.state === "loading") {
        setIsLoading(true)
      } else {
        setIsLoading(false)
      }
    }
    window.addEventListener("ck-dashboard-state", onStateChange)
    return () => {
      clearTimeout(timer)
      window.removeEventListener("ck-dashboard-state", onStateChange)
    }
  }, [])

  return (
    <div className="w-full">
      <div className="mb-4 flex flex-wrap items-center justify-between gap-3">
        <h2
          className="m-0 text-lg font-semibold tracking-tight"
          style={{ color: "var(--text-main)" }}
        >
          Contribution Skyline
        </h2>

        <div
          className="inline-flex items-center gap-1 rounded-lg border p-1"
          style={{
            background: "var(--bg-sunken)",
            borderColor: "var(--border-card)",
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
                className="cursor-pointer rounded-md border-0 px-3 py-1.5 text-sm font-medium transition-colors"
                style={{
                  background: active ? "var(--text-main)" : "transparent",
                  color: active ? "var(--bg-card)" : "var(--text-sub)",
                }}
              >
                {opt.label}
              </button>
            )
          })}
        </div>
      </div>

      {isLoading ? (
        <div className="shadow-panel w-full space-y-5 rounded-lg bg-transparent p-4">
          <Skeleton className="h-32 w-full rounded-lg" />
          <div className="space-y-3">
            <Skeleton className="h-3 w-3/5 rounded-lg" />
            <Skeleton className="h-3 w-4/5 rounded-lg" />
            <Skeleton className="h-3 w-2/5 rounded-lg" />
          </div>
        </div>
      ) : (
        <ContributionSkyline
          data={userData}
          defaultView="3d"
          palette={palette}
          unit="submission"
          unitPlural="submissions"
        />
      )}
    </div>
  )
}

const profileMountEl = document.getElementById("dashboard-profile-root")
if (profileMountEl) {
  ReactDOM.createRoot(profileMountEl).render(
    <React.StrictMode>
      <DashboardProfileSection />
    </React.StrictMode>
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
