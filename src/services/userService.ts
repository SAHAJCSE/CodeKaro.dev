import {
  doc,
  getDoc,
  setDoc,
  updateDoc,
  deleteDoc,
  collection,
  getDocs,
  serverTimestamp,
} from 'firebase/firestore';
import { db } from '../firebase';
import type { UserProfile, ProblemBookmark } from './types';

export const SUPER_ADMIN_EMAIL = 'sahajsingh81844@gmail.com';

export async function getUserProfile(uid: string): Promise<UserProfile | null> {
  if (!uid) return null;
  const userRef = doc(db, 'users', uid);
  const snap = await getDoc(userRef);
  if (!snap.exists()) return null;
  return snap.data() as UserProfile;
}

export async function updateUserProfile(
  uid: string,
  updates: Partial<Pick<UserProfile, 'displayName' | 'photoURL' | 'username'>>
): Promise<void> {
  const userRef = doc(db, 'users', uid);
  await updateDoc(userRef, {
    ...updates,
    updatedAt: serverTimestamp(),
  });
}

export async function getUserBookmarks(uid: string): Promise<string[]> {
  if (!uid) return [];
  const bookmarksRef = collection(db, 'users', uid, 'bookmarks');
  const snap = await getDocs(bookmarksRef);
  return snap.docs.map((d) => d.id);
}

export async function toggleBookmark(uid: string, problemId: string): Promise<boolean> {
  if (!uid || !problemId) return false;
  const bookmarkRef = doc(db, 'users', uid, 'bookmarks', problemId);
  const snap = await getDoc(bookmarkRef);
  if (snap.exists()) {
    await deleteDoc(bookmarkRef);
    return false;
  } else {
    await setDoc(bookmarkRef, {
      problemId,
      userId: uid,
      createdAt: serverTimestamp(),
    });
    return true;
  }
}
