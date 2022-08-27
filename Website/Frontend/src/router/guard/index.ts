import { Router } from 'vue-router'
import { createPageLoadingGuard } from './page-loading-guard'

export function setupRouterGuard(router: Router) {
  createPageLoadingGuard(router)
}
