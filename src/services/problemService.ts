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
  updateDoc,
  serverTimestamp,
} from 'firebase/firestore';
import { db } from '../firebase';
import type { ProblemDoc } from './types';

export async function getPublishedProblems(): Promise<ProblemDoc[]> {
  try {
    const problemsRef = collection(db, 'problems');
    const q = query(
      problemsRef,
      where('published', '==', true),
      where('isArchived', '==', false)
    );
    const snap = await getDocs(q);
    if (!snap.empty) {
      return snap.docs.map((d) => ({ id: d.id, ...(d.data() as Omit<ProblemDoc, 'id'>) }));
    }
  } catch (err) {
    console.warn('Could not query Firestore problems:', err);
  }

  // Fallback to local API
  try {
    const res = await fetch('/api/problems');
    const contentType = res.headers.get('content-type') || '';
    if (res.ok && contentType.includes('application/json')) {
      const data = await res.json();
      if (data && Array.isArray(data.problems)) {
        return data.problems;
      }
    }
  } catch (err) {
    console.warn('Fallback api/problems fetch failed:', err);
  }

  return [];
}

export async function getProblemById(problemId: string): Promise<ProblemDoc | null> {
  if (!problemId) return null;
  try {
    const problemRef = doc(db, 'problems', problemId);
    const snap = await getDoc(problemRef);
    if (snap.exists()) {
      return { id: snap.id, ...(snap.data() as Omit<ProblemDoc, 'id'>) };
    }
  } catch (err) {
    console.warn('Firestore getProblemById fallback:', err);
  }

  // Fallback to local endpoint
  try {
    const res = await fetch(`/api/problems/${problemId}`);
    const contentType = res.headers.get('content-type') || '';
    if (res.ok && contentType.includes('application/json')) {
      return await res.json();
    }
  } catch {
    // Ignore
  }
  return null;
}

export async function saveProblemDoc(problem: ProblemDoc): Promise<void> {
  const problemRef = doc(db, 'problems', problem.id);
  await setDoc(
    problemRef,
    {
      ...problem,
      updatedAt: serverTimestamp(),
    },
    { merge: true }
  );
}
