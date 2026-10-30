import {
  collection,
  getDocs,
  query,
  where,
  orderBy,
  limit,
} from 'firebase/firestore';
import { db } from '../firebase';
import type { ProblemProgress, DailyActivity, UserStats } from './types';

export async function getUserProblemProgress(userId: string): Promise<Record<string, ProblemProgress>> {
  if (!userId) return {};
  try {
    const progressRef = collection(db, 'users', userId, 'progress');
    const snap = await getDocs(progressRef);
    const map: Record<string, ProblemProgress> = {};
    snap.forEach((d) => {
      map[d.id] = d.data() as ProblemProgress;
    });
    return map;
  } catch (err) {
    console.warn('Could not load user progress from Firestore:', err);
    return {};
  }
}

export async function getUserActivityHistory(
  userId: string,
  limitDays: number = 365
): Promise<DailyActivity[]> {
  if (!userId) return [];
  try {
    const actRef = collection(db, 'users', userId, 'activity');
    const q = query(actRef, orderBy('date', 'desc'), limit(limitDays));
    const snap = await getDocs(q);
    return snap.docs.map((d) => d.data() as DailyActivity);
  } catch (err) {
    console.warn('Could not load user activity history:', err);
    return [];
  }
}

export function computeOopMastery(progressList: ProblemProgress[]) {
  const topics = {
    'Encapsulation': { total: 10, solved: 0 },
    'Inheritance': { total: 12, solved: 0 },
    'Polymorphism': { total: 9, solved: 0 },
    'Abstraction': { total: 10, solved: 0 },
    'Collections': { total: 8, solved: 0 },
  };

  progressList.forEach((p) => {
    if (p.status === 'solved') {
      (p.topics || []).forEach((t) => {
        Object.keys(topics).forEach((k) => {
          if (t.toLowerCase().includes(k.toLowerCase())) {
            topics[k as keyof typeof topics].solved++;
          }
        });
      });
    }
  });

  return Object.entries(topics).map(([name, data]) => ({
    name,
    solved: data.solved,
    total: data.total,
    percentage: Math.min(100, Math.round((data.solved / Math.max(data.total, 1)) * 100)),
  }));
}
