import {
  collection,
  getDocs,
  doc,
  getDoc,
  setDoc,
  updateDoc,
  query,
  where,
  orderBy,
  limit,
  serverTimestamp,
} from 'firebase/firestore';
import { db } from '../firebase';
import type { UserProfile, ProblemDoc, SubmissionDoc, AuditLogDoc, ReportDoc } from './types';

export async function logAdminAction(
  adminUid: string,
  adminEmail: string,
  action: string,
  targetType: 'user' | 'problem' | 'admin' | 'announcement' | 'report' | 'system',
  targetId: string,
  details?: Record<string, any>
): Promise<void> {
  const logId = 'log_' + Date.now().toString(36) + '_' + Math.random().toString(36).slice(2, 6);
  const logRef = doc(db, 'auditLogs', logId);
  await setDoc(logRef, {
    id: logId,
    adminUid,
    adminEmail,
    action,
    targetType,
    targetId,
    details: details || {},
    timestamp: serverTimestamp(),
  });
}

export async function fetchPlatformOverview(): Promise<{
  totalUsers: number;
  activeUsers: number;
  totalSubmissions: number;
  totalProblems: number;
}> {
  try {
    const res = await fetch('/api/admin/overview');
    if (res.ok) {
      return await res.json();
    }
  } catch (err) {
    console.warn('Could not fetch admin overview:', err);
  }
  return {
    totalUsers: 0,
    activeUsers: 0,
    totalSubmissions: 0,
    totalProblems: 41,
  };
}
