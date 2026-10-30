import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { doc, writeBatch, serverTimestamp } from 'firebase/firestore';
import { db } from '../src/firebase';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');

const PROBLEMS_DIR = path.join(ROOT_DIR, 'problems');
const STARTERS_DIR = path.join(ROOT_DIR, 'starters');
const REFERENCE_DIR = path.join(ROOT_DIR, 'reference');
const PROBLEMS_META_PATH = path.join(ROOT_DIR, 'problems_meta.json');

export async function migrateAllProblems() {
  console.log('Starting migration of 41 Java problems into Firestore...');
  if (!fs.existsSync(PROBLEMS_META_PATH)) {
    throw new Error('problems_meta.json not found');
  }

  const metaAll = JSON.parse(fs.readFileSync(PROBLEMS_META_PATH, 'utf-8'));
  const problemFolders = fs
    .readdirSync(PROBLEMS_DIR, { withFileTypes: true })
    .filter((d) => d.isDirectory() && /^[a-z0-9-]+$/.test(d.name))
    .map((d) => d.name)
    .sort();

  console.log(`Found ${problemFolders.length} problem folders.`);

  // Write in chunks of 20 (Firestore batch limit is 500)
  const batch = writeBatch(db);
  let count = 0;

  for (const id of problemFolders) {
    const meta = metaAll[id] || {};
    const problemDir = path.join(PROBLEMS_DIR, id);

    const readSafe = (p: string) => (fs.existsSync(p) ? fs.readFileSync(p, 'utf-8') : '');
    const readme = readSafe(path.join(problemDir, 'README.md'));
    const solution = readSafe(path.join(problemDir, 'Solution.java'));
    const starter = readSafe(path.join(STARTERS_DIR, id, 'Solution.java')) || solution;

    const lines = readme.split(/\r?\n/);
    const titleLine = lines.find((l) => l.startsWith('# '));
    const title = titleLine
      ? titleLine.slice(2).trim()
      : id.split('-').map((w) => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');

    const summaryLine = lines.find(
      (l) => l.trim() && !l.startsWith('#') && !l.startsWith('*Source:')
    );
    const summary = summaryLine ? summaryLine.trim() : meta.summary || `Practice ${title} in Java.`;

    const probDocRef = doc(db, 'problems', id);
    batch.set(
      probDocRef,
      {
        id,
        display_number: meta.display_number ?? count + 1,
        display_id: meta.id ?? String(count + 1).padStart(2, '0'),
        title,
        summary,
        readme,
        starter,
        difficulty: meta.difficulty || 'Easy',
        topics: meta.topics || ['Object-Oriented Programming'],
        languages: meta.languages || ['Java'],
        path_id: meta.path_id || 'java-basics',
        path_name: meta.path_name || 'Java Basics',
        order_in_path: meta.order_in_path || count + 1,
        collection_ids: meta.collection_ids || [],
        sample_cases: meta.sample_cases || [],
        hints: meta.hints || [],
        published: true,
        isArchived: false,
        totalSubmissions: 0,
        acceptedSubmissions: 0,
        createdAt: serverTimestamp(),
        updatedAt: serverTimestamp(),
      },
      { merge: true }
    );
    count++;
  }

  // Also seed learning paths
  if (metaAll._paths && Array.isArray(metaAll._paths)) {
    for (const p of metaAll._paths) {
      if (p.id) {
        const pathRef = doc(db, 'learningPaths', p.id);
        batch.set(
          pathRef,
          {
            id: p.id,
            title: p.title || p.id,
            description: p.description || '',
            order: p.order || 1,
            problemIds: p.problem_ids || [],
            createdAt: serverTimestamp(),
          },
          { merge: true }
        );
      }
    }
  }

  // Also seed curated collections
  if (metaAll._collections && Array.isArray(metaAll._collections)) {
    for (const c of metaAll._collections) {
      if (c.id) {
        const colRef = doc(db, 'collections', c.id);
        batch.set(
          colRef,
          {
            id: c.id,
            title: c.title || c.id,
            description: c.description || '',
            problemIds: c.problem_ids || [],
            createdAt: serverTimestamp(),
          },
          { merge: true }
        );
      }
    }
  }

  await batch.commit();
  console.log(`Successfully migrated ${count} problems to Firestore collection 'problems'!`);
  return count;
}

// If run directly
if (process.argv[1] && process.argv[1].includes('migrate-problems')) {
  migrateAllProblems()
    .then((n) => {
      console.log(`Migration finished for ${n} problems.`);
      process.exit(0);
    })
    .catch((err) => {
      console.error('Migration failed:', err);
      process.exit(1);
    });
}
