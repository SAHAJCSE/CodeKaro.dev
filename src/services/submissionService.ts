import {
  doc,
  getDoc,
  getDocs,
  collection,
  query,
  where,
  orderBy,
  limit,
  setDoc,
  serverTimestamp,
} from 'firebase/firestore';
import { db } from '../firebase';
import type { SubmissionDoc } from './types';

export async function createPendingSubmission(
  userId: string,
  problemId: string,
  problemTitle: string,
  sourceCode: string,
  language: string = 'Java'
): Promise<string> {
  const submissionId = 'sub_' + Date.now().toString(36) + '_' + Math.random().toString(36).slice(2, 7);
  const subRef = doc(db, 'submissions', submissionId);

  await setDoc(subRef, {
    submissionId,
    userId,
    problemId,
    problemTitle,
    language,
    sourceCode,
    status: 'PENDING',
    submittedAt: serverTimestamp(),
  });

  return submissionId;
}

export async function getUserSubmissions(
  userId: string,
  limitCount: number = 20
): Promise<SubmissionDoc[]> {
  if (!userId) return [];
  try {
    const subsRef = collection(db, 'submissions');
    const q = query(
      subsRef,
      where('userId', '==', userId),
      orderBy('submittedAt', 'desc'),
      limit(limitCount)
    );
    const snap = await getDocs(q);
    return snap.docs.map((d) => d.data() as SubmissionDoc);
  } catch (err) {
    console.warn('Could not query Firestore submissions:', err);
    return [];
  }
}

export async function getSubmissionById(submissionId: string): Promise<SubmissionDoc | null> {
  if (!submissionId) return null;
  const subRef = doc(db, 'submissions', submissionId);
  const snap = await getDoc(subRef);
  if (!snap.exists()) return null;
  return snap.data() as SubmissionDoc;
}
