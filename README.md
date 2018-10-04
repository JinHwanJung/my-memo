# 자주 찾아보는 것들 정리

### prevent master commit & merge
- link: https://stackoverflow.com/questions/40462111/git-prevent-commits-in-master-branch

1. .git/hooks/pre-commit

```bash
#!/bin/sh
branch="$(git rev-parse --abbrev-ref HEAD)"

if [ "$branch" = "master" ]; then
  echo "You can't commit directly to master branch"
  exit 1
fi
```
2. Make it executable
```bash
chmod +x .git/hooks/pre-commit
```

3. .git/config file:
```bash
[branch "master"]
    mergeoptions = --no-ff
```