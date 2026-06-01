# path: Makefile
.DEFAULT_GOAL := help
.PHONY: help refs-sync refs-status refs-clean index

help: ## List available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

refs-sync: ## Hydrate every reference to its pinned ref (references/*.lock)
	@bash scripts/refs-sync.sh sync

refs-status: ## Show pinned ref vs. what is on disk
	@bash scripts/refs-sync.sh status

refs-clean: ## Remove hydrated reference content (lockfiles stay)
	@bash scripts/refs-sync.sh clean

index: ## Regenerate .claude/state/index.yaml from artifact headers
	@python3 scripts/build-index.py
