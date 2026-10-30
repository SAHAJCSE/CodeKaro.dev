import type { Timestamp } from 'firebase/firestore';

export interface UserStats {
  totalSolved: number;
  easySolved: number;
  mediumSolved: number;
  hardSolved: number;
  totalSubmissions: number;
  acceptedSubmissions: number;
  acceptanceRate: number;
  currentStreak: number;
  longestStreak: number;
  lastActiveDate: string;
}

export interface UserProfile {
  uid: string;
  username: string;
  displayName: string;
  photoURL?: string;
  email?: string;
  role: 'student' | 'admin';
  adminRole?: 'super_admin' | 'content_admin' | 'moderator' | 'support_admin';
  status: 'active' | 'suspended';
  provider: 'google' | 'github' | 'email';
  otpVerified: boolean;
  stats: UserStats;
  createdAt: any;
  updatedAt: any;
}

export interface ProblemProgress {
  problemId: string;
  userId: string;
  status: 'solved' | 'attempted';
  difficulty?: 'Easy' | 'Medium' | 'Hard';
  topics?: string[];
  attemptsCount: number;
  bestRuntimeMs?: number | null;
  firstSolvedAt?: any;
  lastSubmittedAt: any;
  updatedAt: any;
}

export interface ProblemBookmark {
  problemId: string;
  userId: string;
  createdAt: any;
}

export interface DailyActivity {
  date: string;
  userId: string;
  submissionCount: number;
  acceptedCount: number;
  problemsSolved?: string[];
  updatedAt: any;
}

export interface ProblemDoc {
  id: string;
  display_number?: number;
  display_id?: string;
  title: string;
  summary: string;
  readme?: string;
  starter: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  topics: string[];
  languages: string[];
  path_id?: string;
  path_name?: string;
  order_in_path?: number;
  collection_ids?: string[];
  sample_cases?: Array<{ name?: string; input: string; expected: string }>;
  hints?: string[];
  published: boolean;
  isArchived: boolean;
  totalSubmissions: number;
  acceptedSubmissions: number;
  createdAt: any;
  updatedAt: any;
}

export type SubmissionVerdict =
  | 'ACCEPTED'
  | 'WRONG_ANSWER'
  | 'COMPILATION_ERROR'
  | 'RUNTIME_ERROR'
  | 'TIME_LIMIT_EXCEEDED'
  | 'MEMORY_LIMIT_EXCEEDED'
  | 'INTERNAL_ERROR';

export interface SubmissionDoc {
  submissionId: string;
  userId: string;
  problemId: string;
  problemTitle?: string;
  language: string;
  sourceCode: string;
  status: 'PENDING' | 'RUNNING' | 'COMPLETED';
  verdict?: SubmissionVerdict;
  passedTests?: number;
  totalTests?: number;
  runtimeMs?: number;
  memoryKb?: number;
  output?: string;
  submittedAt: any;
  evaluatedAt?: any;
}

export interface LearningPathDoc {
  id: string;
  title: string;
  description: string;
  order: number;
  problemIds: string[];
  icon?: string;
  createdAt: any;
  updatedAt?: any;
}

export interface CollectionDoc {
  id: string;
  title: string;
  description: string;
  problemIds: string[];
  createdAt: any;
}

export interface AnnouncementDoc {
  id: string;
  title: string;
  content: string;
  authorId: string;
  authorName?: string;
  priority: 'low' | 'normal' | 'high';
  isPublished: boolean;
  publishedAt: any;
  expiresAt?: any;
}

export interface ReportDoc {
  id: string;
  userId: string;
  userEmail?: string;
  problemId: string;
  type: 'bug' | 'test_case_error' | 'problem_description' | 'other';
  message: string;
  status: 'open' | 'in_review' | 'resolved' | 'dismissed';
  resolvedBy?: string | null;
  resolvedAt?: any;
  createdAt: any;
}

export interface AdminProfileDoc {
  uid: string;
  email: string;
  role: 'super_admin' | 'content_admin' | 'moderator' | 'support_admin';
  permissions: string[];
  isSuspended: boolean;
  assignedBy: string;
  assignedAt: any;
  updatedAt: any;
}

export interface AuditLogDoc {
  id: string;
  adminUid: string;
  adminEmail: string;
  action: string;
  targetType: 'user' | 'problem' | 'admin' | 'announcement' | 'report' | 'system';
  targetId: string;
  details?: Record<string, any>;
  timestamp: any;
}
