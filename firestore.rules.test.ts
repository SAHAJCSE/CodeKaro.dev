/**
 * Firestore Security Rules Test Suite (Dirty Dozen Verification)
 */
export interface DirtyDozenTestCase {
  id: number;
  name: string;
  path: string;
  operation: 'get' | 'list' | 'create' | 'update' | 'delete';
  authUid: string | null;
  payload?: Record<string, unknown>;
  expectedResult: 'PERMISSION_DENIED';
}

export const DIRTY_DOZEN_TESTS: DirtyDozenTestCase[] = [
  {
    id: 1,
    name: 'Shadow Field Injection',
    path: '/users/user_1',
    operation: 'create',
    authUid: 'user_1',
    payload: {
      uid: 'user_1',
      username: 'coder1',
      displayName: 'Coder One',
      provider: 'email',
      otpVerified: true,
      isAdmin: true,
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 2,
    name: 'Identity Spoofing on Create',
    path: '/users/user_1',
    operation: 'create',
    authUid: 'user_1',
    payload: {
      uid: 'user_2',
      username: 'coder1',
      displayName: 'Coder One',
      provider: 'email',
      otpVerified: true,
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 3,
    name: 'Cross-User Profile Write',
    path: '/users/user_2',
    operation: 'update',
    authUid: 'user_1',
    payload: {
      displayName: 'Hijacked Name',
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 4,
    name: 'Immutable Field Mutation (uid)',
    path: '/users/user_1',
    operation: 'update',
    authUid: 'user_1',
    payload: {
      uid: 'user_99',
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 5,
    name: 'Immutable Field Mutation (createdAt)',
    path: '/users/user_1',
    operation: 'update',
    authUid: 'user_1',
    payload: {
      createdAt: '2020-01-01T00:00:00Z',
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 6,
    name: 'Forged Client Timestamp',
    path: '/users/user_1',
    operation: 'create',
    authUid: 'user_1',
    payload: {
      uid: 'user_1',
      username: 'coder1',
      displayName: 'Coder One',
      provider: 'email',
      otpVerified: true,
      createdAt: '1999-01-01T00:00:00Z',
      updatedAt: '1999-01-01T00:00:00Z',
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 7,
    name: 'Denial-of-Wallet String Overflow',
    path: '/users/user_1',
    operation: 'create',
    authUid: 'user_1',
    payload: {
      uid: 'user_1',
      username: 'coder1',
      displayName: 'A'.repeat(500),
      provider: 'email',
      otpVerified: true,
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 8,
    name: 'Invalid Provider Enum',
    path: '/users/user_1',
    operation: 'create',
    authUid: 'user_1',
    payload: {
      uid: 'user_1',
      username: 'coder1',
      displayName: 'Coder One',
      provider: 'invalid_provider',
      otpVerified: true,
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 9,
    name: 'PII Cross-Read Leak',
    path: '/users/user_1/private/info',
    operation: 'get',
    authUid: 'user_2',
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 10,
    name: 'Orphaned Subcollection Write',
    path: '/users/non_existent_user/private/info',
    operation: 'create',
    authUid: 'non_existent_user',
    payload: {
      uid: 'non_existent_user',
      email: 'test@example.com',
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 11,
    name: 'Value Poisoning on Update',
    path: '/users/user_1',
    operation: 'update',
    authUid: 'user_1',
    payload: {
      displayName: 12345,
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 12,
    name: 'ID Poisoning Attack',
    path: '/users/invalid$id!bad',
    operation: 'get',
    authUid: 'user_1',
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 13,
    name: 'Student Self-Promotion on Registration',
    path: '/users/student_1',
    operation: 'create',
    authUid: 'student_1',
    payload: {
      uid: 'student_1',
      role: 'admin',
      status: 'active',
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 14,
    name: 'Student Role Escalation via Profile Update',
    path: '/users/student_1',
    operation: 'update',
    authUid: 'student_1',
    payload: {
      role: 'admin',
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 15,
    name: 'Direct Submission Verdict Tampering by Student',
    path: '/submissions/sub_101',
    operation: 'create',
    authUid: 'student_1',
    payload: {
      submissionId: 'sub_101',
      userId: 'student_1',
      status: 'COMPLETED',
      verdict: 'ACCEPTED',
    },
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 16,
    name: 'Cross-User Submission Inspection',
    path: '/submissions/sub_from_user_2',
    operation: 'get',
    authUid: 'student_1',
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 17,
    name: 'Unauthorized Problem Deletion by Student',
    path: '/problems/class-box',
    operation: 'delete',
    authUid: 'student_1',
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 18,
    name: 'Student Unauthorized Access to Admin Profiles',
    path: '/adminProfiles/admin_1',
    operation: 'get',
    authUid: 'student_1',
    expectedResult: 'PERMISSION_DENIED',
  },
  {
    id: 19,
    name: 'Immutable Audit Log Tampering',
    path: '/auditLogs/log_1',
    operation: 'update',
    authUid: 'super_admin_1',
    payload: {
      action: 'DELETED',
    },
    expectedResult: 'PERMISSION_DENIED',
  },
];
