import React, { useState, useMemo, useEffect, useRef } from "react"
import ReactDOM from "react-dom/client"
import { Check, Camera } from "lucide-react"
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
import { auth, onAuthStateChanged } from "./firebase"
import "./styles/tailwind.css"

/**
 * Default Gmail / Google Account style circular user silhouette photo (SVG data URI).
 */
const DEFAULT_GMAIL_USER_PHOTO =
  "data:image/svg+xml;utf8," +
  encodeURIComponent(
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" fill="none">
      <rect width="128" height="128" rx="64" fill="#E8EAED"/>
      <circle cx="64" cy="48" r="22" fill="#9AA0A6"/>
      <path d="M20 116C20 92.8 39.7 76 64 76C88.3 76 108 92.8 108 116" fill="#9AA0A6"/>
    </svg>`
  )

function isRealPhotoUrl(url?: string | null): url is string {
  if (!url || typeof url !== "string") return false
  const trimmed = url.trim()
  if (!trimmed) return false
  // Exclude generated MorphingFace SVG data URIs
  if (trimmed.startsWith("data:image/svg+xml")) return false
  return (
    trimmed.startsWith("https://") ||
    trimmed.startsWith("http://") ||
    trimmed.startsWith("data:image/")
  )
}

interface StoredUserProfile {
  id: string
  username: string
  name: string
  email?: string
  photoUrl: string
  avatarMode: "photo" | "custom-avatar"
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
    const uploadedPhoto = localStorage.getItem("ck_profile_photo")

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

    const firebasePhoto =
      auth.currentUser?.photoURL ||
      auth.currentUser?.providerData?.find((p) => p?.photoURL)?.photoURL ||
      null

    const candidatePhoto =
      (isRealPhotoUrl(uploadedPhoto) && uploadedPhoto) ||
      (isRealPhotoUrl(firebasePhoto) && firebasePhoto) ||
      (isRealPhotoUrl(user.googlePhoto) && user.googlePhoto) ||
      (isRealPhotoUrl(user.photoURL) && user.photoURL) ||
      (isRealPhotoUrl(user.picture) && user.picture) ||
      (isRealPhotoUrl(user.avatar) && user.avatar) ||
      (isRealPhotoUrl(ckUser?.picture) && ckUser.picture) ||
      DEFAULT_GMAIL_USER_PHOTO

    const avatarMode: "photo" | "custom-avatar" =
      avatarData?.mode === "custom-avatar" ? "custom-avatar" : "photo"

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
      photoUrl: candidatePhoto,
      avatarMode,
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
      photoUrl: DEFAULT_GMAIL_USER_PHOTO,
      avatarMode: "photo",
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
  const [photoUrl, setPhotoUrl] = useState<string>(initialProfile.photoUrl)
  const [avatarMode, setAvatarMode] = useState<"photo" | "custom-avatar">(
    initialProfile.avatarMode
  )
  const [savedNotice, setSavedNotice] = useState(false)
  const [showPicker, setShowPicker] = useState(false)
  const [isLoading, setIsLoading] = useState(true)
  const fileInputRef = useRef<HTMLInputElement | null>(null)

  useEffect(() => {
    const timer = setTimeout(() => setIsLoading(false), 600)
    return () => {
      clearTimeout(timer)
    }
  }, [])

  // Sync Gmail / Google photoURL if Firebase Auth resolves after initial render
  useEffect(() => {
    const unsub = onAuthStateChanged(auth, (fbUser) => {
      if (!fbUser) return
      const uploaded = localStorage.getItem("ck_profile_photo")
      if (isRealPhotoUrl(uploaded)) {
        setPhotoUrl(uploaded)
        return
      }
      const gmailPhoto =
        fbUser.photoURL ||
        fbUser.providerData?.find((p) => p?.photoURL)?.photoURL ||
        null
      if (isRealPhotoUrl(gmailPhoto)) {
        setPhotoUrl(gmailPhoto)
        try {
          const rawSession = localStorage.getItem("oops_session")
          if (rawSession) {
            const sessionObj = JSON.parse(rawSession)
            sessionObj.googlePhoto = gmailPhoto
            if (avatarMode === "photo") {
              sessionObj.picture = gmailPhoto
              sessionObj.avatar = gmailPhoto
            }
            localStorage.setItem("oops_session", JSON.stringify(sessionObj))
          }
        } catch {
          // ignore storage error
        }
      }
    })
    return () => unsub()
  }, [avatarMode])

  const currentSeed = avatarSeed(avatarVal.displayName || "Coder", avatarVal.variant)
  const handleSlug =
    (avatarVal.displayName || initialProfile.username || "coder")
      .trim()
      .toLowerCase()
      .replace(/[^a-z0-9_]/g, "") || "coder"

  const syncSessionPhoto = (newPictureUri: string, nextDisplayName?: string) => {
    try {
      const nameToSave = (nextDisplayName ?? avatarVal.displayName).trim() || "CodeKaro Coder"
      const rawSession = localStorage.getItem("oops_session")
      const sessionObj = rawSession
        ? JSON.parse(rawSession)
        : { id: initialProfile.id || "local_user" }
      sessionObj.name = nameToSave
      sessionObj.username = sessionObj.username || handleSlug
      sessionObj.avatar = newPictureUri
      sessionObj.picture = newPictureUri
      localStorage.setItem("oops_session", JSON.stringify(sessionObj))

      const rawCk = localStorage.getItem("ck_user")
      if (rawCk) {
        const ckObj = JSON.parse(rawCk)
        ckObj.name = nameToSave
        ckObj.avatar = newPictureUri
        ckObj.picture = newPictureUri
        localStorage.setItem("ck_user", JSON.stringify(ckObj))
      }

      window.dispatchEvent(new Event("storage"))
    } catch {
      // ignore storage errors
    }
  }

  const handlePhotoUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return
    const reader = new FileReader()
    reader.onload = () => {
      const img = new Image()
      img.onload = () => {
        const canvas = document.createElement("canvas")
        const maxDim = 256
        let w = img.width
        let h = img.height
        if (w > h) {
          if (w > maxDim) {
            h = Math.round((h * maxDim) / w)
            w = maxDim
          }
        } else {
          if (h > maxDim) {
            w = Math.round((w * maxDim) / h)
            h = maxDim
          }
        }
        canvas.width = w
        canvas.height = h
        const ctx = canvas.getContext("2d")
        if (ctx) {
          ctx.drawImage(img, 0, 0, w, h)
          const dataUrl = canvas.toDataURL("image/jpeg", 0.88)
          try {
            localStorage.setItem("ck_profile_photo", dataUrl)
            const rawAvatar = localStorage.getItem("ck_avatar")
            const avatarObj = rawAvatar ? JSON.parse(rawAvatar) : {}
            avatarObj.mode = "photo"
            localStorage.setItem("ck_avatar", JSON.stringify(avatarObj))
          } catch {
            // ignore quota errors
          }
          setPhotoUrl(dataUrl)
          setAvatarMode("photo")
          syncSessionPhoto(dataUrl)
          setSavedNotice(true)
          setTimeout(() => setSavedNotice(false), 2400)
        }
      }
      if (typeof reader.result === "string") {
        img.src = reader.result
      }
    }
    reader.readAsDataURL(file)
    e.target.value = ""
  }

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
          mode: "custom-avatar",
        })
      )
      setAvatarMode("custom-avatar")
      syncSessionPhoto(dataUri, next.displayName)
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

  const showAnimatedFace = showPicker || avatarMode === "custom-avatar"

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
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              title="Add or change profile photo"
              className="group relative h-20 w-20 shrink-0 cursor-pointer overflow-hidden rounded-full border p-0 shadow-sm"
              style={{
                borderColor: "var(--border-card)",
                background: "var(--bg-sunken)",
              }}
            >
              {showAnimatedFace ? (
                <MorphingFace seed={currentSeed} />
              ) : (
                <img
                  src={photoUrl || DEFAULT_GMAIL_USER_PHOTO}
                  alt={avatarVal.displayName || "User profile photo"}
                  referrerPolicy="no-referrer"
                  onError={(e) => {
                    const target = e.currentTarget
                    if (target.src !== DEFAULT_GMAIL_USER_PHOTO) {
                      target.src = DEFAULT_GMAIL_USER_PHOTO
                    }
                  }}
                  className="h-full w-full object-cover"
                />
              )}
              <span className=" absolute inset-0 flex items-center justify-center bg-black/45 opacity-0 transition-opacity group-hover:opacity-100">
                <Camera className="size-5 text-white" />
              </span>
            </button>

            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              onChange={handlePhotoUpload}
              className="hidden"
              aria-label="Upload profile photo"
            />

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

          <div className="flex flex-wrap items-center gap-2.5">
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              className="inline-flex cursor-pointer items-center justify-center gap-1.5 rounded-lg border px-4 py-2 text-sm font-semibold transition-opacity hover:opacity-90"
              style={{
                background: "var(--bg-sunken)",
                color: "var(--text-main)",
                borderColor: "var(--border-card)",
              }}
            >
              <Camera className="size-4" />
              Add Photo
            </button>
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
