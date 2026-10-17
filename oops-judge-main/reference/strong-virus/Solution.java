class Virus {
    boolean isStrongVirus(String dna) {
        for (int i = 0; i + 4 < dna.length(); i++) {
            char a = dna.charAt(i), b = dna.charAt(i + 4);
            if ((a == 'x' && b == 'y') || (a == 'y' && b == 'x')) return true;
        }
        return false;
    }
}
