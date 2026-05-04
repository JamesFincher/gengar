declare global {
  interface Window {
    /** Set true by the server only for `gengar dashboard --tui` (or GENGAR_DASHBOARD_TUI=1). */
    __GENGAR_DASHBOARD_EMBEDDED_CHAT__?: boolean;
    /** @deprecated Older injected name; treated as on when true. */
    __GENGAR_DASHBOARD_TUI__?: boolean;
  }
}

/** True only when the dashboard was started with embedded TUI Chat (`gengar dashboard --tui`). */
export function isDashboardEmbeddedChatEnabled(): boolean {
  if (typeof window === "undefined") return false;
  if (window.__GENGAR_DASHBOARD_EMBEDDED_CHAT__ === true) return true;
  return window.__GENGAR_DASHBOARD_TUI__ === true;
}
