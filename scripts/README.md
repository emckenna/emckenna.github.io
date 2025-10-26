# Scripts

## update-version.sh

Updates the version SHA in the footer of index.html to match the current git commit.

### Usage

```bash
./scripts/update-version.sh
```

### Automatic Updates

A pre-commit hook has been installed at `.git/hooks/pre-commit` that automatically runs this script on every commit. This ensures the version SHA is always up-to-date without manual intervention.

The hook will:
1. Run the update-version.sh script on every commit
2. Update the SHA to match the current commit
3. Stage the updated index.html
4. Continue with the commit

**Note:** Since git hooks are not tracked in the repository, you'll need to manually install the pre-commit hook on new clones:

```bash
cp scripts/pre-commit.sample .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
