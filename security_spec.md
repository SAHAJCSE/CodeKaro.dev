# Firestore Security Specification (`security_spec.md`)

## 1. Data Invariants
1. **Default-Deny Catch-All**: All paths not explicitly matched (`/databases/{database}/documents/{document=**}`) deny all reads and writes.
2. **Identity & Ownership**: A `UserProfile` at `/users/{userId}` can only be created or updated if `request.auth != null`, `request.auth.uid == userId`, and `incoming().uid == request.auth.uid`.
3. **Path Variable Hardening**: `userId` and `docId` path variables must satisfy `isValidId()` (`id is string && id.size() >= 1 && id.size() <= 128 && id.matches('^[a-zA-Z0-9_\\-]+$')`).
4. **PII Isolation (Split Collection)**: Private user data (`email`) is isolated in `/users/{userId}/private/{docId}`, readable and writable strictly by the owner (`request.auth.uid == userId`), and requires the parent `/users/{userId}` document to exist (`exists()` or `existsAfter()`).
5. **Immutable Fields**: `uid`, `provider`, and `createdAt` cannot be modified after creation.
6. **Temporal Integrity**: `createdAt` must equal `request.time` on `create`, and `updatedAt` must equal `request.time` on both `create` and `update`.
7. **Strict Key & Size Boundaries**: Every write must pass `isValidUserProfile(incoming())` or `isValidUserPrivate(incoming())` enforcing `hasAll`/`hasOnly` keys, exact types, and maximum string lengths.

## 2. The "Dirty Dozen" Adversarial Payloads
1. **Shadow Field Injection**: Creating `/users/user_1` with an undeclared field `{"isAdmin": true}` -> `PERMISSION_DENIED`.
2. **Identity Spoofing on Create**: User `user_1` creating `/users/user_1` with `{"uid": "user_2"}` -> `PERMISSION_DENIED`.
3. **Cross-User Profile Write**: User `user_1` attempting to update `/users/user_2` -> `PERMISSION_DENIED`.
4. **Immutable Field Mutation (`uid`)**: User `user_1` updating `uid` to `"user_99"` on `/users/user_1` -> `PERMISSION_DENIED`.
5. **Immutable Field Mutation (`createdAt`)**: User `user_1` updating `createdAt` on `/users/user_1` -> `PERMISSION_DENIED`.
6. **Forged Client Timestamp**: Creating `/users/user_1` with a past/future `createdAt` not matching `request.time` -> `PERMISSION_DENIED`.
7. **Denial-of-Wallet String Overflow**: Creating `/users/user_1` with a 5,000-char `displayName` (exceeds `maxLength: 100`) -> `PERMISSION_DENIED`.
8. **Invalid Provider Enum**: Creating `/users/user_1` with `provider: "hacker"` (not in `['google', 'github', 'email']`) -> `PERMISSION_DENIED`.
9. **PII Cross-Read Leak**: Authenticated user `user_2` attempting `get` on `/users/user_1/private/info` -> `PERMISSION_DENIED`.
10. **Orphaned Subcollection Write**: Creating `/users/user_1/private/info` when `/users/user_1` does not exist -> `PERMISSION_DENIED`.
11. **Value Poisoning on Update**: Updating `displayName` on `/users/user_1` with a number `12345` instead of a bounded string -> `PERMISSION_DENIED`.
12. **ID Poisoning Attack**: Targeting `/users/invalid$id!with*bad^chars` -> `PERMISSION_DENIED`.

## 3. Role-Based Access Control (RBAC) & Authorization
- **Student (Default)**: Automatically assigned on registration (`role: 'student'`). Can read published problems, manage personal bookmarks, create submissions in `PENDING` status, and view only their own progress and activity history.
- **Admin Roles**:
  - `super_admin`: Full administrative access. Root Super Admin (`sahajsingh81844@gmail.com`) is non-demotable and non-suspendable.
  - `content_admin`: Problem catalogue authoring, publishing, editing hints and test cases.
  - `moderator`: Reviewing submissions, handling student problem reports, and managing discussions.
  - `support_admin`: Account assistance, email verification status, and audit log inspection.
- **Server-Side Enforcement**: Verdict calculation, runtime/memory benchmarking, and test case pass rates are strictly evaluated server-side. Frontend clients cannot write `COMPLETED` or `ACCEPTED` verdicts directly.
- **Tamper-Proof Audit Logging**: Administrative mutations write immutable documents to `/auditLogs/{logId}`.

## 4. Collection Architecture (12 Collections)
| Collection Path | Access Control | Purpose |
|-----------------|----------------|---------|
| `/users/{uid}` | Owner read/write; public profile read | User profile, provider, stats |
| `/users/{uid}/progress/{problemId}` | Owner read/write; admin read | Problem solved status & attempts |
| `/users/{uid}/bookmarks/{problemId}` | Owner read/write | User bookmarked problems |
| `/users/{uid}/activity/{date}` | Owner read/write; admin read | Daily submission heatmap records |
| `/problems/{problemId}` | Public read (published); Admin write | 41 Java practice problems |
| `/submissions/{submissionId}` | Owner read; server evaluate | Persistent submission records |
| `/learningPaths/{pathId}` | Public read; Admin write | Structured Java learning curricula |
| `/collections/{collectionId}` | Public read; Admin write | Curated problem playlists |
| `/announcements/{announcementId}`| Public read; Admin write | Platform notices and releases |
| `/reports/{reportId}` | Owner create; Admin read/update | User bug/problem reports |
| `/adminProfiles/{uid}` | Admin read/write | Elevated permissions metadata |
| `/auditLogs/{logId}` | Admin read; Append-only | Security and governance trails |

## 5. Verification & Test Commands
- **Lint Security Rules**: `npm run lint`
- **Execute Security & Invariant Suite**: `npm run test:rules`
- **Deploy Rules**: Rules deployed via `deploy_firebase` to database `ai-studio-codekarodev-e24c4c0f-2f89-495d-b036-154b1080193b`.
